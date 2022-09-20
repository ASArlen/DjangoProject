from django.db import models

# Create your models here.

# Application_Type = [
#     (0,"CS"),
#     (1,"REM"),
#     (2,"COL"),
#     (4,"Shared")
# ]
# class Project(models.Model):
#     #Field name
#     #Service ID
#     service_id = models.CharField(max_length=200,blank=False,verbose_name="Service ID")
#     #Application_Type
#     application_type = models.SmallIntegerField(blank=False,choices=Application_Type,verbose_name="Application Type")
#     #Interface Name
#     interface_name = models.CharField(max_length=200, blank=False, verbose_name="Interface Name")
#
#
#     class Meta:
#         verbose_name = "Interface Management"
#         verbose_name_plural = verbose_name

#############################################################################################################
#############################################################################################################
#############################################################################################################


class Application(models.Model):
    """
    Application Table
    """
    application = models.CharField(verbose_name='应用',max_length=32)

    def __str__(self):
        return self.application

class Interface(models.Model):
    """
    Interface Table
    """
    # account = models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=0)
    interface_name = models.CharField(verbose_name='接口名称', max_length=32)
    # service_id = models.IntegerField(verbose_name="ESB ID")
    service_id = models.CharField(verbose_name="ESB ID",max_length=16)
    create_time = models.CharField(verbose_name="创建时间",max_length=128)
    # create_time = models.DateTimeField(verbose_name="创建时间")

    #无约束
    # application_id = models.BigIntegerField(verbose_name='application id')

    # 有约束
    # to 与哪张表关联
    # to_field 与哪一列关联
    # django自动
    # 写的application
    # 生成数列自动+ application_id
    #级联删除
    application = models.ForeignKey(to="Application",to_field="id",on_delete=models.CASCADE)
    # 置空
    # application = models.ForeignKey(to="Application", to_field="id", null=True,blank=True,on_delete=models.SET_NULL)

    # 在django中做的约束
    interface_method_choice = (
        (1,"POST"),
        (2,"GET"),
    )
    interface_method = models.SmallIntegerField(verbose_name="接口方式",choices=interface_method_choice)


