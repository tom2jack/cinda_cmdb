# -*- coding: utf-8 -*-
from openerp import fields
from openerp import models


class base_class(models.Model):
    _name = "cmdb.base_class"
    _rec_name = 'class_name'

    class_number = fields.Char(string="总类编号")
    class_name = fields.Char(string="总类名称")
    comment = fields.Char(string="备注")


class base_type(models.Model):
    _name = "cmdb.base_type"
    _rec_name = 'type_name'

    type_number = fields.Char(string="细类编号")
    type_name = fields.Char(string="细类名称")
    class_id = fields.Many2one("cmdb.base_class", string="所属父类")
    comment = fields.Char(string="备注")


class base_data(models.Model):
    _name = "cmdb.base_data"

    base_data_id = fields.Char(string="基础数据ID")
    value = fields.Char(string="值")
    pare_id = fields.Char(string="父id")
    pare_lnk_mod = fields.Integer(string="父节点连接类型")
    pare_val = fields.Char(string="父值")
    last_id = fields.Integer(string="前节点id")
    last_lnk_mod = fields.Integer(string="前节点连接类型")
    last_val = fields.Char(string="前节点值")
    next_id = fields.Integer(string="后节点id")
    next_lnk_mod = fields.Integer(string="后节点连接类型")
    next_val = fields.Char(string="后节点值")
    chld_id = fields.Integer(string="子节点id")
    chld_lnk_mod = fields.Integer(string="子节点连接类型")
    chld_val = fields.Char(string="子节点值")
    fld1 = fields.Char(string="栏位1")
    fld2 = fields.Char(string="栏位2")
    fld3 = fields.Char(string="栏位3")
    fld4 = fields.Char(string="栏位4")
    fld5 = fields.Char(string="栏位5")
    fld6 = fields.Char(string="栏位6")
    fld7 = fields.Char(string="栏位7")
    fld8 = fields.Char(string="栏位8")
    fld9 = fields.Char(string="栏位9")
    fld10 = fields.Char(string="栏位10")
    fld11 = fields.Char(string="栏位11")
    fld12 = fields.Char(string="栏位12")
    fld13 = fields.Char(string="栏位13")
    fld14 = fields.Char(string="栏位14")
    fld15 = fields.Char(string="栏位15")
    fld16 = fields.Char(string="栏位16")
    fld17 = fields.Char(string="栏位17")
    fld18 = fields.Char(string="栏位18")
    fld19 = fields.Char(string="栏位19")
    fld20 = fields.Char(string="栏位20")
    comment = fields.Char(string="备注")
    last_upd = fields.Datetime(default=fields.datetime.now(), require=True)


class device(models.Model):
    _name = "cmdb.device"
    _rec_name = "sn"

    device_id = fields.Char(string="硬件ID")
    lab_id = fields.Many2one("cmdb.base_type", string='机房', domain=[('class_id', 'ilike', "机房")])
    cab = fields.Many2one("cmdb.cabinet", string="机柜")
    pos_seq = fields.Integer(string="位置序号")
    u_pos = fields.Many2one("cmdb.base_type", string="位置U", domain=[('class_id', 'ilike', "位置代号")])
    u_space = fields.Integer(string="占位U")
    env_id = fields.Many2one("cmdb.base_type", string="环境", domain=[('class_id', 'ilike', "环境")])
    use_mode = fields.Selection([('using', '使用中'), ('un_use', '未使用'),], default="", Require="False")
    dev_start = fields.Selection([('start up', '开机'), ('shut down', '关机'),], default="", Require="False")
    type_id = fields.Many2one("cmdb.base_type", string="设备类型", domain=[('class_id', 'ilike', "设备类型")])
    brand_id = fields.Many2one("cmdb.base_type", string="品牌", domain=[('class_id', 'ilike', "设备品牌")])
    product_name = fields.Char(string="产品型号")
    host_name = fields.Char(string="设备命名")
    model = fields.Char(string="Model")
    asset_num_old = fields.Char(string="旧资产编号")
    asset_num = fields.Char(string="资产编号")
    sn = fields.Char(string="序列号")
    purpose = fields.Char(string="用途")
    accept_date = fields.Char(string="初验日期")
    reject_date = fields.Char(string="过保日期")
    owner_id = fields.Many2one("cmdb.base_type", string="资产所有人", domain=[('class_id', 'ilike', "资产所有者")])
    user = fields.Many2one("cmdb.member_list", string="使用人")
    srve_prvd = fields.Many2one("cmdb.vendor_list", string="服务商")
    admin = fields.Char(string="管理人")
    comment = fields.Char(string="备注")
    last_upd = fields.Datetime(default=fields.datetime.now(), require=True)

    def create(self, cr, uid, vals, context=None):
        vals['device_id'] = self.pool.get('ir.sequence').get(cr, uid, 'cmdb.device')
        return super(device, self).create(cr, uid, vals, context=context)


