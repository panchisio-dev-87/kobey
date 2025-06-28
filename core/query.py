

def query_custom_no_result():
    return [
        {
            "query":"SELECT TOP 2 ROTCODE FROM GENERAL where ROTCODE='0800'",
            "name":"GENERAL"
        },
        {
            "query":"SELECT TOP 2 ROTCODE, DMDCODE FROM DEMAND where cuscode='555'",
            "name":"PEDIDOS"
        }
    ]


def query_stock_dz():
    return [
        {
            "query":f"declare @preventa date, \
                    @despacho date, \
                    @horainicio datetime, \
                    @horafin datetime, \
                    @customerxss int, \
                    @cusdelete int, \
                    @customerroute int, \
                    @cusst int, \
                    @customerstatus int, \
                    @customerroute1 int, \
                    @product int, \
                    @catalog int, \
                    @cataa int, \
                    @catai int, \
                    @promotion int, \
                    @promotiond int, \
                    @promotiondp int, \
                    @generico int, \
                    @cpa int, \
                    @pa int \
                    select @preventa= (select  top(1) aptTransactionDate from dbo.AREAPRODUCT WHERE areCode='A001') \
                    select @despacho= (select  top(1) aptServerLastUpdate from dbo.AREAPRODUCT WHERE areCode='A001') \
                    select @horainicio=(SELECT max(Trndate) FROM[TRANSACTION] WHERE TRNSCRIPTS LIKE'%CALCULATE%') \
                    select  @horafin=(SELECT max(trnLastDate) FROM[TRANSACTION] WHERE TRNSCRIPTS LIKE'%CALCULATE%') \
                    select @customerxss= (select count(*) from customer) \
                    select @cusdelete=(select count(*) from customer where _Deleted='0' ) \
                    select @customerroute=(select count(distinct cuscode) from customerroute where ctrvisittoday='1' and rotcode not like'%t%') \
                    select @customerstatus=(select count(*) from customerstatus WHERE CUSCODE IN (SELECT CUSCODE FROM CUSTOMERROUTE)) \
                    select @cusst=(select count(*) from customerstatus where cuscode in(select cusCode from customerroute where ctrVisitToday='1' and rotcode not like'%t%')) \
                    select @customerroute1=(select count(distinct cuscode) from customerroute) \
                    select @product=(select count(*) from product where _Deleted='0') \
                    select @catalog=(select count(*) from CatalogDetail where catCode like'%NacDZ%') \
                    select @cataa=(select count(*) from Catalog where catActive='1') \
                    select @catai=(select count(*) from Catalog where _deleted='1') \
                    select @promotion=(select count(*) from promotion) \
                    select @promotiond=(select count(*) from promotiondetail) \
                    select @promotiondp=(select count(*) from promotiondetailproduct) \
                    select @generico=(select count(*) from customerstatus where cusCode like'%3030000074%') \
                    select @cpa=(select count(*) from customerpartner) \
                    select @pa=(select count(*) from partner) \
                    select DB_NAME() as DZ_Regional, @preventa as PREVENTA, @despacho as DESPACHO, \
                    dateadd(hh,-1,@horainicio) as ECInicioStock, dateadd(hh,-1,@horafin) as ECFinStock, @customerxss as CUSTOMER_XSS, @cusdelete as CUSTOMER_DELETE_0, \
                    @customerroute1 as CUSROUT_TOTAL, @customerroute as CUSROUTE_VISIT_TODAY, @cusst as CUSSTATUS_VISIT_TODAY, \
                    @customerstatus as CUSSTATUS_TOTAL, @product as PRODUCT, @catalog as CATALOGO, @cataa as CA, @catai as CI, \
                    @promotion as PROMOTION, @promotiond as PROMOTIOND, @promotiondp as PROMOTIONDP, @generico as GENERICO, @cpa CUSPAR, @pa PAR",
            "name":"STOCK_DZ_Y_TABLAS"
        }
    ]


def query_matriz_gdd_pollo_blanco():
    return [
        {
            "query":f"Select Top 10 DB_NAME() as DZ_Regional, didName, didSince,didUntil,didActualDiscount,atpCode  From discountDetail Where didName like'MAT%' and atpcode='6' order by didUntil desc",
            "name":"MATRIZ_GDD_POLLO_BLANCO"
        }
    ]

def query_matriz_gdd_pollo_criollo():
    return [
        {
            "query":f"Select Top 10 DB_NAME() as DZ_Regional, count(*) RESULT  From DiscountDetailProduct Where cl4Code in ('IDGDD002','IDDG003')",
            "name":"MATRIZ_GDD_POLLO_CRIOLLO"
        }
    ]

def query_general_dia():
    return [
        {
            "query":f"Select Top 100 DB_NAME() as DZ_Regional, gnlDate, gnlStatus, count(*) as Cantidad From General Where rotCode in (Select rotCode From route Where rotInactive= 0 and _deleted= 0) Group By gnlDate, gnlStatus Order By gnlDate Desc",
            "name":"GENERAL_DIA"
        }
    ]


def query_solo_stock_dz_dia():
    return [
        {
            "query":f"declare @preventa datetime, @despacho datetime, @horainicio datetime, @horafin datetime \
                    select @preventa= (select max(aptTransactionDate) from dbo.AREAPRODUCT) \
                    select @despacho= (select max(aptServerLastUpdate) from dbo.AREAPRODUCT) \
                    select @horainicio=(SELECT max(dateadd(hh,-1,Trndate)) FROM[TRANSACTION] WHERE TRNSCRIPTS LIKE'%CALCULATE%') \
                    select  @horafin=(SELECT max(dateadd(hh,-1,trnLastDate)) FROM[TRANSACTION] WHERE TRNSCRIPTS LIKE'%CALCULATE%') \
                    select top 1 DB_NAME() as DZ_Regional, @preventa as STOCK_PREVENTA, @despacho as STOCK_DESPACHO, \
                    CASE \
                            WHEN CAST(@preventa AS DATE) = CAST(GETDATE() AS DATE) THEN 'si' \
                            ELSE 'no' \
                        END AS stock_fecha_actual, \
                    @horainicio as HoraECUInicioStock ,@horafin as HoraECUFinStock, \
                    CASE \
                            WHEN \
                                (CAST(@horainicio AS DATE) = CAST(GETDATE() AS DATE) AND CAST(@horainicio AS TIME) < '02:00:00') \
                                OR \
                                (CAST(@horainicio AS DATE) = DATEADD(DAY, -1, CAST(GETDATE() AS DATE)) AND CAST(@horainicio AS TIME) >= '17:00:00') \
                            THEN 'si' \
                            ELSE 'no' \
                    END AS stock_en_rango",
            "name":"SOLO_STOCK_DZ_DIA"
        }
    ]



