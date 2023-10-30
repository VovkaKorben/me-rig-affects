# me-rig-affects

1. нам поняадобятся: <br>
словарь с описанием групп (me_groups.sql)<br>
табличка с вырезкой из `invmarketgroups`, где взяты только итемы с `parentGroupID`==2 (чертежи) и все их наследники (me_prepare.sql)<br>
переделанная таблица `industryactivityproducts` с добавленным столбцом `me_group`, оставлены только записи `activityID` == (1,11)  (me_industry.sql)<br>

2. ручками добавляем в `me_prepare.sql` для родительских групп нужные категории <br>
можно сразу проверять наши правки онлайн (Flask -> make_me_groups.py)<br>
![пример работы фласка](https://github.com/VovkaKorben/me-rig-affects/blob/main/check_example.png)



3. после того, как все группы выставлены, запускаем функцию из того же скрипта (make_me_groups.py -> make_groups() )

4. на выходе в таблице `me_industry` имеем напротив каждого чертежа айди ME категории