class server(models.Model):
    _name = "cmdb.server"

    server_id = fields.Char(string="服务器id")
    # app_sys_id = fields.Integer(string="所属系统id")
    app_sys = fields.Char(string="所属系统")
    buss_ip_addr = fields.Char(string="业务网IP地址")
    stor_ip_addr = fields.Char(string="存储网IP地址")
    bck_ip_addr = fields.Char(string="备份网IP地址")
    mng_ip_addr = fields.Char(string="管理网IP地址")
    admin_ip = fields.Char(string="管理口IP")
    admin_info = fields.Char(string="管理口信息点")
    os_id = fields.Char(string="底层操作系统id")
    os = fields.Char(string="底层操作系统")
    cpu_num = fields.Char(string="CPU数量")
    cpu_spec = fields.Char(string="CPU规格")
    mem_size = fields.Char(string="内存容量")
    mem_spec = fields.Char(string="内存规格")
    disk_size = fields.Char(string="硬盘容量(裸容量)")
    disk_spec = fields.Char(string="硬盘规格")
    ext_st_size = fields.Char(string="外接存储容量")
    hba_config = fields.Char(string="HBA卡配置")
    hba_used = fields.Char(string="HBA卡已用情况")
    g_netcard_config = fields.Char(string="千兆网卡配置")
    g_netcard_used = fields.Char(string="千兆网卡已用情况")
    t_netcard_config = fields.Char(string="万兆网卡配置")
    t_netcard_used = fields.Char(string="万兆网卡已用情况")
    netcard_band = fields.Char(string="网卡绑定")
    exten_mod = fields.Char(string="扩展模块")
    vir_mark = fields.Char(string="虚拟化标志")
    comment1 = fields.Char(string="备注1")
    comment2 = fields.Char(string="备注2")
    last_upd = fields.Datetime(default=fields.datetime.now(), require=True)
    dev_id = fields.Many2one("cmdb.device", string="设备资产id")
    san_wwn = fields.Char(string="san网络wwn号")
    ha_mode = fields.Char(string="主备状态")


class net_dev(models.Model):
    _name = "cmdb.net_dev"

    net_dev_id = fields.Char(string="网络设备id")
    area_id = fields.Integer(string="区域id")
    area = fields.Char(string="区域")
    version = fields.Char(string="软件版本")
    admin_ip = fields.Char(string="管理IP")
    account = fields.Char(string="账号")
    root_acc = fields.Char(string="根用户")
    chg_acc = fields.Char(string="变更用户")
    mon_acc = fields.Char(string="监控用户")
    ha_mode = fields.Char(string="主备状态")
    fld1 = fields.Char(string="栏位1")
    fld2 = fields.Char(string="栏位2")
    fld3 = fields.Char(string="栏位3")
    fld4 = fields.Char(string="栏位4")
    fld5 = fields.Char(string="栏位5")
    fld6 = fields.Char(string="栏位6")
    fld7 = fields.Char(string="栏位7")
    comment1 = fields.Char(string="备注1")
    comment2 = fields.Char(string="备注2")
    last_upd = fields.Datetime(default=fields.datetime.now(), require=True)
    dev_id = fields.Integer(string="设备资产id")


