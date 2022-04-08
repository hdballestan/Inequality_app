from django.db import models


class BaseMeta(models.Model):

    country_id = models.CharField(max_length=3, verbose_name='Country Code',
                                  db_column='Country Code', null=True, blank=True)
    country_name = models.CharField(max_length=70, verbose_name='Country Name',
                                    db_column='Country Name', null=True, blank=True)
    indicator_name = models.CharField(max_length=70, verbose_name='Indicator Name',
                                      db_column='Indicator Name', null=True, blank=True)
    indicator_code = models.CharField(max_length=70, verbose_name='Indicator Code',
                                      db_column='Indicator Code', null=True, blank=True)
    se = models.FloatField(verbose_name='1960', db_column='1960', blank=True, default=0, null=True)
    seu = models.FloatField(verbose_name='1961', db_column='1961', blank=True, default=0, null=True)
    sed = models.FloatField(verbose_name='1962', db_column='1962', blank=True, default=0, null=True)
    set = models.FloatField(verbose_name='1963', db_column='1963', blank=True, default=0, null=True)
    secu = models.FloatField(verbose_name='1964', db_column='1964', blank=True, default=0, null=True)
    seci = models.FloatField(verbose_name='1965', db_column='1965', blank=True, default=0, null=True)
    sese = models.FloatField(verbose_name='1966', db_column='1966', blank=True, default=0, null=True)
    sesi = models.FloatField(verbose_name='1967', db_column='1967', blank=True, default=0, null=True)
    seo = models.FloatField(verbose_name='1968', db_column='1968', blank=True, default=0, null=True)
    sen = models.FloatField(verbose_name='1969', db_column='1969', blank=True, default=0, null=True)
    si = models.FloatField(verbose_name='1970', db_column='1970', blank=True, default=0, null=True)
    siu = models.FloatField(verbose_name='1971', db_column='1971', blank=True, default=0, null=True)
    sid = models.FloatField(verbose_name='1972', db_column='1972', blank=True, default=0, null=True)
    sit = models.FloatField(verbose_name='1973', db_column='1973', blank=True, default=0, null=True)
    sicu = models.FloatField(verbose_name='1974', db_column='1974', blank=True, default=0, null=True)
    sici = models.FloatField(verbose_name='1975', db_column='1975', blank=True, default=0, null=True)
    sise = models.FloatField(verbose_name='1976', db_column='1976', blank=True, default=0, null=True)
    sisi = models.FloatField(verbose_name='1977', db_column='1977', blank=True, default=0, null=True)
    sio = models.FloatField(verbose_name='1978', db_column='1978', blank=True, default=0, null=True)
    sin = models.FloatField(verbose_name='1979', db_column='1979', blank=True, default=0, null=True)
    o = models.FloatField(verbose_name='1980', db_column='1980', blank=True, default=0, null=True)
    ou = models.FloatField(verbose_name='1981', db_column='1981', blank=True, default=0, null=True)
    od = models.FloatField(verbose_name='1982', db_column='1982', blank=True, default=0, null=True)
    ot = models.FloatField(verbose_name='1983', db_column='1983', blank=True, default=0, null=True)
    ocu = models.FloatField(verbose_name='1984', db_column='1984', blank=True, default=0, null=True)
    oci = models.FloatField(verbose_name='1985', db_column='1985', blank=True, default=0, null=True)
    ose = models.FloatField(verbose_name='1986', db_column='1986', blank=True, default=0, null=True)
    osi = models.FloatField(verbose_name='1987', db_column='1987', blank=True, default=0, null=True)
    oo = models.FloatField(verbose_name='1988', db_column='1988', blank=True, default=0, null=True)
    on = models.FloatField(verbose_name='1989', db_column='1989', blank=True, default=0, null=True)
    n = models.FloatField(verbose_name='1990', db_column='1990', blank=True, default=0, null=True)
    nu = models.FloatField(verbose_name='1991', db_column='1991', blank=True, default=0, null=True)
    nd = models.FloatField(verbose_name='1992', db_column='1992', blank=True, default=0, null=True)
    nt = models.FloatField(verbose_name='1993', db_column='1993', blank=True, default=0, null=True)
    ncu = models.FloatField(verbose_name='1994', db_column='1994', blank=True, default=0, null=True)
    nci = models.FloatField(verbose_name='1995', db_column='1995', blank=True, default=0, null=True)
    nse = models.FloatField(verbose_name='1996', db_column='1996', blank=True, default=0, null=True)
    nsi = models.FloatField(verbose_name='1997', db_column='1997', blank=True, default=0, null=True)
    no = models.FloatField(verbose_name='1998', db_column='1998', blank=True, default=0, null=True)
    nn = models.FloatField(verbose_name='1999', db_column='1999', blank=True, default=0, null=True)
    c = models.FloatField(verbose_name='2000', db_column='2000', blank=True, default=0, null=True)
    cu = models.FloatField(verbose_name='2001', db_column='2001', blank=True, default=0, null=True)
    cd = models.FloatField(verbose_name='2002', db_column='2002', blank=True, default=0, null=True)
    ct = models.FloatField(verbose_name='2003', db_column='2003', blank=True, default=0, null=True)
    ccu = models.FloatField(verbose_name='2004', db_column='2004', blank=True, default=0, null=True)
    cci = models.FloatField(verbose_name='2005', db_column='2005', blank=True, default=0, null=True)
    cse = models.FloatField(verbose_name='2006', db_column='2006', blank=True, default=0, null=True)
    csi = models.FloatField(verbose_name='2007', db_column='2007', blank=True, default=0, null=True)
    co = models.FloatField(verbose_name='2008', db_column='2008', blank=True, default=0, null=True)
    cn = models.FloatField(verbose_name='2009', db_column='2009', blank=True, default=0, null=True)
    u = models.FloatField(verbose_name='2010', db_column='2010', blank=True, default=0, null=True)
    uu = models.FloatField(verbose_name='2011', db_column='2011', blank=True, default=0, null=True)
    ud = models.FloatField(verbose_name='2012', db_column='2012', blank=True, default=0, null=True)
    ut = models.FloatField(verbose_name='2013', db_column='2013', blank=True, default=0, null=True)
    ucu = models.FloatField(verbose_name='2014', db_column='2014', blank=True, default=0, null=True)
    uci = models.FloatField(verbose_name='2015', db_column='2015', blank=True, default=0, null=True)
    use = models.FloatField(verbose_name='2016', db_column='2016', blank=True, default=0, null=True)
    usi = models.FloatField(verbose_name='2017', db_column='2017', blank=True, default=0, null=True)
    uo = models.FloatField(verbose_name='2018', db_column='2018', blank=True, default=0, null=True)
    un = models.FloatField(verbose_name='2019', db_column='2019', blank=True, default=0, null=True)
    d = models.FloatField(verbose_name='2020', db_column='2020', blank=True, default=0, null=True)

    class Meta:
        abstract = True


class Data(BaseMeta):

    class Meta:
        db_table = "Data"
        verbose_name = 'data'
        verbose_name_plural = 'datas'


