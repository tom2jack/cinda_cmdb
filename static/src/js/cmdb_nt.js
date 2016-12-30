/**
 * Created by nantian on 2016/12/14.
 */
openerp.cinda_cmdb=function(instance){
    var _t=instance.web._t,
        _lt=instance.web._lt,
        QWeb=instance.web.qweb;
    instance.cinda_cmdb={};

    instance.cinda_cmdb.Widget=instance.web.Widget.extend({
        init:function(){
            //暂时不需要
        },
        start:function(o){
            var displayName=o.client.action_manager.inner_action.display_name;
            switch(displayName){
                case "机房":this.addJumpEvent("deviceRoom");break;
                case "机柜表":this.addJumpEvent("cabinet");break;
            }
        },
        addJumpEvent:function(title){
            var me=this;
            $("div.oe_view_manager_view_form").on("mouseup","a.self_add_link",function(){
                var id=$(this).find("span.oe_form_char_content").html()-0;
                if(title=="deviceRoom"){
                    $.post("/cabinet_data/",{id:id},function(d){
                        me.dRDialog(d);
                    },"json");
                }else if(title=="cabinet"){
                    $.post("/u_data/",{id:id},function(d){
                        me.cabDialog(d);
                    },"json");
                }

            });
        },
        dRDialog:function(data){//机房弹出框
            var canvas=QWeb.render("cmdb",{h:500,w:898});
            var $dialog=new instance.web.Dialog(null,{
                size: 'large',
                dialogClass: 'oe_act_window',
                title: _t("机房")
            },canvas).open();
            $("#myCanvas").engineRoom().start(data).init();
        },
        cabDialog:function(data){//机柜弹出框
            var canvas=QWeb.render("cmdb",{h:500,w:597});
            var $dialog=new instance.web.Dialog(null,{
                size: 'medium',
                dialogClass: 'oe_act_window',
                title: _t("机柜")
            },canvas).open();
            $("#myCanvas").cabinet_v().start(data).init();
        }
    });

    //当视图加载时调用自己指定代码
    instance.web.actionList.push(new instance.cinda_cmdb.Widget());
}