class board(models.Model):
    _name = "cmdb.board"

    board_id = fields.Char(string="板卡id")
    area_id = fields.Integer(string="区域id")
    area = fields.Char(string="区域")
    dev_id = fields.Integer(string="设备资产id")
    net_dev_id = fields.Integer(string="网络设备id")
    srv_dev_id = fields.Integer(string="服务器设备id")
    card_type = fields.Char(string="板卡类型")
    card_sn = fields.Char(string="板卡序列号")
    slot = fields.Char(string="槽位")
    fld1 = fields.Char(string="栏位1")
    fld2 = fields.Char(string="栏位2")
    fld3 = fields.Char(string="栏位3")
    fld4 = fields.Char(string="栏位4")
    fld5 = fields.Char(string="栏位5")
    fld6 = fields.Char(string="栏位6")
    fld7 = fields.Char(string="栏位7")
    comment1 = fields.Char(string="备注")
    comment2 = fields.Char(string="备注2")
    last_upd = fields.Datetime(default=fields.datetime.now(), require=True)


class st_dev(models.Model):
    _name = "cmdb.st_dev"

    st_dev_id = fields.Char(string="存储id")
    cage_num = fields.Integer(string="笼子数")
    disk_num = fields.Integer(string="磁盘数")
    disk_size = fields.Char(string="磁盘裸容量")
    total_size = fields.Char(string="总容量")
    used_size = fields.Char(string="使用容量")
    free_size = fields.Char(string="剩余容量")
    port_num = fields.Integer(string="有效口总数")
    used_port_num = fields.Integer(string="使用数(连线的)")
    free_port_num = fields.Integer(string="剩余端口数")
    eight_g_mod_num = fields.Integer(string="8G模块数")
    used_8g_mod_num = fields.Integer(string="已经使用的8G模块数")
    free_8g_mod_num = fields.Integer(string="空余的8G模块数")
    four_g_mod_num = fields.Integer(string="4G模块数")
    used_4g_mod_num = fields.Integer(string="已经使用的4G模块数")
    free_4g_mod_num = fields.Integer(string="空余的4G模块数量")
    comment = fields.Integer(string="备注")
    fld1 = fields.Char(string="栏位1")
    fld2 = fields.Char(string="栏位2")
    fld3 = fields.Char(string="栏位3")
    fld4 = fields.Char(string="栏位4")
    fld5 = fields.Char(string="栏位5")
    fld6 = fields.Char(string="栏位6")
    last_upd = fields.Datetime(default=fields.datetime.now(), require=True)
    dev_id = fields.Integer(string="设备资产id")


class srv_room_dev(models.Model):
    _name = "cmdb.srv_room_dev"

    srv_room_dev_id = fields.Char(string="机房设备id")
    asset_type = fields.Char(string="资产大类")
    num = fields.Integer(string="数量")
    start_date = fields.Date(string="启用日期")
    elec_power = fields.Integer(string="总功率")
    ampere = fields.Integer(string="电流")
    comment = fields.Char(string="备注")
    fld1 = fields.Char(string="栏位1")
    fld2 = fields.Char(string="栏位2")
    fld3 = fields.Char(string="栏位3")
    fld4 = fields.Char(string="栏位4")
    fld5 = fields.Char(string="栏位5")
    fld6 = fields.Char(string="栏位6")
    fld7 = fields.Char(string="栏位7")
    fld8 = fields.Char(string="栏位8")
    fld9 = fields.Char(string="栏位9")
    fld10 = fields.Char(string="栏位10")
    fld11 = fields.Char(string="栏位11")
    fld12 = fields.Char(string="栏位12")
    last_upd = fields.Datetime(default=fields.datetime.now(), require=True)
    dev_id = fields.Integer(string="设备资产id")


