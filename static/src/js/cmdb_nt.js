/**
 * Created by nantian on 2016/12/14.
 */
openerp.cmdb=function(instance){
    var _t=instance.web._t,
        _lt=instance.web._lt,
        QWeb=instance.web.qweb;
    instance.cmdb={};

    instance.cmdb.Widget=instance.web.Widget.extend({
        init:function(){
            //暂时不需要
        },
        start:function(o){
            var displayName=o.client.action_manager.inner_action.display_name;
            switch(displayName){
                case "机房":this.addJumpEvent("机房");break;
                case "机柜表":console.log(2);break;
            }
        },
        addJumpEvent:function(){
            var me=this;
            $("div.oe_view_manager_view_form").on("mouseup","span.oe_form_char_content",function(){
                me.popDialog();
            });
        },
        popDialog:function(){
            var canvas=QWeb.render("cmdb",{h:500,w:898});
            var $dialog=new instance.web.Dialog(null,{
                size: 'large',
                dialogClass: 'oe_act_window',
                title: _t("机房")
            },canvas).open();

        }
    });

    //当视图加载时调用自己指定代码
    instance.web.actionList.push(new instance.cmdb.Widget());
}