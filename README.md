Простой скрипт, который позволяет из TOML-файла получать Anki-колоду.
Скрипт сделан, для работы с <a href="https://zhukovsd.github.io/java-backend-interview-prep/">методичкой</a> по вопросам Сергея Жукова.

Шаблон вызова:

<pre>main.exe|main.py "url" "path"</pre>

url - урл в интернете, указывающий най TOML-файл <br/>
path - путь в вашей файловой системе, куда вы хотите сохранить колоду

Url-ы можно найти в репозитории Сергея Жукова: https://github.com/zhukovsd/java-backend-interview-prep/tree/master/data

После выбора нужной темы, необходимо нажать "Raw", тогда url вида 
"https://github.com/zhukovsd/java-backend-interview-prep/blob/master/data/%D0%90%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%B8%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0/Message%20broker.toml" 
превратится в url вида "<a href="raw.githubusercontent.com/zhukovsd/java-backend-interview-prep/refs/heads/master/data/Архитектура и разработка/Message broker.toml">raw.githubusercontent.com/zhukovsd/java-backend-interview-prep/refs/heads/master/data/Архитектура и разработка/Message broker.toml</a>"

Программа работает только с ulr такого вида. 

После создания колоды, если в вопросах были картинки, они окажутся в папке "pictures". В связи с невозможностью программно 
прикреплять картинки к колоде, они сохраняются отдельно. Вам надо скопировать папку, которая находится внутри 
"pictures", в вашу пользовательскую папку Anki для media. У меня на Win 10 она находится в "C:\Users\user\AppData\Roaming
\Anki\ваш пользователь\collection.media"