class san_port(models.Model):
    _name = "cmdb.san_port"

    san_port_id = fields.Char(string="SAN端口id")
    dev_id = fields.Integer(string="设备资产id")
    type_id = fields.Integer(string="设备类型")
    port = fields.Char(string="端口号")
    module = fields.Char(string="模块")
    port = fields.Char(string="本端端口号")
    wwn = fields.Char(string="本端口的WWN")
    end_on_dev_id = fields.Integer(string="对端设备id")
    end_port_id = fields.Integer(string="对端端口ID")
    end_on_port = fields.Char(string="对端的端口号")
    end_on_wwn = fields.Char(string="对端的WWN")
    speed = fields.Char(string="速率")
    protocl = fields.Char(string="使用协议")
    device_code = fields.Char(string="设备编号")
    fc_card_name = fields.Char(string="光纤卡名")
    slot = fields.Char(string="槽位")
    alias = fields.Char(string="别名")
    captain = fields.Char(string="说明")
    comment = fields.Char(string="备注")
    fld1 = fields.Char(string="栏位1")
    fld2 = fields.Char(string="栏位2")
    fld3 = fields.Char(string="栏位3")
    fld4 = fields.Char(string="栏位4")
    fld5 = fields.Char(string="栏位5")
    fld6 = fields.Char(string="栏位6")
    fld7 = fields.Char(string="栏位7")
    last_upd = fields.Datetime(default=fields.datetime.now(), require=True)


class ip_port(models.Model):
    _name = "cmdb.ip_port"

    ip_port_id = fields.Char(string="IP端口ID")
    dev_id = fields.Integer(string="设备id")
    net_dev_id = fields.Integer(string="网络设备id")
    card_id = fields.Integer(string="板卡id")
    port = fields.Char(string="本端物理端口号")
    port_num = fields.Char(string="本端端口名")
    port_mac = fields.Char(string="本端MAC")
    port_ip = fields.Char(string="本端IP地址")
    port_type = fields.Integer(string="本端端口类型")
    end_on_dev_id = fields.Integer(string="对端设备id")
    end_on_card_id = fields.Integer(string="对端板卡id")
    end_on_port = fields.Char(string="对端物理端口号")
    end_on_nam = fields.Char(string="对端端口名")
    end_on_port_mac = fields.Char(string="对端MAC")
    end_on_port_ip = fields.Char(string="对端ip地址")
    end_on_port_type = fields.Integer(string="对端端口类型")
    port_status = fields.Char(string="端口状态")
    port_speed = fields.Char(string="端口速率")
    port_info = fields.Char(string="端口描述")
    mod_type = fields.Char(string="模块类型")
    mod_sn = fields.Char(string="模块序列号")
    fld1 = fields.Char(string="栏位1")
    fld2 = fields.Char(string="栏位2")
    fld3 = fields.Char(string="栏位3")
    fld4 = fields.Char(string="栏位4")
    fld5 = fields.Char(string="栏位5")
    fld6 = fields.Char(string="栏位6")
    fld7 = fields.Char(string="栏位7")
    last_upd = fields.Datetime(default=fields.datetime.now(), require=True)


class cabinet(models.Model):
    _name = "cmdb.cabinet"
    _rec_name = "cab_num"

    cabinet_id = fields.Char(string="机柜id")
    lab_id = fields.Char(string="机房id", require=True)
    cab_num = fields.Char(string="机柜号", require=True)
    lab = fields.Many2one("cmdb.base_type", string="机房")
    pdu_num = fields.Integer(string="PDU数目")
    elec_power = fields.Integer(string="电源功率")
    ampere = fields.Integer(string="电流")
    u_num = fields.Integer(string="U位数目")
    purpose = fields.Char(string="用途")
    fld1 = fields.Char(string="栏位1")
    fld2 = fields.Char(string="栏位2")
    fld3 = fields.Char(string="栏位3")
    fld4 = fields.Char(string="栏位4")
    fld5 = fields.Char(string="栏位5")
    fld6 = fields.Char(string="栏位6")
    fld7 = fields.Char(string="栏位7")
    fld8 = fields.Char(string="栏位8")
    fld9 = fields.Char(string="栏位9")
    fld10 = fields.Char(string="栏位10")
    comment = fields.Char(string="备注")
    last_upd = fields.Datetime(default=fields.datetime.now(), require=True)


