# # function
# # lambda
# # decorators
# # generators
# import random
# def add(a,b):
#     return a + b


# add(1,2)
# add(1,2)
# add(1,2)


# def random_number(v):
#     return random.randint(v)


# def manipulate():
#     data = 'something here'

#     return data.capitilize()



# data = 'something here'

# def manipulate(data_value):
#     return data_value.capitalize()


import  time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.perf_counter()
        ans = func(*args,*kwargs)
        end= time.perf_counter()
        timer = f'{end- start:.2f}'
        return {ans: timer}
    return wrapper



logs_data = '''Jul 26 03:36:57 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:9984 [26/Jul/2019:03:36:57.304] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:36:57 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.49:52002 [26/Jul/2019:03:36:57.337] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:36:57 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52032 [26/Jul/2019:03:36:57.438] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/30/30 200 347 - - ---- 1/1/0/0/0 0/0 {34.213.227.84} "GET /lender/touch/ HTTP/1.1"
Jul 26 03:36:57 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 127.0.0.1:44670 [26/Jul/2019:03:36:57.625] stats stats/<STATS> 0/0/0/0/0 200 5164 - - LR-- 1/1/0/0/0 0/0 "GET /haproxy?stats/;csv;norefresh HTTP/1.1"
Jul 26 03:36:59 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.55:55088 [26/Jul/2019:03:36:59.303] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:00 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52036 [26/Jul/2019:03:37:00.437] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/4/4 200 226 - - ---- 1/1/0/0/0 0/0 {18.217.88.49} "GET /ping/octane HTTP/1.1"
Jul 26 03:37:02 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.187:18186 [26/Jul/2019:03:37:02.294] stats stats/<STATS> 0/0/0/0/0 200 57102 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:05 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.72:35496 [26/Jul/2019:03:37:05.628] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:07 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:10014 [26/Jul/2019:03:37:07.311] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:07 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.49:52016 [26/Jul/2019:03:37:07.348] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:08 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52062 [26/Jul/2019:03:37:08.439] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/32/32 200 347 - - ---- 1/1/0/0/0 0/0 {34.213.227.84} "GET /lender/touch/ HTTP/1.1"
Jul 26 03:37:09 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.55:55100 [26/Jul/2019:03:37:09.314] stats stats/<STATS> 0/0/0/0/0 200 57100 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:10 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.55:31376 [26/Jul/2019:03:37:10.150] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/4/4 200 226 - - ---- 1/1/0/0/0 0/0 {34.224.255.169} "GET /ping/octane HTTP/1.1"
Jul 26 03:37:12 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52070 [26/Jul/2019:03:37:12.113] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/42/42 200 347 - - ---- 1/1/0/0/0 0/0 {34.213.227.84} "GET /lender/touch/ HTTP/1.1"
Jul 26 03:37:12 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.187:18202 [26/Jul/2019:03:37:12.305] stats stats/<STATS> 0/0/0/0/0 200 57100 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:12 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 127.0.0.1:44826 [26/Jul/2019:03:37:12.625] stats stats/<STATS> 0/0/0/0/0 200 5164 - - LR-- 1/1/0/0/0 0/0 "GET /haproxy?stats/;csv;norefresh HTTP/1.1"
Jul 26 03:37:14 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52078 [26/Jul/2019:03:37:14.731] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/38/38 200 347 - - ---- 1/1/0/0/0 0/0 {34.213.227.84} "GET /lender/touch/ HTTP/1.1"
Jul 26 03:37:15 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.72:35504 [26/Jul/2019:03:37:15.639] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:15 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52084 [26/Jul/2019:03:37:15.823] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/36/36 200 347 - - ---- 1/1/0/0/0 0/0 {34.213.227.84} "GET /lender/touch/ HTTP/1.1"
Jul 26 03:37:17 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:10052 [26/Jul/2019:03:37:17.319] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:17 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.49:52024 [26/Jul/2019:03:37:17.354] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:17 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52100 [26/Jul/2019:03:37:17.439] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/6/6 200 226 - - ---- 1/1/0/0/0 0/0 {97.107.137.214} "GET /ping/octane HTTP/1.1"
Jul 26 03:37:19 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.55:55120 [26/Jul/2019:03:37:19.325] stats stats/<STATS> 0/0/0/0/0 200 57103 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:22 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.187:18222 [26/Jul/2019:03:37:22.316] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:25 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.72:35514 [26/Jul/2019:03:37:25.649] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:27 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.187:28970 [26/Jul/2019:03:37:27.225] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/5/5 200 226 - - ---- 1/1/0/0/0 0/0 {76.72.172.208} "GET /ping/octane HTTP/1.1"
Jul 26 03:37:27 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:10070 [26/Jul/2019:03:37:27.323] stats stats/<STATS> 0/0/0/0/0 200 57100 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:27 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.49:52034 [26/Jul/2019:03:37:27.361] stats stats/<STATS> 0/0/0/0/0 200 57100 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:27 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 127.0.0.1:44982 [26/Jul/2019:03:37:27.625] stats stats/<STATS> 0/0/0/0/0 200 5164 - - LR-- 1/1/0/0/0 0/0 "GET /haproxy?stats/;csv;norefresh HTTP/1.1"
Jul 26 03:37:29 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.55:55134 [26/Jul/2019:03:37:29.326] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:32 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.187:18244 [26/Jul/2019:03:37:32.327] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:32 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.55:31412 [26/Jul/2019:03:37:32.699] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/44/44 200 1193 - - ---- 1/1/0/0/0 0/0 {73.82.145.111} "GET /api/v1/vehicles/?limit=5000&lenders__name__iexact=Roadrunner+Financial&model__make__name__iexact=Exmark&model__id=34080&year__exact=2020&leasable=0 HTTP/1.1"
Jul 26 03:37:35 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.72:35522 [26/Jul/2019:03:37:35.657] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:37 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:10090 [26/Jul/2019:03:37:37.335] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:37 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.49:52044 [26/Jul/2019:03:37:37.369] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:39 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.55:55152 [26/Jul/2019:03:37:39.337] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:39 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52140 [26/Jul/2019:03:37:39.681] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/5/5 200 226 - - ---- 1/1/0/0/0 0/0 {52.67.114.110} "GET /ping/octane HTTP/1.1"
Jul 26 03:37:42 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.187:18258 [26/Jul/2019:03:37:42.338] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:42 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 127.0.0.1:45132 [26/Jul/2019:03:37:42.625] stats stats/<STATS> 0/0/0/0/0 200 5164 - - LR-- 1/1/0/0/0 0/0 "GET /haproxy?stats/;csv;norefresh HTTP/1.1"
Jul 26 03:37:45 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.72:35536 [26/Jul/2019:03:37:45.662] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:47 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:10112 [26/Jul/2019:03:37:47.345] stats stats/<STATS> 0/0/0/0/0 200 57102 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:47 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.49:52054 [26/Jul/2019:03:37:47.376] stats stats/<STATS> 0/0/0/0/0 200 57102 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:49 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52162 [26/Jul/2019:03:37:49.123] https_frontend~ https_frontend/<NOSRV> -1/-1/-1/-1/0 503 212 - - SC-- 1/1/0/0/0 0/0 {209.17.97.114} "GET / HTTP/1.1"
Jul 26 03:37:49 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52164 [26/Jul/2019:03:37:49.175] https_frontend~ https_frontend/<NOSRV> -1/-1/-1/-1/0 503 212 - - SC-- 1/1/0/0/0 0/0 {209.17.97.114} "GET / HTTP/1.1"
Jul 26 03:37:49 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52172 [26/Jul/2019:03:37:49.269] https_frontend~ https_frontend/<NOSRV> -1/-1/-1/-1/1 503 212 - - SC-- 1/1/0/0/0 0/0 {209.17.97.114} "GET / HTTP/1.1"
Jul 26 03:37:49 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.55:55168 [26/Jul/2019:03:37:49.348] stats stats/<STATS> 0/0/0/0/0 200 57102 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:49 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.187:29012 [26/Jul/2019:03:37:49.391] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/6/6 200 226 - - ---- 1/1/0/0/0 0/0 {13.114.248.197} "GET /ping/octane HTTP/1.1"
Jul 26 03:37:52 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.187:18282 [26/Jul/2019:03:37:52.349] stats stats/<STATS> 0/0/0/0/0 200 57099 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:55 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.72:35546 [26/Jul/2019:03:37:55.673] stats stats/<STATS> 0/0/0/0/0 200 57099 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:56 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52178 [26/Jul/2019:03:37:56.276] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/4/4 200 226 - - ---- 1/1/0/0/0 0/0 {35.177.31.93} "GET /ping/octane HTTP/1.1"
Jul 26 03:37:57 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:10152 [26/Jul/2019:03:37:57.357] stats stats/<STATS> 0/0/0/0/0 200 57098 - - LR-- 2/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:57 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.49:52066 [26/Jul/2019:03:37:57.383] stats stats/<STATS> 0/0/0/0/0 200 57098 - - LR-- 2/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:57 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 127.0.0.1:45292 [26/Jul/2019:03:37:57.625] stats stats/<STATS> 0/0/0/0/0 200 5164 - - LR-- 2/1/0/0/0 0/0 "GET /haproxy?stats/;csv;norefresh HTTP/1.1"
Jul 26 03:37:59 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.55:55188 [26/Jul/2019:03:37:59.359] stats stats/<STATS> 0/0/0/0/0 200 57099 - - LR-- 2/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:37:59 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.55:31466 [26/Jul/2019:03:37:59.463] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/6/6 200 226 - - ---- 2/2/1/1/0 0/0 {18.217.159.174} "GET /ping/octane HTTP/1.1"
Jul 26 03:37:59 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.55:31470 [26/Jul/2019:03:37:59.501] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/5/5 200 226 - - ---- 2/2/1/1/0 0/0 {23.239.4.211} "GET /ping/octane HTTP/1.1"
Jul 26 03:38:00 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52180 [26/Jul/2019:03:37:57.209] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/3136/3143 200 243351 - - ---- 1/1/0/0/0 0/0 {34.213.227.84} "GET /lender/ HTTP/1.1"
Jul 26 03:38:02 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.187:18294 [26/Jul/2019:03:38:02.358] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:38:05 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52202 [26/Jul/2019:03:38:05.461] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/101/101 200 347 - - ---- 1/1/0/0/0 0/0 {34.213.227.84} "GET /lender/touch/ HTTP/1.1"
Jul 26 03:38:05 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.72:35558 [26/Jul/2019:03:38:05.684] stats stats/<STATS> 0/0/0/0/0 200 57100 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:38:07 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:10172 [26/Jul/2019:03:38:07.368] stats stats/<STATS> 0/0/0/0/0 200 57100 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:38:07 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.49:52082 [26/Jul/2019:03:38:07.391] stats stats/<STATS> 0/0/0/0/0 200 57100 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:38:09 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.100.55:55208 [26/Jul/2019:03:38:09.370] stats stats/<STATS> 0/0/0/0/0 200 57101 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:38:11 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52228 [26/Jul/2019:03:38:11.508] https_frontend~ https_frontend/<NOSRV> -1/-1/-1/-1/0 503 212 - - SC-- 2/2/0/0/0 0/0 {209.17.96.234} "GET / HTTP/1.1"
Jul 26 03:38:11 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52230 [26/Jul/2019:03:38:11.509] https_frontend~ https_frontend/<NOSRV> -1/-1/-1/-1/0 503 212 - - SC-- 1/1/0/0/0 0/0 {209.17.96.234} "GET / HTTP/1.1"
Jul 26 03:38:11 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52240 [26/Jul/2019:03:38:11.674] https_frontend~ https_frontend/<NOSRV> -1/-1/-1/-1/0 503 212 - - SC-- 1/1/0/0/0 0/0 {209.17.96.234} "GET / HTTP/1.1"
Jul 26 03:38:12 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52244 [26/Jul/2019:03:38:12.092] https_frontend~ https_frontend/<NOSRV> -1/-1/-1/-1/1 503 212 - - SC-- 1/1/0/0/0 0/0 {209.17.96.234} "GET / HTTP/1.1"
Jul 26 03:38:12 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.187:18314 [26/Jul/2019:03:38:12.366] stats stats/<STATS> 0/0/0/0/0 200 57100 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:38:12 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 127.0.0.1:45448 [26/Jul/2019:03:38:12.627] stats stats/<STATS> 0/0/0/0/0 200 5164 - - LR-- 1/1/0/0/0 0/0 "GET /haproxy?stats/;csv;norefresh HTTP/1.1"
Jul 26 03:38:15 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.101.72:35566 [26/Jul/2019:03:38:15.694] stats stats/<STATS> 0/0/0/0/0 200 57104 - - LR-- 1/1/0/0/0 0/0 "GET / HTTP/1.1"
Jul 26 03:38:15 prod-webproxy-02.aws.octanelending.com haproxy[23641]: 172.24.102.151:52250 [26/Jul/2019:03:38:15.841] https_frontend~ wwwprod_octanelending/marathonlb 0/0/0/33/33 200 347 - - ---- 1/1/0/0/0 0/0 {34.213.227.84} "GET /lender/touch/ HTTP/1.1"'''