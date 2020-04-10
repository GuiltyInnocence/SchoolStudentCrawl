# SchoolStudentCrawl

政府采购招标花了九十万做出来的系统竟然文件**明着暴露公网**？？？

[消息来源](https://www.tianyancha.com/bid/16f134cf743f11ea85737cd30aeb144c)

![](https://GuiltyInnocence.github.io/549.jpg)
python3脚本，下载ywhs学生上传的照片
其他学校自己修改

运行库需求requests
使用包管理器安装

> pip install requests

### 注意！
文件保存在脚本同目录，所以自己新建个文件夹就行 因为懒233
# 默认整个年级！大量文件预警！

-------

二维码扫描得网址为明ip

> 115.239.202.76:8181

经查询纯真数据如下

> 中国浙江金华义乌市
电信chinatelecom.com.cn
地区中心经纬度29.10721, 119.64901
住宅用户/企业用户

鉴于其为非常规80端口的端口映射，**猜测服务器架设于学校机房**

暴露的api如下
<pre>$http({
                            method: 'post',
                            url: '../../api/faceUpload.ashx',
                            data: {
                                "schType": $scope.xdNow, "schName": $scope.schNow, "gradeName": $scope.gradeNow, "className": $scope.classNow,
                                "userName": name, "base64": base64
                            },

                        })
</pre>
<pre>$http({
                            method: 'GET',
                            url: "../../api/yw_sch.ashx?type=faceList&sch_Type=" + $scope.xdNow + "&schName=" + $scope.schNow + "&gradeName=" + $scope.gradeNow +
                                "&className=" + $scope.classNow
                        })
</pre>
<pre>$http({
                            method: 'GET',
                            url: "../../api/yw_sch.ashx?type=sch_List&sch_Type=" + xd
                        })
</pre>