class soft(models.Model):
    _name = "cmdb.soft"

    soft_id = fields.Char(string="软件总id")
    total_class = fields.Char(string="总类别", require=True)
    subclass = fields.Char(string="明细类别", require=True)
    soft_code = fields.Char(string="软件编号", require=True)
    soft_name = fields.Char(string="全称")
    purpose = fields.Char(string="用途")
    license_type = fields.Char(string="许可类型")
    license_company = fields.Char(string="许可单位")
    num = fields.Char(string="数量")
    developer = fields.Char(string="开发商")
    status = fields.Char(string="状态")
    media_type = fields.Char(string="介质类型")
    reject_date = fields.Char(string="支持到期类型")
    contact_info = fields.Char(string="支持联系方式")
    license_pos = fields.Char(string="许可证位置")
    fld1 = fields.Char(string="栏位1")
    fld2 = fields.Char(string="栏位2")
    fld3 = fields.Char(string="栏位3")
    fld4 = fields.Char(string="栏位4")
    fld5 = fields.Char(string="栏位5")
    fld6 = fields.Char(string="栏位6")
    fld7 = fields.Char(string="栏位7")
    fld8 = fields.Char(string="栏位8")
    fld9 = fields.Char(string="栏位9")
    fld10 = fields.Char(string="栏位10")
    comment = fields.Char(string="备注")
    last_upd = fields.Datetime(default=fields.datetime.now(), require=True)


class soft_detail(models.Model):
    _name = "cmdb.soft_detail"

    soft_detail_id = fields.Char(string="软件明细id")
    detail_code = fields.Char(string="明细编号")
    detail_name = fields.Char(string="细项名称")
    version = fields.Char(string="版本号")
    num = fields.Char(string="购买数量")
    auth_info = fields.Char(string="授权信息")
    buy_date = fields.Char(string="购买时间")
    over_date = fields.Char(string="服务截止时间")
    vendor = fields.Char(string="供应商")
    buyer = fields.Char(string="购买单位")
    owner = fields.Char(string="资产所有人")
    user = fields.Char(string="使用人")
    media_path = fields.Char(string="介质路径")
    license_key = fields.Char(string="许可密钥")
    license_path = fields.Char(string="许可保存路径")
    fld1 = fields.Char(string="栏位1")
    fld2 = fields.Char(string="栏位2")
    fld3 = fields.Char(string="栏位3")
    fld4 = fields.Char(string="栏位4")
    fld5 = fields.Char(string="栏位5")
    fld6 = fields.Char(string="栏位6")
    fld7 = fields.Char(string="栏位7")
    fld8 = fields.Char(string="栏位8")
    fld9 = fields.Char(string="栏位9")
    fld10 = fields.Char(string="栏位10")
    comment = fields.Char(string="备注")
    last_upd = fields.Datetime(default=fields.datetime.now(), require=True)


class vendor_list(models.Model):
    _name = "cmdb.vendor_list"
    _rec_name = "vendor"

    vendor_list_id = fields.Char(string="服务商ID")
    vendor = fields.Char(string="人员名称", require=True)
    attr = fields.Char(string="性质")
    address = fields.Char(string="地址")
    contact = fields.Char(string="联系人")
    position = fields.Char(string="职位")
    fixed_phone = fields.Char(string="电话")
    mobile_phone = fields.Char(string="手机")
    mail = fields.Char(string="邮件")
    comment = fields.Char(string="备注")
    last_upd = fields.Datetime(default=fields.datetime.now(), require=True)