def query_rev_day():
    return [
        {
            "query":"declare @preventa date, \
                    @despacho date, \
                    @horainicio datetime, \
                    @horafin datetime, \
                    @customerxss int, \
                    @cusdelete int, \
                    @customerroute int, \
                    @cusst int, \
                    @customerstatus int, \
                    @customerroute1 int, \
                    @product int, \
                    @catalog int, \
                    @cataa int, \
                    @catai int, \
                    @promotion int, \
                    @promotiond int, \
                    @promotiondp int, \
                    @generico int, \
                    @cpa int, \
                    @pa int \
                    select @preventa= (select  top(1) aptTransactionDate from dbo.AREAPRODUCT WHERE areCode='A001') \
                    select @despacho= (select  top(1) aptServerLastUpdate from dbo.AREAPRODUCT WHERE areCode='A001') \
                    select @horainicio=(SELECT max(Trndate) FROM[TRANSACTION] WHERE TRNSCRIPTS LIKE'%CALCULATE%') \
                    select  @horafin=(SELECT max(trnLastDate) FROM[TRANSACTION] WHERE TRNSCRIPTS LIKE'%CALCULATE%') \
                    select @customerxss= (select count(*) from customer) \
                    select @cusdelete=(select count(*) from customer where _Deleted='0' ) \
                    select @customerroute=(select count(distinct cuscode) from customerroute where ctrvisittoday='1' and rotcode not like'%t%') \
                    select @customerstatus=(select count(*) from customerstatus WHERE CUSCODE IN (SELECT CUSCODE FROM CUSTOMERROUTE)) \
                    select @cusst=(select count(*) from customerstatus where cuscode in(select cusCode from customerroute where ctrVisitToday='1' and rotcode not like'%t%')) \
                    select @customerroute1=(select count(distinct cuscode) from customerroute) \
                    select @product=(select count(*) from product where _Deleted='0') \
                    select @catalog=(select count(*) from CatalogDetail where catCode like'%NacDZ%') \
                    select @cataa=(select count(*) from Catalog where catActive='1') \
                    select @catai=(select count(*) from Catalog where _deleted='1') \
                    select @promotion=(select count(*) from promotion) \
                    select @promotiond=(select count(*) from promotiondetail) \
                    select @promotiondp=(select count(*) from promotiondetailproduct) \
                    select @generico=(select count(*) from customerstatus where cusCode like'%3030000074%') \
                    select @cpa=(select count(*) from customerpartner) \
                    select @pa=(select count(*) from partner) \
                    select DB_NAME() as DZ_Regional, @preventa as PREVENTA, @despacho as DESPACHO, \
                    dateadd(hh,-1,@horainicio) as ECInicioStock, dateadd(hh,-1,@horafin) as ECFinStock, @customerxss as CUSTOMER_XSS, @cusdelete as CUSTOMER_DELETE_0, \
                    @customerroute1 as CUSROUT_TOTAL, @customerroute as CUSROUTE_VISIT_TODAY, @cusst as CUSSTATUS_VISIT_TODAY, \
                    @customerstatus as CUSSTATUS_TOTAL, @product as PRODUCT, @catalog as CATALOGO, @cataa as CA, @catai as CI, \
                    @promotion as PROMOTION, @promotiond as PROMOTIOND, @promotiondp as PROMOTIONDP, @generico as GENERICO, @cpa CUSPAR, @pa PAR",
            "name":"STOCK"
        },
        {
            "query":"Select Top 100 gnlDate, gnlStatus, count(*) as Cantidad From General Where rotCode in (Select rotCode From route Where rotInactive= 0 and _deleted= 0) Group By gnlDate, gnlStatus Order By gnlDate Desc",
            "name":"GENERAL"
        },
        {
            "query":"Select Top 10 didName, didSince,didUntil,didActualDiscount,atpCode  From discountDetail Where didName like'MAT%' and atpcode='6' order by didUntil desc",
            "name":"POLLO_BLANCO"
        },
        {
            "query":"Select Top 10 count(*) RESULT  From DiscountDetailProduct Where cl4Code in ('IDGDD002','IDDG003')",
            "name":"POLLO_CRIOLLO"
        }
    ]

