# me-rig-affects

1. нам поняадобятся: 
словарь с описанием групп (me_groups.sql)
табличка с вырезкой из `invmarketgroups`, где взяты только итемы с `parentGroupID`==2 (чертежи) и все их наследники (me_prepare.sql)
переделанная таблица `industryactivityproducts` с добавленным столбцом `me_group`, оставлены только записи `activityID` == (1,11)  (me_industry.sql)

2. ручками добавляем в `me_prepare.sql` для родительских групп нужные категории 
можно сразу проверять наши правки онлайн (Flask -> make_me_groups.py)
![пример работы фласка](https://github.com/VovkaKorben/me-rig-affects/blob/main/check_example.png)



4. после того, как все группы выставлены, запускаем функцию из того же скрипта (make_me_groups.py -> make_groups() )