class member_list(models.Model):
    _name = "cmdb.member_list"
    _rec_name = "name"

    member_list_id = fields.Char(string="人员表ID")
    name = fields.Char(string="名称", require=True)
    attr = fields.Char(string="性质")
    address = fields.Char(string="地址")
    position = fields.Char(string="职位")
    fixed_phone = fields.Char(string="电话")
    mobile_phone = fields.Char(string="手机")
    mail = fields.Char(string="邮件")
    comment = fields.Char(string="备注")
    last_upd = fields.Datetime(default=fields.datetime.now(), require=True)


class chg_log(models.Model):
    _name = "cmdb.chg_log"

    chg_log_id = fields.Char(string="变更记录id")
    exe_date = fields.Date(string="日期")
    executor = fields.Char(string="实施人", require=True)
    chg_fld = fields.Char(string="变更栏位")
    action = fields.Char(string="动作", require=True)


class net_config(models.Model):
    _name = "cmdb.net_config"

    net_config_id = fields.Char(string="网络配置管理id")
    logic_area = fields.Char(string="逻辑区域")
    admin_ip = fields.Char(string="管理IP")
    version = fields.Char(string="软件版本")
    license_date = fields.Date(string="许可证日期")
    port_num = fields.Integer(string="端口数量")
    port_info = fields.Char(string="端口信息")
    vlan_info = fields.Char(string="VLAN信息")
    fw_policy1 = fields.Char(string="防火墙策略1")
    fw_policy2 = fields.Char(string="防火墙策略2")
    mail_gw_policy = fields.Char(string="邮件网关策略")


class st_zone_lun(models.Model):
    _name = "cmdb.st_zone_lun"

    st_zone_lun_id = fields.Char(string="存储zone_lun划分id")
    zone_lun_id = fields.Char(string="ZONE_LUN_ID")
    lun_id = fields.Char(string="lun号")
    ioport = fields.Char(string="ioport")
    total_size = fields.Char(string="总容量")
    used_size = fields.Char(string="使用容量")
    free_size = fields.Char(string="剩余容量")
    host_name = fields.Char(string="使用的主机")
    system = fields.Char(string="业务系统")
    raid_type = fields.Char(string="RAID类型")
    volumes_name = fields.Char(string="volumes_name")
    aggregate = fields.Char(string="aggregata")
    ip_addr = fields.Char(string="IP地址")
    config_info = fields.Char(string="配置信息")
    comment = fields.Char(string="备注")


class vlan(models.Model):
    _name = "cmdb.vlan"

    vlan_id_id = fields.Char(string="VLAN表ID")
    vlan_id = fields.Char(string="VLAN号")
    vlan_name = fields.Char(string="VLAN名称")
    vlan_segment = fields.Char(string="VLAN网段")
    comment = fields.Char(string="备注")


class fw_policy1(models.Model):
    _name = "cmdb.fw_policy1"

    fw_policy1_id = fields.Char(string="防火墙策略1id")
    fw_name = fields.Char(string="防火墙名称")
    s_addrname = fields.Char(string="源地址命名")
    s_ip = fields.Char(string="源地址")
    d_addrname = fields.Char(string="目的地址命名")
    d_ip = fields.Char(string="目的地址")
    service_name = fields.Char(string="服务命名")
    service_port = fields.Char(string="服务端口")
    policy_date = fields.Date(string="策略时间")


class fw_policy2(models.Model): 
    _name = "cmdb.fw_policy2"

    fw_policy2_id = fields.Char(string="防火墙策略2id")
    fw_name = fields.Char(string="防火墙名称")
    switch_mode = fields.Char(string="转换模式")
    s_addrname = fields.Char(string="源地址命名")
    s_ip = fields.Char(string="源地址")
    d_addrname = fields.Char(string="目的地址命名")
    d_ip = fields.Char(string="目的地址")
    switch_addrname = fields.Char(string="转换后地址命名")
    switch_ip = fields.Char(string="转换后地址")
    service_name = fields.Char(string="服务命令")
    service = fields.Char(string="服务")