def query_GDD_report(fecha):
    return [
        {
            "query":f"""declare @inicio VARCHAR(255), @fin VARCHAR(255) \
                    set @inicio='{fecha} 00:00:00.000'set @fin='{fecha} 23:59:00.000' \
                    Select Top 1000000 LTRIM(RTRIM(Emp_Codigo)) AS Emp_Codigo, \
                    LTRIM(RTRIM(Id_Negociacion)) AS Id_Negociacion, \
                    LTRIM(RTRIM(Tipo)) AS Tipo, \
                    LTRIM(RTRIM(Codigo_Cliente)) AS Codigo_Cliente, \
                    LTRIM(RTRIM(Dia_Negociacion)) AS Dia_Negociacion, \
                    LTRIM(RTRIM(Mes_Negociacion)) AS Mes_Negociacion, \
                    LTRIM(RTRIM(Anio_Negociacion)) AS Anio_Negociacion, \
                    LTRIM(RTRIM(Cod_Vendedor)) AS Cod_Vendedor, \
                    LTRIM(RTRIM(Descuento_Negociado)) AS Descuento_Negociado, \
                    LTRIM(RTRIM(Descuento_Realizado)) AS Descuento_Realizado, \
                    LTRIM(RTRIM(Descuento_Status)) AS Descuento_Status, \
                    LTRIM(RTRIM(Desc_Prev_Pedido)) AS Desc_Prev_Pedido, \
                    LTRIM(RTRIM(Descuento_Procesado_XSales)) AS Descuento_Procesado_XSales, \
                    LTRIM(RTRIM(Pedido_Realizado)) AS Pedido_Realizado \
                    From ( \
                    Select Top 1000000 \
                    Case When company.comName='Pronaca' Then'202' \
                    when company.comName='Almabi' Then'360' \
                    when company.comName='Alsodi' Then'314' \
                    when company.comName='Apronam' Then'162' \
                    when company.comName='Cenacop' Then'325' \
                    when company.comName='Disprolop' Then'431' \
                    when company.comName='Dimmia' Then'111' \
                    when company.comName='Disanahisa' Then'323' \
                    when company.comName='Discarnicos' Then'261' \
                    when company.comName='Dismag' Then'215' \
                    when company.comName='Disproalza' Then'247' \
                    when company.comName='Disprovalles' Then'210' \
                    when company.comName='Ecoal' Then'373' \
                    when company.comName='Granpir' Then'234' \
                    when company.comName='DISTMANA' Then'324' \
                    when company.comName='Judispro' Then'239' \
                    when company.comName='Madeli' Then'128' \
                    when company.comName='ProOriente' Then'140' \
                    when company.comName='Paul_Florencia' Then'168' \
                    when company.comName='Patricio_Cevallos' Then'254' \
                    when company.comName='Posso&Cueva' Then'253' \
                    when company.comName='Pronacnor' Then'303' \
                    when company.comName='Skandinar' Then'121' \
                    Else'517' end Emp_Codigo, \
                    Descu.didCode as Id_Negociacion, \
                    Descu.Tipo, \
                    Descu.Cliente as Codigo_Cliente, \
                    Day(Descu.Fecha) as Dia_Negociacion, \
                    Month(Descu.Fecha) as Mes_Negociacion, \
                    Year(Descu.Fecha) as Anio_Negociacion,  \
                    Ruta as Cod_Vendedor, Porcentaje as Descuento_Negociado, \
                    'Si' as Descuento_Realizado, Descu.Status as Descuento_Status, \
                    Case When Descu.Fecha< Ped2.Fecha Then'Si' Else'No' End as Desc_Prev_Pedido,Descu.Procesado as Descuento_Procesado_XSales, \
                    Case When len(Ped2.Fecha)> 4 Then'Si' Else'No' End as Pedido_Realizado From \
                    (Select  D.didCode,D.cusCode CLIENTE,Convert(Varchar,D.didSystemDate,25) FECHA, D.rotCode RUTA, \
                    Replace(I.dlpMinDiscount1,',','.') PORCENTAJE, \
                    Case When (Select A.ApvResponseDetail From Approval A Where A.apvCode=D.apvCode) Like'%RECHAZ%' Then'Rechazado' \
                    When (Select A.ApvResponseDetail From Approval A Where A.apvCode=D.apvCode) Like'%Respuesta"%:"SI%' ESCAPE':' Then'Aprobado' \
                    When (Select A.ApvResponseDetail From Approval A Where A.apvCode=D.apvCode) Like'%Respuesta"%:"No%' ESCAPE':' Then'Rechazado' \
                    When D.ApvCode IS NULL Then'Aprobado'When (Select A.ApvResponseDetail From Approval A Where A.apvCode=D.apvCode) Like'%Respuesta"%:null%' ESCAPE':' Then'Pendiente' \
                    When (Select A.ApvResponseDetail From Approval A Where A.apvCode=D.apvCode) Like'%Respuesta"%:"EXCEPCION%' ESCAPE':' Then'Pendiente' \
                    When (Select A.ApvResponseDetail From Approval A Where A.apvCode=D.apvCode) IS NULL Then'Pendiente'END As STATUS, \
                    Case When D.didProcess='1' Then'Si' Else'No' End As PROCESADO, \
                    case when apvcode is NULL then'RANGO' else'FUERA RANGO' end as TIPO From DiscountDetailUp D \
                    Inner Join DiscountDetailProductUp I On D.didCode=I.didCode \
                    Where D.didCanceled='0' And D.didProcess='1' And D.DidSystemDate Between @inicio And @fin And D.didCode Not In (Select T.didCode From demandTeamProductDiscount T \
                    Inner Join Demand P On T.dmdCode=P.dmdCode Where P.dmdCancelOrder='1' And P.dmdProcess IS NULL) ) Descu \
                    Left Join Company On 1=1 \
                    Left Join (Select  D.rotCode, D.cusCode,Max(D.dmdDate) as Fecha From Demand D Left Join DemandProduct DP On D.dmdCode= DP.dmdCode \
                    Where D.dmdDate Between @inicio And @fin And docCode='ped' and D.rotCode in (Select rotCode From route Where chaCode='V01') And D.dmdCancelOrder= 0 And DP.proCode in (Select proCode From product Where cl4Code='IDGDD001') Group By D.rotCode, D.cusCode) Ped2 On Descu.cliente= Ped2.cuscode and Descu.Ruta= Ped2.rotcode \
                    order by Descu.Ruta ) Todos """,
            "name":"GDD_REPORT"
        }
    ]

