from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(max_length=1000, blank=False, null=False)
    time_create = models.DateTimeField(default=timezone.datetime.now())


class Baby(models.Model):
    age = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)


# Create your models here.
Dia_Ban = [
    (1, "Đồng bằng"), (2, "Ven biển"),
    (3, "Trung du"), (4, "Miền núi – hải đảo"),
]

Gioi_Tinh = [(0, "Nữ"), (1, "Nam"), ]

Dan_Toc = [(0, "Kinh"), (1, "Khác"), ]

Hoc_Van = [(1, "Chưa đi học"), (2, "Tiểu học"), (3, "THCS"), (4, "THPT - BTPT"), ]

Quyen_QD =[ (1, "Không có quyền ra quyết định"),
            (2, "Cùng ra quyết định với một người khác không phải là thành viên gia đình"),
            (3, "Cùng ra quyết định với một thành viên trong gia đình"),
            (4, "Vợ chồng cùng ra quyết định"),
            (5, "Tự mình ra quyết định"),]

Mucdo_QD = [(1, "Rất không tự tin"),
            (2, "Không tự tin"),
            (3, "Bình thường"),
            (4, "Khá tự tin"),
            (5, "Rất tự tin"),]

Quyen_SH = [ (1, "Không có quyền ra sở hữu"),
            (2, "Cùng sở hữu với một người khác không phải là thành viên gia đình"),
            (3, "Cùng sở hữu với một thành viên trong gia đình"),
            (4, "Vợ chồng cùng sở hữu"),
            (5, "Sở hữu một mình"),]



class Khaosat(models.Model):
    dienthoai = models.CharField(max_length=15)
    thon = models.CharField(max_length=50)
    xa = models.CharField(max_length=50)
    huyen = models.CharField(max_length=50)
    tinh = models.CharField(max_length=50)
    diaban = models.IntegerField(default=1, choices=Dia_Ban)
    gioitinh = models.IntegerField(default=0, choices=Gioi_Tinh)
    dantoc = models.IntegerField(default=0, choices=Dan_Toc)
    tuoi = models.IntegerField(default=0)
    hocvan = models.IntegerField(default=1, choices=Hoc_Van)
    cau1a1 = models.IntegerField(default=1, choices=Quyen_QD)
    cau1a2 = models.IntegerField(default=1, choices=Mucdo_QD)
    cau1b1 = models.IntegerField(default=1, choices=Quyen_QD)
    cau1b2 = models.IntegerField(default=1, choices=Mucdo_QD)
    cau1c1 = models.IntegerField(default=1, choices=Quyen_QD)
    cau1c2 = models.IntegerField(default=1, choices=Mucdo_QD)
    cau2a = models.IntegerField(default=1, choices=Quyen_SH)
    cau2b = models.IntegerField( default=1, choices=Quyen_SH)
    