class spam_policy(models.Model):
    _name = "cmdb.spam_policy"

    spam_policy_id = fields.Char(stirng="SPAM策略id")
    industry = fields.Char(string="行业")
    company_name = fields.Char(string="公司名称")
    domain_name = fields.Char(string="域名")
    mx_name = fields.Char(string="mx名称")
    ip_addr = fields.Char(string="IP")
    desc = fields.Char(string="描述")
    comment = fields.Char(string="备注")


class vm(models.Model):
    _name = "cmdb.vm"

    vm_id = fields.Char(string="虚拟机id")
    environment = fields.Char(string="环境")
    cluster = fields.Char(string="集群")
    resource_pool = fields.Char(string="资源地")
    exi_ip = fields.Char(string="主机")
    vm_hostname = fields.Char(string="虚机名称")
    status = fields.Char(string="状况")
    cpu = fields.Char(string="CPU")
    mem = fields.Char(string="内存")
    disk = fields.Char(string="置备的空间")
    os = fields.Char(string="客户机操作系统")
    vm_ip = fields.Char(string="虚拟机IP地址")
    purpose = fields.Char(string="用途")
    system_module = fields.Char(string="系统模块名称")
    app_user = fields.Char(string="应用联系人")
    deliver_date = fields.Date(string="交付日期")
    back_date = fields.Date(string="计划归还日期")


class account(models.Model):
    _name = "cmdb.account"

    account_id = fields.Char(string="账户id")
    dev_id = fields.Integer(string="设备id",  require=True)
    soft_id = fields.Integer(string="软件id")
    acc_nam = fields.Char(string="账户名称",  require=True)
    encr_pasw = fields.Char(string="加密密码",  require=True)
    use_purp = fields.Char(string="使用目的",  require=True)
    use_mode = fields.Char(string="使用类型",  require=True)
    authority = fields.Char(string="账户权限",  require=True)
    owner_id = fields.Integer(string="账户负责人",  require=True)
    auth_owner = fields.Integer(string="授权负责人",  require=True)
    crt_date = fields.Char(string="创建日期")
    crt_pers = fields.Integer(string="创建人")
    crt_appr_pers = fields.Integer(string="创建批准人")
    crt_chg_num = fields.Char(string="创建的变更号")
    curr_user = fields.Integer(string="当前使用人")
    use_appr_pers = fields.Integer(string="当前使用授权人")
    appr_date = fields.Datetime(string="当前授权日期")
    last_recovery = fields.Datetime(string="上次回收日期")
    comment1 = fields.Char(string="备注1")
    comment2 = fields.Char(string="备注2")
    last_upd = fields.Datetime(default=fields.datetime.now(), require=True)


class auth_log(models.Model):
    _name = "cmdb.auth_log"

    auth_log_id = fields.Char(string="授权记录id")
    exe_date = fields.Char(string="",require=True)
    executor = fields.Integer(string="",require=True)
    chg_num = fields.Char(string="")
    action = fields.Char(string="",require=True)
    per_user = fields.Integer(string="")
    aft_user = fields.Integer(string="")
    per_owner = fields.Integer(string="")
    aft_owner = fields.Integer(string="")
    comment1 = fields.Char(string="")
    comment2 = fields.Char(string="")
    last_upd = fields.Datetime(default=fields.datetime.now(), require=True)


# u位表
class position_u(models.Model):
    _name = "cmdb.position_u"

    name = fields.Char(string="名称")
    status = fields.Boolean(string="状态", default=False)
    cabinet_id = fields.Many2one("cmdb.cabinet", string="所在机柜", required="True")