def query_rev_dia_directa():
    return [
        {
            "query":"declare @customerxss int, @cusdelete int, @customerroute int, @cusst int, @customerstatus int, @customerroute1 \
                    int,@product int, @catalog int, @promotion int, @promotiond int, @promotiondp int, @genericou int, @genericog \
                    int, @genericoc int, @genericom int,@PreventastockD1 date,@DespachostockD1 date,@horainicioD01 varchar(255), \
                    @horafinD01 varchar(255),@horainicioD02 varchar(255),@horafinD02 varchar(255),@horainicioD03 varchar(255),@horafinD03 varchar(255), \
                    @horainicioD04 varchar(255),@horafinD04 varchar(255),@PreventastockD3 date,@DespachostockD3 date, \
                    @horainicioD05 varchar(255),@horafinD05 varchar(255),@PreventastockD2 date,@DespachostockD2 date,@PreventastockD4 date, \
                    @DespachostockD4 date,@PreventastockD5 date, @DespachostockD5 date \
                    select @customerxss= (select count(*) from customer) \
                    select @cusdelete=(select count(*) from customer where _Deleted='0' ) \
                    select @customerroute=(select count(distinct cuscode) from customerroute where ctrvisittoday='1' and rotcode not like'%t%') \
                    select @customerroute1=(select count(distinct cuscode) from customerroute) \
                    select @cusst=(select count(*) from customerstatus where cuscode in(select cusCode from customerroute where ctrVisitToday='1' and rotcode not like'%t%')) \
                    select @customerstatus=(select count(*) from customerstatus WHERE CUSCODE IN (SELECT CUSCODE FROM CUSTOMERROUTE)) \
                    select @product=(select count(*) from product where _Deleted='0') \
                    Select @catalog=(select count(*) From CatalogDetail) \
                    select @promotion=(select count(*) from promotion) \
                    select @promotiond=(select count(*) from promotiondetail) \
                    select @promotiondp=(select count(*) from promotiondetailproduct) \
                    select @genericou=(select count(*) from customerstatus where cusCode like'%199998%') \
                    select @genericog=(select count(*) from customerstatus where cusCode like'%299998%') \
                    select @genericoc=(select count(*) from customerstatus where cusCode like'%488888%') \
                    select @genericom=(select count(*) from customerstatus where cusCode like'%588888%') \
                    select @horainicioD01=(SELECT max(Trndate) FROM[TRANSACTION] WHERE TRNSCRIPTS LIKE'%CALCULATE%' and TRNSCRIPTS like'%D01%') \
                    select @horafinD01=(SELECT max(trnLastDate) FROM[TRANSACTION]WHERE TRNSCRIPTS LIKE'%CALCULATE%'and TRNSCRIPTS like'%D01%') \
                    select @horainicioD02=(SELECT max(Trndate) FROM[TRANSACTION] WHERE TRNSCRIPTS LIKE'%CALCULATE%' and TRNSCRIPTS like'%D02%') \
                    select @horafinD02=(SELECT max(trnLastDate) FROM[TRANSACTION]WHERE TRNSCRIPTS LIKE'%CALCULATE%'and TRNSCRIPTS like'%D02%') \
                    select @horainicioD03=(SELECT max(Trndate) FROM[TRANSACTION] WHERE TRNSCRIPTS LIKE'%CALCULATE%' and TRNSCRIPTS like'%D03%') \
                    select @horafinD03=(SELECT max(trnLastDate) FROM[TRANSACTION]WHERE TRNSCRIPTS LIKE'%CALCULATE%'and TRNSCRIPTS like'%D03%') \
                    select @horainicioD04=(SELECT max(Trndate) FROM[TRANSACTION] WHERE TRNSCRIPTS LIKE'%CALCULATE%' and TRNSCRIPTS like'%D04%') \
                    select @horafinD04=(SELECT max(trnLastDate) FROM[TRANSACTION]WHERE TRNSCRIPTS LIKE'%CALCULATE%'and TRNSCRIPTS like'%D04%') \
                    select @horainicioD05=(SELECT max(Trndate) FROM[TRANSACTION] WHERE TRNSCRIPTS LIKE'%CALCULATE%' and TRNSCRIPTS like'%D05%') \
                    select @horafinD05=(SELECT max(trnLastDate) FROM[TRANSACTION]WHERE TRNSCRIPTS LIKE'%CALCULATE%'and TRNSCRIPTS like'%D05%') \
                    select @PreventastockD1= (select  top(1) aptTransactionDate from dbo.AREAPRODUCT where areCode='D01') \
                    select @DespachostockD1= (select  top(1) aptServerLastUpdate from dbo.AREAPRODUCT where areCode='D01') \
                    select @PreventastockD2= (select  top(1) aptTransactionDate from dbo.AREAPRODUCT where areCode='D02') \
                    select @DespachostockD2= (select  top(1) aptServerLastUpdate from dbo.AREAPRODUCT where areCode='D02') \
                    select @PreventastockD3= (select  top(1) aptTransactionDate from dbo.AREAPRODUCT where areCode='D03') \
                    select @DespachostockD3= (select  top(1) aptServerLastUpdate from dbo.AREAPRODUCT where areCode='D03') \
                    select @PreventastockD4= (select  top(1) aptTransactionDate from dbo.AREAPRODUCT where areCode='D04') \
                    select @DespachostockD4= (select  top(1) aptServerLastUpdate from dbo.AREAPRODUCT where areCode='D04') \
                    select @PreventastockD5= (select  top(1) aptTransactionDate from dbo.AREAPRODUCT where areCode='D05') \
                    select @DespachostockD5= (select  top(1) aptServerLastUpdate from dbo.AREAPRODUCT where areCode='D05') \
                    select \
                    @PreventastockD1 as PQuito, \
                    @DespachostockD1 as DQuito, \
                    dateadd (hh,-1,@horainicioD01) as IQuito, \
                    dateadd (hh,-1,@horafinD01) as FQuito, \
                    @PreventastockD2 as PGye, \
                    @DespachostockD2 as DGye, \
                    dateadd (hh,-1,@horainicioD02) as IGye, \
                    dateadd (hh,-1,@horafinD02) as FGye, \
                    @PreventastockD3 as PSt, \
                    @DespachostockD3 as DSt, \
                    dateadd (hh,-1,@horainicioD03) as ISt, \
                    dateadd (hh,-1,@horafinD03) as FSt, \
                    @PreventastockD4 as PCuenca, \
                    @DespachostockD4 as DCuenca, \
                    dateadd (hh,-1,@horainicioD04) as ICUENCA, \
                    dateadd (hh,-1,@horafinD04) as FCUENCA, \
                    @PreventastockD5 as PMontecristi, \
                    @DespachostockD5 as DMontecristi, \
                    dateadd (hh,-1,@horainicioD05) as IMON, \
                    dateadd (hh,-1,@horafinD05) as FMON, \
                    @customerxss as CUSTOMER_XSS, @cusdelete as CUSTOMER_DELETE_0,@customerroute1 as CUSROUT_TOTAL, \
                    @customerroute as CUSROUTE_VISIT_TODAY,@cusst as CUSSTATUS_VISIT_TODAY,@customerstatus as CUSSTATUS_TOTAL, \
                    @product as PRODUCT, @catalog as CATALOG, @promotion as PROMOTION,@promotiond as PROMOTIOND, @promotiondp as PROMOTIONDP, \
                    @genericou as GENUIO, @genericog as GENGYE, @genericoc as GENCUE, @genericom as GENMON",
            "name":"Stock Directa"
        }
    ]

def query_catalogo(item):
    return [
        {
            "query":f"select top 100 procode item, proname nombre, proshortname nombre_corto, \
                    untcode unidad, proInactive inacnito, _deleted eliminado \
                    from product where procode in({item})",
            "name":"PRODUCTO"
        },
        {
            "query":f"SELECT TOP 100 arecode area, procode item, untcode unidad, \
                    aptquantity cantidad, aptclosed cerrado \
                    FROM AREAPRODUCT where procode in({item})",
            "name":"STOCK"
        },
        {
            "query":f"SELECT DISTINCT TOP 100 c.catCode CATALOGO, c.catname NOMBRE, \
                    cd.procode PROCODE, \
                    case c.catActive \
                    when 1 then'SI'when 0 then'NO'end as ACTIVO, \
                    case c._deleted \
                    when 1 then'SI'when 0 then'NO'end as ELIMINADO, \
                    case cd.cdeExcluded \
                    when 1 then'EXCLUIDO'when 0 then'NO_EXCLUIDO'end as CDEEXCLUDED \
                    FROM catalog c \
                    INNER JOIN catalogdetail cd \
                    ON c.catcode= cd.catcode \
                    where cd.procode IN({item})",
            "name":"CATALOGO"
        }
    ]


def query_licencias_activas():
    return [
        {
            "query":"select top 1000 count(*) REGISTROS \
                    from company c \
                    inner join \
                    companyBranch cb on c.comCode=cb.comCode \
                    inner join branch b on cb.brcCode=b.brcCode \
                    inner join login l on b.brcCode=l.brcCode \
                    inner join route r on l.lgnCode=r.lgnCode \
                    WHERE r.rotInactive=0 \
                    AND r._deleted=0 \
                    AND c.comCode='1000'",
            "name":"LICENCIAS_ACTIVAS"
        }
    ]

