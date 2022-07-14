# Generated by Django 3.2.4 on 2022-05-26 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ticket", "0067_auto_20220328_1105"),
    ]

    operations = [
        migrations.AlterField(
            model_name="status",
            name="type",
            field=models.CharField(
                choices=[
                    ("START", "开始节点(圆形)"),
                    ("NORMAL", "普通节点"),
                    ("SIGN", "会签节点"),
                    ("APPROVAL", "审批节点"),
                    ("TASK", "自动节点"),
                    ("TASK-SOPS", "标准运维节点"),
                    ("TASK-DEVOPS", "蓝盾任务节点"),
                    ("WEBHOOK", "WebHook节点"),
                    ("ROUTER", "分支网关节点(菱形)"),
                    ("ROUTER-P", "并行网关节点"),
                    ("COVERAGE", "汇聚网关节点"),
                    ("END", "结束节点(圆形)"),
                ],
                db_index=True,
                default="NORMAL",
                max_length=32,
                verbose_name="节点类型类型",
            ),
        ),
        migrations.AlterField(
            model_name="ticketcomment",
            name="source",
            field=models.CharField(
                choices=[
                    ("WEB", "蓝鲸平台"),
                    ("SMS", "短信邀请"),
                    ("SYS", "系统自评"),
                    ("API", "OPENAPI"),
                ],
                default="SYS",
                max_length=64,
                verbose_name="评价来源",
            ),
        ),
    ]