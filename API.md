二维码扫描得网址为明ip
> 115.239.202.76:8181
经查询纯真数据如下

> 中国浙江金华义乌市

> 电信chinatelecom.com.cn

> 地区中心经纬度29.10721, 119.64901

> 住宅用户/企业用户

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