def query_status_total_parcial_10_min():
    return [
        {
            "query":"SELECT TOP 100  DB_NAME() as DZ_Regional, count(*) Result FROM \
                            General \
                            WHERE (DATEDIFF(MINUTE, dateadd(hh,-1,gnlStatusDate), dateadd(hh,-1,GETDATE())) >= 10 \
                            AND gnlStatus between 9 and 10) or (DATEDIFF(MINUTE, dateadd(hh,-1,gnlPartialStatusDate), dateadd(hh,-1,GETDATE()))>= 10 \
                        AND gnlPartialStatus<8 AND gnlStatus<10)",
            "name":"RUTAS_STATUS_TOTAL_PARCIAL_10_MIN"
        }
    ]


def query_clave_usuario(ruta):
    return [
        {
            "query":f"select top 100 \
                r.rotcode, r.rotInactive,r._deleted,r.rotName,TRIM(r.lgnCode), TRIM(l.lgnPassword) \
                from route r \
                INNER JOIN login l \
                ON r.lgnCode=l.lgnCode \
                where rotcode='{ruta}'",
            "name":"CLAVE_USUARIO"
        }
    ]

#retornos

def query_retornos(fecha):
    return [
        {
            "query":f"select top 10000 reacode, dmdprocess PROCESADO, dmddate FECHA, doccode Documento, dmdCode SECUENCIAL, rotCode RUTA, _processMessage RESPUESTA from demand where CONVERT(date,dmddate,101)='{fecha}' AND \
            DMDCANCELORDER='0' and (dmdcode in (select dmdcode from demandproduct where dptquantity<>dptmodifiedquantity) or dmdcode IN \
            (select DMDCODE FROM DEMAND WHERE REACODE<>'000') or dmdcode in (select dmdcode from demand where doccode='dev01' and dmdinvoice='1')) and dmdprocess='0'",
            "name":"RETORNO_ENTREGA_NO_PROCESADOS"
        }
    ]

def query_retornos_no_procesados_ruta_fecha(ruta, fecha):
    return [
        {
            "query":f"select top 10000 reacode, dmdprocess PROCESADO, dmddate FECHA, doccode Documento, dmdCode SECUENCIAL, rotCode RUTA, _processMessage RESPUESTA from demand where CONVERT(date,dmddate,101)='{fecha}' AND \
            DMDCANCELORDER='0' and (dmdcode in (select dmdcode from demandproduct where dptquantity<>dptmodifiedquantity) or dmdcode IN \
            (select DMDCODE FROM DEMAND WHERE REACODE<>'000') or dmdcode in (select dmdcode from demand where doccode='dev01' and dmdinvoice='1')) and dmdprocess='0' and rotcode='{ruta}'",
            "name":"RETORNO_ENTREGA_NO_PROCESADOS_RUTA_FECHA"
        }
    ]

def query_retornos_si_procesados_ruta_fecha(ruta, fecha):
    return [
        {
            "query":f"select top 10000 reacode, dmdprocess PROCESADO, dmddate FECHA, doccode Documento, dmdCode SECUENCIAL, rotCode RUTA, _processMessage RESPUESTA from demand where CONVERT(date,dmddate,101)='{fecha}' AND \
            DMDCANCELORDER='0' and (dmdcode in (select dmdcode from demandproduct where dptquantity<>dptmodifiedquantity) or dmdcode IN \
            (select DMDCODE FROM DEMAND WHERE REACODE<>'000') or dmdcode in (select dmdcode from demand where doccode='dev01' and dmdinvoice='1')) and dmdprocess='1' and rotcode='{ruta}'",
            "name":"RETORNO_ENTREGA_SI_PROCESADOS_RUTA_FECHA"
        }
    ]

#COBROS No procesados total
def query_cobros_diarios(fecha):
    return [
        {
            "query":f"select top 1000 payDate Fecha_Cobro,payProcess Procesado,dateadd(hh,-1,_processDate) Fecha_Procesado,payCancel Eliminado,payAmount Monto, payCode Secuencia,rotcode Ruta, cuscode Cliente, _processMessage Respuesta \
                    from payment where  CONVERT(DATE,PAYDATE,101)='{fecha}' and payCancel='0' and payProcess='0'",
            "name":"COBROS_DIARIOS_NO_PROCESADOS"
        }
    ]

#Si procesados total
def query_cobros_diarios_si_procesados(fecha):
    return [
        {
            "query":f"select top 1000 payDate Fecha_Cobro,payProcess Procesado,dateadd(hh,-1,_processDate) Fecha_Procesado,payCancel Eliminado,payAmount Monto, payCode Secuencia,rotcode Ruta, cuscode Cliente, _processMessage Respuesta \
                    from payment where  CONVERT(DATE,PAYDATE,101)='{fecha}' and payCancel='0' and payProcess='1'",
            "name":"COBROS_DIARIOS_SI_PROCESADOS"
        }
    ]

#No procesados ruta y fecha
def query_cobros_diarios_no_ruta_fecha(ruta, fecha):
    return [
        {
            "query":f"select top 1000 payDate Fecha_Cobro,payProcess Procesado,dateadd(hh,-1,_processDate) Fecha_Procesado,payCancel Eliminado,payAmount Monto, payCode Secuencia,rotcode Ruta, cuscode Cliente, _processMessage Respuesta \
                    from payment where  CONVERT(DATE,PAYDATE,101)='{fecha}' and payCancel='0' and payProcess='0' and rotcode='{ruta}'",
            "name":"COBROS_DIARIOS_NO_PROCESADOS_RUTA_FECHA"
        }
    ]


#Si procesados ruta y fecha
def query_cobros_diarios_si_ruta_fecha(ruta, fecha):
    return [
        {
            "query":f"select top 1000 payDate Fecha_Cobro,payProcess Procesado,dateadd(hh,-1,_processDate) Fecha_Procesado,payCancel Eliminado,payAmount Monto, payCode Secuencia,rotcode Ruta, cuscode Cliente, _processMessage Respuesta \
                    from payment where  CONVERT(DATE,PAYDATE,101)='{fecha}' and payCancel='0' and payProcess='1' and rotcode='{ruta}'",
            "name":"COBROS_DIARIOS_SI_PROCESADOS:RUTA_FECHA"
        }
    ]

def query_rutas_por_sincronizar(fecha):
    return [
        {
            "query":f"Select top 10000 rotCode RUTA, gnlDate FECHA, gnlStatus ESTADO from general where convert(date,gnlDate,101)='{fecha}' \
            and rotcode in(select rotcode from route where rotDummy1='PDA' and _deleted='0' and rotInactive='0') \
            and gnlStatus BETWEEN '3' AND '10'",
            "name":"RUTAS_POR_SINCRONIZAR"
        }
    ]

