# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BusanBuk(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'busan_buk'


class BusanDong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'busan_dong'


class BusanDongnae(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'busan_dongnae'


class BusanJin(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'busan_jin'


class BusanJung(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'busan_jung'


class BusanNam(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'busan_nam'


class BusanSaha(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'busan_saha'


class BusanSasang(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'busan_sasang'


class BusanSeo(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'busan_seo'


class BusanSuyeong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'busan_suyeong'


class BusanYeongdo(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'busan_yeongdo'


class BusanYeonje(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'busan_yeonje'


class ChungbukBoeun(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungbuk_boeun'


class ChungbukCheongju(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungbuk_cheongju'


class ChungbukChungju(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungbuk_chungju'


class ChungbukDanyang(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungbuk_danyang'


class ChungbukEumseong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungbuk_eumseong'


class ChungbukJecheon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungbuk_jecheon'


class ChungbukJincheon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungbuk_jincheon'


class ChungbukOkjcheon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungbuk_okjcheon'


class ChungbukYeongdong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungbuk_yeongdong'


class ChungnamAsan(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungnam_asan'


class ChungnamBoryeong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungnam_boryeong'


class ChungnamBuyeo(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungnam_buyeo'


class ChungnamCheongyang(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungnam_cheongyang'


class ChungnamGeumsan(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungnam_geumsan'


class ChungnamGongju(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungnam_gongju'


class ChungnamGyeryong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungnam_gyeryong'


class ChungnamNonsan(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungnam_nonsan'


class ChungnamSeocheon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungnam_seocheon'


class ChungnamSeosan(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungnam_seosan'


class DaeguBuk(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daegu_buk'


class DaeguDalseo(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daegu_dalseo'


class DaeguDalseong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daegu_dalseong'


class DaeguJung(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daegu_jung'


class DaeguNam(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daegu_nam'


class DaeguSuseong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daegu_suseong'


class DaejeonDaedeok(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daejeon_daedeok'


class DaejeonEast(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daejeon_east'


class DaejeonWest(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daejeon_west'


class DaejeonYuseong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daejeon_yuseong'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GangwonDonghae(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangwon_donghae'


class GangwonGoseong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangwon_goseong'


class GangwonHongcheon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangwon_hongcheon'


class GangwonHwacheon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangwon_hwacheon'


class GangwonInje(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangwon_inje'


class GangwonJeongseon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangwon_jeongseon'


class GangwonPyeongchang(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangwon_pyeongchang'


class GangwonWonju(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangwon_wonju'


class GangwonYanggu(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangwon_yanggu'


class GangwonYangyang(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangwon_yangyang'


class GangwonYeongwol(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangwon_yeongwol'


class GwangjuEast(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gwangju_east'


class GwangjuGwangsan(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gwangju_gwangsan'


class GwangjuNorth(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gwangju_north'


class GwangjuSouth(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gwangju_south'


class GwangjuWest(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gwangju_west'


class GyeongbukAndong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_andong'


class GyeongbukBonghwa(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_bonghwa'


class GyeongbukCheongdo(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_cheongdo'


class GyeongbukChilgok(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_chilgok'


class GyeongbukGimcheon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_gimcheon'


class GyeongbukGoryeong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_goryeong'


class GyeongbukGumi(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_gumi'


class GyeongbukGunwi(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_gunwi'


class GyeongbukGyeongju(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_gyeongju'


class GyeongbukGyeongsan(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_gyeongsan'


class GyeongbukMungyeong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_mungyeong'


class GyeongbukPohang(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_pohang'


class GyeongbukSangju(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_sangju'


class GyeongbukUiseong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_uiseong'


class GyeongbukUljin(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_uljin'


class GyeongbukUlleung(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_ulleung'


class GyeongbukYecheon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_yecheon'


class GyeongbukYeongcheon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_yeongcheon'


class GyeongbukYeongdeok(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_yeongdeok'


class GyeongbukYeongyang(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk_yeongyang'


class GyeonggiAnsan(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_ansan'


class GyeonggiAnseong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_anseong'


class GyeonggiAnyang(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_anyang'


class GyeonggiBucheon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_bucheon'


class GyeonggiDongducheon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_dongducheon'


class GyeonggiGapyeong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_gapyeong'


class GyeonggiGimpo(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_gimpo'


class GyeonggiGoyang(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_goyang'


class GyeonggiGunpo(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_gunpo'


class GyeonggiGuri(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_guri'


class GyeonggiGwangju(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_gwangju'


class GyeonggiGwangmyeong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_gwangmyeong'


class GyeonggiHanam(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_hanam'


class GyeonggiHwaseong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_hwaseong'


class GyeonggiIcheon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_icheon'


class GyeonggiNamyangju(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_namyangju'


class GyeonggiOsan(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_osan'


class GyeonggiPaju(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_paju'


class GyeonggiPyeongtaek(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_pyeongtaek'


class GyeonggiSeongnam(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=100, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_seongnam'


class GyeonggiSiheung(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_siheung'


class GyeonggiSuwon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_suwon'


class GyeonggiUijeongbu(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_uijeongbu'


class GyeonggiYangju(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_yangju'


class GyeonggiYangpyeong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_yangpyeong'


class GyeonggiYeoju(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_yeoju'


class GyeonggiYeoncheon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_yeoncheon'


class GyeonggiYongin(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi_yongin'


class GyeongnamChangwon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongnam_changwon'


class GyeongnamGeoje(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongnam_geoje'


class GyeongnamGimhae(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongnam_gimhae'


class GyeongnamGoseong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongnam_goseong'


class GyeongnamHadong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongnam_hadong'


class GyeongnamHaman(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongnam_haman'


class GyeongnamHamyang(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongnam_hamyang'


class GyeongnamJinju(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongnam_jinju'


class GyeongnamMiryang(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongnam_miryang'


class GyeongnamNamhae(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongnam_namhae'


class GyeongnamSacheon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongnam_sacheon'


class GyeongnamTongyeong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongnam_tongyeong'


class GyeongnamUiryeong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongnam_uiryeong'


class IncheonEast(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incheon_east'


class IncheonGanghwa(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incheon_ganghwa'


class IncheonGyeyang(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incheon_gyeyang'


class IncheonJunggu(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incheon_junggu'


class IncheonOngjin(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incheon_ongjin'


class IncheonSoutheast(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incheon_southeast'


class IncheonWest(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incheon_west'


class IncheonYeonsu(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incheon_yeonsu'


class JejuSeogwipo(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeju_seogwipo'


class JeonbukBuan(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonbuk_buan'


class JeonbukGochang(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonbuk_gochang'


class JeonbukGunsan(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonbuk_gunsan'


class JeonbukImsil(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonbuk_imsil'


class JeonbukJeongeup(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonbuk_jeongeup'


class JeonbukJinan(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonbuk_jinan'


class JeonbukSamwon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonbuk_samwon'


class JeonbukSunchang(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonbuk_sunchang'


class JeonbukWanju(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonbuk_wanju'


class JeonnamBoseong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonnam_boseong'


class JeonnamGangjin(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonnam_gangjin'


class JeonnamGoheung(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonnam_goheung'


class JeonnamGokseong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonnam_gokseong'


class JeonnamGurye(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonnam_gurye'


class JeonnamHaenam(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonnam_haenam'


class JeonnamHampyeong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonnam_hampyeong'


class JeonnamHwasun(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonnam_hwasun'


class JeonnamJangheung(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonnam_jangheung'


class JeonnamJangseong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonnam_jangseong'


class JeonnamMokpo(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonnam_mokpo'


class JeonnamSuncheon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonnam_suncheon'


class JeonnamWando(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonnam_wando'


class JeonnamYeongam(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonnam_yeongam'


class JeonnamYeonggwang(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonnam_yeonggwang'


class JeonnamYeosu(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonnam_yeosu'


class Sejong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sejong'


class SeoulDobong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_dobong'


class SeoulDongjak(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_dongjak'


class SeoulEunpyeong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_eunpyeong'


class SeoulGangdong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_gangdong'


class SeoulGangnam(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_gangnam'


class SeoulGangseo(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_gangseo'


class SeoulGeumcheon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_geumcheon'


class SeoulGuro(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_guro'


class SeoulGwanak(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_gwanak'


class SeoulJongro(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_jongro'


class SeoulJungnang(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_jungnang'


class SeoulMapo(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_mapo'


class SeoulNowon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_nowon'


class SeoulSeocho(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_seocho'


class SeoulSeodaemun(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_seodaemun'


class SeoulSeongbuk(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_seongbuk'


class SeoulSeongdong(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_seongdong'


class SeoulSongpa(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_songpa'


class SeoulYangcheon(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_yangcheon'


class SeoulYeongdeungpo(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_yeongdeungpo'


class SeoulYongsan(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_yongsan'


class UlsanEast(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ulsan_east'


class UlsanNorth(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ulsan_north'


class UlsanSouth(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ulsan_south'


class UlsanUlju(models.Model):
    toilet_name = models.CharField(max_length=50, blank=True, null=True)
    male_female = models.CharField(max_length=1, blank=True, null=True)
    male_disabled_toilet_public_toiletnum = models.IntegerField(blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    management_agency = models.CharField(max_length=50, blank=True, null=True)
    male_toilent_num = models.IntegerField(blank=True, null=True)
    male_disabled_urinal_num = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    land_address = models.CharField(max_length=100, blank=True, null=True)
    female_toilet_num = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    male_urinal_num = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    female_child_toilet_num = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=100, blank=True, null=True)
    male_child_toilet_num = models.IntegerField(blank=True, null=True)
    male_child_urinal_num = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    female_disabled_toilet_num = models.IntegerField(blank=True, null=True)
    installation_year = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ulsan_ulju'