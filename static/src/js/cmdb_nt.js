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
        start:function(model){
            switch(model){
                case "cinda_cmdb.base_type":this.addJumpEvent("deviceRoom");break;
                case "cinda_cmdb.cabinet":this.addJumpEvent("cabinet");break;
            }
        },
        addJumpEvent:function(title){
            var me=this;
            //由于form的展示界面禁用了单击事件，此处采用鼠标抬起事件代替
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
                title: _t("机房 - "+data.roomName)
            },canvas).open();
            $("#myCanvas").engineRoom().start(data).init();
        },
        cabDialog:function(data){//机柜弹出框
            var canvas=QWeb.render("cmdb",{h:500,w:597});
            var $dialog=new instance.web.Dialog(null,{
                size: 'medium',
                dialogClass: 'oe_act_window',
                title: _t("机柜 - "+data.name)
            },canvas).open();
            $("#myCanvas").cabinet_v().start(data).init();
        }
    });

    instance.web.FormView.include({
        load_form:function(data){
            var self = this;
            var cinda_cmdb = new instance.cinda_cmdb.Widget(self);
            cinda_cmdb.start(data.model);
            return this._super.apply(this, arguments);
        }
    });

    //合同统计
    instance.cinda_cmdb.Contract = instance.web.Widget.extend({
        template:"cmdb.contract",
        init:function(){
            this.data = null;
        },
        start:function(){
            /*this.rpc("/connum/").then(function(data){
                console.log(data);
            },function(err){
                console.log(err);
            });*/
            var me = this;
            $.get("/connum/",function(data){
                me.data = data;
                me.setData()
            },"json")
        },
        setData:function(){
            this.$el.find('.new_num').html(this.data["new_num"]);
            this.$el.find('.old_num').html(this.data["old_num"]);
        }
    });

    instance.web.ViewManagerAction.include({
        set_title:function(title){
            if(this.dataset && this.active_view =="list" && this.dataset.model == "cinda_cmdb.contract_purchase"){
                if(this.$el.find('.contract_total').length == 0){
                    var contract = new instance.cinda_cmdb.Contract(this);
                    contract.insertAfter(this.$el.find('.oe_breadcrumb_title:first'));
                }
            }else{
                this.$el.find('.contract_total').remove();
            }
            return this._super.apply(this, arguments);
        }
    });
}