def query_sincronizacion_rutas():
    return [
        {
            "query":f"SELECT TOP 100 ROTCODE RUTA, GNLDATE PREVENTA, GNLNEXTWORKINGDAY DESPACHO, JRNCODE, \
                    GNLSTATUS, GNLSTATUSDATE, GNLPARTIALSTATUS, GNLPARTIALSTATUSDATE FROM GENERAL",
            "name":"SINCRONIZACION_RUTAS"
        }
    ]


def query_informacion_entrega(ruta):
    return [
        {
            "query":f"declare @fecha date, @date date, @manana date, @status int, @fac int, @dev int, @customerroute int, @carga date, @ruta VARCHAR(255), @jrn VARCHAR(255) \
                    set @ruta='{ruta}' \
                    set @fecha=GETDATE() \
                    select @date= (select  top(1) gnlDate from general where rotcode=@ruta) \
                    select @manana= (select  top(1) gnlNextWorkingDay from general where rotcode=@ruta) \
                    select @status=(select top(1) gnlStatus from general where rotcode=@ruta) \
                    select @jrn=(select top(1) jrnCode from general where rotcode=@ruta) \
                    select @carga=(select top(1) rldDate from reload where rotcode=@ruta order by rldDate desc) \
                    select @customerroute=(select count(*) from customerroute where rotcode=@ruta) \
                    select @fac=(select count(*) from demand where rotcode=@ruta and docCode='FAC' and dmddate=@fecha) \
                    select @dev=(select count(*) from demand where rotcode=@ruta and docCode='DEV01' and dmddate=@fecha) \
                    select @date as DATE, @manana as MANANA, @customerroute as CUSTOMERROUTE, @jrn as JOURNEY, @status as STATUS, @carga as CARGA_CAMION, @fac as FAC, @dev as DEV",
            "name":"INFORMACION_ENTREGA"
        }
    ]


def query_clientes_nuevos(fecha):
    return [
        {
            "query":f"select top 100 cusSystemDate as Fecha_Creacion, \
            case cusProcess \
            when 1 then'SI' \
            when 0 then'NO' \
            end as Procesado,cusemail Email, \
            case \
            when cusBackEndCode IS NULL then '--' \
            ELSE cusBackEndCode \
            end as Encuesta, \
            case cusnew \
            when 1 then'SI' \
            when 0 then'NO' \
            end as Nuevo,cuscode Cliente, rotcode Ruta, cusTaxID1 Identificacion, cusBusinessName Razon_Social, \
            case \
            when _processMessage IS NULL then '--' \
            ELSE _processMessage \
            end as Respuesta \
            from customerup where convert(date, CUSSYSTEMDATE, 101) = '{fecha}' and cusnew = 'true'",
            "name":"CLIENTES_NUEVOS"
        }
    ]


def query_clientes_nuevos_ruta(ruta, fecha):
    return [
        {
            "query":f"select top 100 cusSystemDate as Fecha_Creacion, \
            case cusProcess \
            when 1 then'SI' \
            when 0 then'NO' \
            end as Procesado,cusemail Email, \
            case \
            when cusBackEndCode IS NULL then '--' \
            ELSE cusBackEndCode \
            end as Encuesta, \
            case cusnew \
            when 1 then'SI' \
            when 0 then'NO' \
            end as Nuevo,cuscode Cliente, rotcode Ruta, cusTaxID1 Identificacion, cusBusinessName Razon_Social, \
            case \
            when _processMessage IS NULL then '--' \
            ELSE _processMessage \
            end as Respuesta \
            from customerup where convert(date, CUSSYSTEMDATE, 101) = '{fecha}' and cusnew = 'true' and rotcode = '{ruta}'",
            "name":"CLIENTES_NUEVOS"
        }
    ]


def query_detalle_diario(fecha):
    return [
        {
            "query":f"declare @fecha VARCHAR(255), @total int, @ex int, @np int, @err int, @rp int, @cusnp int, @result int, @times datetime \
                    set @fecha='{fecha}' \
                    select top(100) @total= (select count(*) from demand where convert(date,dmddate,101)=@fecha and dmdCancelOrder='0') \
                    select @ex= (select count(*) from demand where convert(date,dmddate,101)=@fecha and dmdCancelOrder='0' and dmdprocess='1' and _processError='3') \
                    select @np= (select count(*) from demand where convert(date,dmddate,101)=@fecha and dmdCancelOrder='0' and dmdprocess='0') \
                    select @err= (select count(*) from demand where convert(date,dmddate,101)=@fecha and dmdCancelOrder='0' and _processError<>3) \
                    select @rp= (select count(*) from general where convert(date,gnlDate,101)=@fecha and gnlStatus BETWEEN '3' AND '10') \
                    select @cusnp= (select count(*) from customerup where convert(date,CUSSYSTEMDATE,101)=@fecha and cusProcess='0' and cusNew='1') \
                    select @result= (select count(*) from general WHERE (DATEDIFF(MINUTE, dateadd(hh,-1,gnlStatusDate), dateadd(hh,-1,GETDATE())) >= 10 AND gnlStatus between 9 and 10) or (DATEDIFF(MINUTE, dateadd(hh,-1,gnlPartialStatusDate), dateadd(hh,-1,GETDATE()))>= 10 AND gnlPartialStatus<8 AND gnlStatus<10) )	\
                    SELECT @times= (select CURRENT_TIMESTAMP) \
                    select DB_NAME() as DZ_Regional, @total as DMD_TOTAL, @ex as DMD_EXITO, @np as DMD_NP, @err DMD_ERR, @rp as RP, @cusnp as CUSNP, @result as retarded, dateadd (hh,-1,@times) as TIMESTAMP",
            "name":"DETALLE_DIARIO"
        }
    ]



def query_detalle_diario_por_rutas(fecha):
    return [
        {
            "query":f"select \
                    top 100 \
                    DB_NAME() as DZ_Regional, \
                    d.rotcode as Ruta, \
                    sum(case when dmdCancelOrder='0' and doccode='ped' then 1 else 0 end) TPedido, \
                    sum(case when dmdCancelOrder='0' and doccode='dev' then 1 else 0 end) TDevolucion, \
                    sum(case when dmdCancelOrder='0' and dmdprocess='0' and doccode='ped' then 1 else 0 end) PedidoPorPocesar, \
                    sum(case when dmdCancelOrder='0' and dmdprocess='0' and doccode='dev' then 1 else 0 end) DevPorPocesar \
                    from demand d INNER JOIN general g on d.rotcode= g.rotcode where convert(date,dmddate,101)='{fecha}' group by d.rotcode, g.gnlStatus, g.gnlStatusDate \
                    order by d.rotcode asc",
            "name":"DETALLE_DIARIO_POR_RUTA"
        }
    ]


def query_ultimos_pedidos(cliente):
    return [
        {
            "query":f"SELECT TOP 100 DMDDATE PREVENTA, dmdDeliveryDate DESPACHO, ROTCODE RUTA, CUSCODE CLIENTE, \
                DMDCANCELORDER CANCELADO,DOCCODE TIPO, DMDPROCESS PROCESADO,_processMessage RESPUESTA, \
                dateadd(hh,-1,_processDate) FECHA_PROCESO, dmdCode SECUENCIAL \
                FROM DEMAND WHERE DOCCODE IN('ped','dev') AND CUSCODE IN('{cliente}') ORDER BY DMDDATE DESC",
            "name":"ULTIMOS_PEDIDOS_CLIENTE"
        }
    ]

def query_detalle_pedido_cliente_fecha(cliente, fecha):
    return [
        {
            "query":f"select top 1000 d.dmddate Preventa, d.dmdcode Referencia, d.rotcode Vendedor, \
                    d.doccode Tipo, d.cuscode Cliente, \
                    p.procode Producto, p.dptmodifiedquantity Cantidad, p.dptPromotionQuantity Promocion, p.dptUnattendedSales StandBy, \
                    d._processMessage RESPUESTA, dateadd(hh,-1,d._processDate) FECHA_PROCESO \
                    from Demand d inner Join DemandProduct p on d.dmdcode= p.dmdcode \
                    where d.doccode='ped' AND convert(date,dmddate,101)='{fecha}' and dmdCancelOrder='0' and d.cuscode in('{cliente}')",
            "name":"DETALLE_PEDIDO_CLIENTE_FECHA"
        }
    ]

def query_detalle_pedido_dmd_code(dmd_code):
    return [
        {
            "query":f"select top 100000 d.dmddate Preventa, d.dmdcode Referencia, d.rotcode Vendedor, \
            d.doccode Tipo, d.cuscode Cliente, \
            p.procode Producto, p.dptmodifiedquantity Cantidad, p.dptPromotionQuantity Promocion, p.dptUnattendedSales StandBy, \
            d._processMessage RESPUESTA,dateadd(hh,-1,d._processDate) FECHA_PROCESO \
            from Demand d inner Join DemandProduct p on d.dmdcode= p.dmdcode \
            and d.dmdcode in('{dmd_code}')",
            "name":"DETALLE_PEDIDO_DMD_CODE"
        }
    ]


def query_detalle_pedido_directa(fecha):
    return [
        {
            "query":f"select top(50) \
            brcCode as Regional, \
            sum(case when dmdCancelOrder='0' and doccode='ped' then 1 else 0 end) TotalPedidos, \
            sum(case when dmdCancelOrder='0' and doccode='dev' then 1 else 0 end) TotalDevoluciones, \
            sum(case when (_processMessage='-0' OR _processMessage like'%exito%') and doccode='ped' then 1 else 0 end) PedidosExito, \
            sum(case when (_processMessage='-0' OR _processMessage like'%exito%') and doccode='dev' then 1 else 0 end) DevolucionesExito, \
            sum(case when dmdCancelOrder='0' and dmdprocess='0' and doccode='ped' then 1 else 0 end) pSINPROCESAR, \
            sum(case when dmdCancelOrder='0' and dmdprocess='0' and doccode='dev' then 1 else 0 end) dSINPROCESAR, \
            sum(case when (_processMessage like'%transito%') and doccode='ped' then 1 else 0 end) PTransito, \
            sum(case when (_processMessage like'%transito%') and doccode='dev' then 1 else 0 end) DTransito, \
            sum(case when (_processMessage like'%soap%') and doccode='ped' then 1 else 0 end) PSoap, \
            sum(case when (_processMessage like'%soap%') and doccode='dev' then 1 else 0 end) DSoap, \
            sum(case when (_processMessage like'%error%') and doccode='ped' then 1 else 0 end) PErr, \
            sum(case when (_processMessage like'%error%') and doccode='dev' then 1 else 0 end) DErr, \
            sum(case when (_processMessage like'%existente%') and doccode='ped' then 1 else 0 end) PExistente, \
            sum(case when (_processMessage like'%existente%') and doccode='dev' then 1 else 0 end) DExistente \
            from demand where Convert(date,dmdDate,101)='{fecha}' \
            and rotcode in(select rotcode from route where rotDummy1='PDA'  and chaCode='V01' and _deleted='0' and rotInactive='0') \
            group by brcCode order by brcCode asc",
            "name":"DETALLE_PEDIDO_DIRECTA"
        }
    ]


def query_catalogo_solo_dz(item):
    return [
        {
            "query":f"SELECT DISTINCT TOP 100 \
                c.catCode AS PORTAFOLIO, \
                DB_NAME() AS DZ_Regional, \
                P.proInactive AS INACTIVO, \
                P._deleted AS ELIMINADO, \
                P.procode AS PRODUCTO, \
                A.areCode, \
                A.aptQuantity, \
                A.aptClosed, \
                A.aptTransactionDate, \
                A.aptServerLastUpdate \
            FROM \
                product P \
            LEFT JOIN \
                catalogdetail C ON P.procode = C.procode \
            LEFT JOIN \
                areaproduct A ON P.procode = A.procode AND A.areCode = 'A001' \
            WHERE \
                P.procode IN ({item})",
            "name":"PORTAFOLIO_SOLO_DZ"
        }
    ]


def query_detalle_devolucion_cliente_fecha(cliente, fecha):
    return [
        {
            "query":f"select top 100000 d.dmddate Preventa, d.rotcode Vendedor, d.doccode Tipo, d.cuscode Cliente, \
            p.procode Producto, p.dpnQuantity Cantidad, \
            d._processMessage RESPUESTA, dateadd(hh,-1,d._processDate) FECHA_PROCESO \
            from Demand d inner Join DemandProductReturn  p on d.dmdcode= p.dmdcode \
            and d.cuscode in('{cliente}') and convert(date,d.dmddate,101)='{fecha}' and d.dmdCancelOrder='0'",
            "name":"DETALLE_DEVOLUCION_CLIENTE_FECHA"
        }
    ]

def query_detalle_cliente_nuevo_pedido(fecha):
    return [
        {
            "query":f"SELECT TOP 100 \
            C.cusSystemDate FECHA, C.ROTCODE RUTA, C.CUSCODE CLIENTE, C.cusName NOMBRE, C.cusBusinessName NEGOCIO, C.cusemail EMAIL, C.cusBackEndCode ENCUESTA, C.cusnew NEW, C.cusProcess PROCESADO, C._processMessage RESPUESTA_C,C._processDate FCLIENTE, \
            D.DMDCODE PEDIDO, D.dmdCancelOrder CANCELADO, D.dmdprocess PROCESADOD, D._processMessage RESPUESTAPEDIDO,D._processDate FPEDIDO \
            FROM DEMAND D \
            RIGHT JOIN CUSTOMERUP C \
            ON \
            D.cusCodeNewCustomer=C.CUSCODE \
            where convert(date,C.CUSSYSTEMDATE,101)='{fecha}'AND C.cusnew='true'",
            "name":"CLIENTE_NUEVO_PEDIDO"
        }
    ]


def query_catalogo_solo_pronaca(item):
    return [
        {
            "query":f"SELECT DISTINCT TOP 100 c.catCode CATALOGO, c.catname NOMBRE, \
                    cd.procode PROCODE, \
                    case c.catActive \
                    when 1 then'SI'when 0 then'NO'end as ACTIVO, \
                    case c._deleted \
                    when 1 then'SI'when 0 then'NO'end as ELIMINADO, \
                    case cd.cdeExcluded \
                    when 1 then'EXCLUIDO'when 0 then'NO_EXCLUIDO'end as CDEEXCLUDED \
                    FROM catalog c \
                    INNER JOIN catalogdetail cd \
                    ON c.catcode= cd.catcode \
                    where cd.procode IN ({item})",
            "name":"CATALOGO_SOLO_PRONACA"
        }
    ]

def query_sincronizo_mas_de_una_vez():
    return [
        {
            "query":f"WITH LastStatus AS ( \
                        SELECT \
                            rotcode, \
                            jrtstatus, \
                            jrtstatusdate, \
                            ROW_NUMBER() OVER (PARTITION BY rotcode ORDER BY jrtstatusdate DESC) AS rn \
                        FROM \
                            journeytrace \
                    ) \
                    SELECT top 100 \
                        t1.rotcode, \
                        t1.jrtstatusdate AS fecha_no_sincronizado, \
                        t2.jrtstatusdate AS fecha_sincronizado, \
                        t3.jrtstatusdate AS fecha_vuelto_no_sincronizado, \
                        ls.jrtstatus AS ultimo_estado, \
                        ls.jrtstatusdate AS fecha_ultimo_estado \
                    FROM \
                        journeytrace t1 \
                    JOIN \
                        journeytrace t2 ON t1.rotcode = t2.rotcode AND t2.jrtstatus = 3 \
                    JOIN \
                        journeytrace t3 ON t1.rotcode = t3.rotcode AND t3.jrtstatus = 2 \
                    JOIN \
                        LastStatus ls ON t1.rotcode = ls.rotcode AND ls.rn = 1 \
                    WHERE \
                        t1.jrtstatus = 2 \
                        AND t1.jrtstatusdate < t2.jrtstatusdate \
                        AND t2.jrtstatusdate < t3.jrtstatusdate \
                        AND CAST(t1.jrtstatusdate AS DATE) = CAST(GETDATE() AS DATE) \
                    ORDER BY \
                        t1.rotcode, t1.jrtstatusdate",
            "name":"SINCRONIZO_MAS_DE_UNA_VEZ"  
            }
    ]   

def documentos_ventas_tiempo_excedido(fecha, timer):
    return [
        {
            "query":f"SELECT TOP 100 \
                            g.rotCode, \
                            d.docCode, \
                            COUNT(*) AS cantidad_registros, \
                            g.gnlStatus, \
                            DATEADD(HOUR, -1, g.gnlStatusDate) sincronizacion_completa, \
                            MAX(DATEDIFF(MINUTE, DATEADD(HOUR, -1, g.gnlStatusDate), DATEADD(HOUR, -1, GETDATE()))) AS minutos_transcurridos, \
                            MAX(CASE \
                                WHEN DATEDIFF(MINUTE, DATEADD(HOUR, -1, g.gnlStatusDate), DATEADD(HOUR, -1, GETDATE())) > {timer} \
                                    THEN 1 ELSE 0 \
                            END) AS tiempo_transcurrido_mayor_10_min \
                        FROM \
                            general g \
                        INNER JOIN \
                            demand d ON g.rotCode = d.rotCode \
                        WHERE \
                            g.gnlStatus = 11 \
                            AND d.dmdCancelOrder = 0 \
                            AND d.dmdProcess = 0 \
                            AND d.docCode IN ('ped', 'dev') \
                            AND CONVERT(DATE, d.dmdDate, 101) = '{fecha}' \
                            AND DATEDIFF(MINUTE, DATEADD(HOUR, -1, g.gnlStatusDate), DATEADD(HOUR, -1, GETDATE())) > {timer} \
                        GROUP BY \
                            g.rotCode, d.docCode, g.gnlStatusDate, g.gnlStatus",
            "name":"DOCUMENTOS_VENTAS_TIEMPO_EXCEDIDO"
        }
    ]   

def documentos_entregas_tiempo_excedido(fecha, timer):
    return [
        {
            "query":f"SELECT TOP 100 \
                            g.rotCode, \
                            d.docCode, \
                            COUNT(*) AS cantidad_registros, \
                            g.gnlStatus, \
                            DATEADD(HOUR, -1, g.gnlStatusDate) sincronizacion_completa, \
                            MAX(DATEDIFF(MINUTE, DATEADD(HOUR, -1, g.gnlStatusDate), DATEADD(HOUR, -1, GETDATE()))) AS minutos_transcurridos, \
                            MAX(CASE \
                                WHEN DATEDIFF(MINUTE, DATEADD(HOUR, -1, g.gnlStatusDate), DATEADD(HOUR, -1, GETDATE())) > {timer} \
                                    THEN 1 ELSE 0 \
                            END) AS tiempo_transcurrido_mayor_10_min \
                        FROM \
                            general g \
                        INNER JOIN \
                            demand d ON g.rotCode = d.rotCode \
                        WHERE \
                            g.gnlStatus = 11 \
                            AND d.dmdCancelOrder = 0 \
                            AND d.dmdProcess = 0 \
                            AND d.docCode IN ('FAC','DEV01') \
                            AND CONVERT(DATE, d.dmdDate, 101) = '{fecha}' \
                            AND DATEDIFF(MINUTE, DATEADD(HOUR, -1, g.gnlStatusDate), DATEADD(HOUR, -1, GETDATE())) > {timer} \
                        GROUP BY \
                            g.rotCode, d.docCode, g.gnlStatusDate, g.gnlStatus",
            "name":"DOCUMENTOS_ENTREGAS_TIEMPO_EXCEDIDO"
        }
    ]   


















