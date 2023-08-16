��    9      �  O   �      �     �  �     �   �  B  �    �  s  �  d   s
    �
  +  �  �     #  �           �   "  2  �  u  �  Z   Q  ^   �  8     �   D  �   �  C   �  �     2  �  �     �  �  b   �  �  �     q!     r"     y"     ~"     �"     �"     �"  =   �"      #     #  
   #  
   )#     4#     B#     U#     s#     |#  d   �#  `   �#     \$  �   k$    a%  O   r&    �&     �'     �'     �'  x  �'    r)  1   �*  �  $+  �  �,  e  �.  7  �0  �   3  �   �5  "  �6  *  �<  �  �@  d  �B     E  �  &E     �F  w  �G  �  ^J  �   <M  �   �M  �   �N  T  %O  �  zP  �   )R  i  �R  V   T  �  wZ  �  \  �   �^    j_    lb     �d     �d  6   �d  2   �d     e  K   ,e  a   xe     �e  C   �e  %   %f     Kf  $   \f  ;   �f  D   �f     g  G   g  �   ]g  �   !h     �h  �  i  �  �j  �   �l  ?  �m     �o  *   �o     p  �  $p         4       2         -         $          %       
   	      )          8       +                                      3          6   &                    5      #              .             0          (   "            !      '   /      1          9               ,          7   *    "%s" not a valid entry. A boolean that specifies whether to use the X-Forwarded-Host header in preference to the Host header. This should only be enabled if a proxy which sets this header is in use. A boolean that specifies whether to use the X-Forwarded-Port header in preference to the SERVER_PORT META variable. This should only be enabled if a proxy which sets this header is in use. USE_X_FORWARDED_HOST takes priority over this setting. A dictionary containing the settings for all databases to be used with Django. It is a nested dictionary whose contents map a database alias to a dictionary containing the options for an individual database. The DATABASES setting must configure a default database; any number of additional databases may also be specified. A list of IP addresses, as strings, that: Allow the debug() context processor to add some variables to the template context. Can use the admindocs bookmarklets even if not logged in as a staff user. Are marked as "internal" (as opposed to "EXTERNAL") in AdminEmailHandler emails. A list of all available languages. The list is a list of two-tuples in the format (language code, language name) for example, ('ja', 'Japanese'). This specifies which languages are available for language selection. Generally, the default value should suffice. Only set this setting if you want to restrict language selection to a subset of the Django-provided languages.  A list of authentication backend classes (as strings) to use when attempting to authenticate a user. A list of strings representing the host/domain names that this site can serve. This is a security measure to prevent HTTP Host header attacks, which are possible even under many seemingly-safe web server configurations. Values in this list can be fully qualified names (e.g. 'www.example.com'), in which case they will be matched against the request's Host header exactly (case-insensitive, not including port). A value beginning with a period can be used as a subdomain wildcard: '.example.com' will match example.com, www.example.com, and any other subdomain of example.com. A value of '*' will match anything; in this case you are responsible to provide your own validation of the Host header (perhaps in a middleware; if so this middleware must be listed first in MIDDLEWARE). A string representing the language code for this installation. This should be in standard language ID format. For example, U.S. English is "en-us". It serves two purposes: If the locale middleware isn't in use, it decides which translation is served to all users. If the locale middleware is active, it provides a fallback language in case the user's preferred language can't be determined or is not supported by the website. It also provides the fallback translation when a translation for a given literal doesn't exist for the user's preferred language. A string representing the time zone for this installation. Note that this isn't necessarily the time zone of the server. For example, one server may serve multiple Django-powered sites, each with a separate time zone setting. A tuple representing a HTTP header/value combination that signifies a request is secure. This controls the behavior of the request object’s is_secure() method. Warning: Modifying this setting can compromise your site’s security. Ensure you fully understand your setup before changing it. Default Default: '' (Empty string). Password to use for the SMTP server defined in EMAIL_HOST. This setting is used in conjunction with EMAIL_HOST_USER when authenticating to the SMTP server. If either of these settings is empty, Django won't attempt authentication. Default: '' (Empty string). Username to use for the SMTP server defined in EMAIL_HOST. If empty, Django won't attempt authentication. Default: '/accounts/login/' The URL where requests are redirected for login, especially when using the login_required() decorator. This setting also accepts named URL patterns which can be used to reduce configuration duplication since you don't have to define the URL in two places (settings and URLconf). Default: '/accounts/profile/' The URL where requests are redirected after login when the contrib.auth.login view gets no next parameter. This is used by the login_required() decorator, for example. This setting also accepts named URL patterns which can be used to reduce configuration duplication since you don't have to define the URL in two places (settings and URLconf). Default: 'django.contrib.sessions.backends.db'. Controls where Django stores session data. Default: 'django.core.mail.backends.smtp.EmailBackend'. The backend to use for sending emails. Default: 'localhost'. The host to use for sending email. Default: 'sessionid'. The name of the cookie to use for sessions.This can be whatever you want (as long as it's different from the other cookie names in your application). Default: 'webmaster@localhost' Default email address to use for various automated correspondence from the site manager(s). This doesn't include error messages sent to ADMINS and MANAGERS; for that, see SERVER_EMAIL. Default: 25. Port to use for the SMTP server defined in EMAIL_HOST. Default: 2621440 (i.e. 2.5 MB). The maximum size (in bytes) that an upload will be before it gets streamed to the file system. See Managing files for details. See also DATA_UPLOAD_MAX_MEMORY_SIZE. Default: 2621440 (i.e. 2.5 MB). The maximum size in bytes that a request body may be before a SuspiciousOperation (RequestDataTooBig) is raised. The check is done when accessing request.body or request.POST and is calculated against the total request size excluding any file upload data. You can set this to None to disable the check. Applications that are expected to receive unusually large form posts should tune this setting. The amount of request data is correlated to the amount of memory needed to process the request and populate the GET and POST dictionaries. Large requests could be used as a denial-of-service attack vector if left unchecked. Since web servers don't typically perform deep request inspection, it's not possible to perform a similar check at that level. See also FILE_UPLOAD_MAX_MEMORY_SIZE. Default: False. Whether to use a TLS (secure) connection when talking to the SMTP server. This is used for explicit TLS connections, generally on port 587. If you are experiencing hanging connections, see the implicit TLS setting EMAIL_USE_SSL. Default: False. Whether to use an implicit TLS (secure) connection when talking to the SMTP server. In most email documentation this type of TLS connection is referred to as SSL. It is generally used on port 465. If you are experiencing problems, see the explicit TLS setting EMAIL_USE_TLS. Note that EMAIL_USE_TLS/EMAIL_USE_SSL are mutually exclusive, so only set one of those settings to True. Default: None. Specifies a timeout in seconds for blocking operations like the connection attempt. Default: None. The URL where requests are redirected after a user logs out using LogoutView (if the view doesn't get a next_page argument). If None, no redirect will be performed and the logout view will be rendered. This setting also accepts named URL patterns which can be used to reduce configuration duplication since you don't have to define the URL in two places (settings and URLconf). Default: [] (Empty list). List of compiled regular expression objects representing User-Agent strings that are not allowed to visit any page, systemwide. Use this for bad robots/crawlers. This is only used if CommonMiddleware is installed (see Middleware). Django Edit Edit setting: %s Edit settings English Enter the new setting value. Is this settings being overridden by an environment variable? Name Namespace: %s, not found Namespaces Overridden Setting count Setting namespaces Setting updated successfully. Settings Settings in namespace: %s Settings inherited from an environment variable take precedence and cannot be changed in this view.  Settings updated, restart your installation and refresh your browser for changes to take effect. Smart settings The file storage engine to use when collecting static files with the collectstatic management command. A ready-to-use instance of the storage backend defined in this setting can be found at django.contrib.staticfiles.storage.staticfiles_storage. The full Python path of the WSGI application object that Django's built-in servers (e.g. runserver) will use. The django-admin startproject management command will create a simple wsgi.py file with an application callable in it, and point this setting to that application. The list of validators that are used to check the strength of user's passwords. URL to use when referring to static files located in STATIC_ROOT. Example: "/static/" or "http://static.example.com/" If not None, this will be used as the base path for asset definitions (the Media class) and the staticfiles app. It must end in a slash if set to a non-empty value. Value View settings Warning When set to True, if the request URL does not match any of the patterns in the URLconf and it doesn't end in a slash, an HTTP redirect is issued to the same URL with a slash appended. Note that the redirect may cause any data submitted in a POST request to be lost. The APPEND_SLASH setting is only used if CommonMiddleware is installed (see Middleware). See also PREPEND_WWW. Project-Id-Version: Mayan EDMS
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2023-01-05 02:55+0000
Last-Translator: Lyudmil Antonov <lantonov.here@gmail.com>, 2023
Language-Team: Bulgarian (https://app.transifex.com/rosarior/teams/13584/bg/)
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Language: bg
Plural-Forms: nplurals=2; plural=(n != 1);
 &quot;%s&quot; не е валиден запис. Булева стойност, която определя дали да се използва заглавката на X-Forwarded-Host за предпочитане пред заглавката на Host. Това трябва да бъде активирано само ако се използва прокси, който задава, че това заглавие се използва. Булева стойност, която определя дали да се използва заглавката на X-Forwarded-Port за предпочитане пред променливата SERVER_PORT META. Това трябва да бъде активирано само ако се използва прокси, който задава това заглавие. USE_X_FORWARDED_HOST има приоритет пред тази настройка. Речник, съдържащ настройките за всички бази данни, които ще се използват с Джанго. Това е вложен речник, чието съдържание пренася псевдоним в базата данни към речник, съдържащ опциите за отделна база данни. Настройката DATABASES трябва да конфигурира база данни по подразбиране; може да бъде посочен и всякакъв брой допълнителни бази данни. Списък на IP адреси като низове, който: Позволява на debug() контекст процесора да добави някои променливи към контекста на шаблона. Може да използва книжните маркери на admindocs, дори ако не е влязъл като потребител от персонала. Те са маркирани като &quot;вътрешни&quot; (за разлика от &quot;ВЪНШНИ&quot;) в имейлите на AdminEmailHandler. Списък на всички налични езици. Списъкът е списък с две двойки във формата (код на езика, име на език), например, („ja“, „японски“). Това определя кои езици са достъпни за избор на език. По принцип стойността по подразбиране трябва да е достатъчна. Задайте тази настройка само ако искате да ограничите избора на език до подмножество от предоставените от Джанго езици. Списък на резервни класове за удостоверяване (като низове), които да се използват при опит за удостоверяване на потребител. Списък с низове, представляващи имена на хост / домейн, които този сайт може да показва. Това е мярка за сигурност за предотвратяване на HTTP Host header атаки, които са възможни дори при на пръв поглед много безопасни конфигурации на уеб сървъра. Стойностите в този списък могат да бъдат напълно квалифицирани имена (напр. „www.example.com“), като в този случай те ще бъдат съпоставени точно със заглавката на хоста на заявката (нечувствителни към регистъра, без да включват порта). Стойност, започваща с точка, може да бъде използвана като заместващ поддомейн: „.example.com“ ще съответства на example.com, www.example.com и всеки друг поддомейн от example.com. Стойност &#39;*&#39; ще отговаря на всичко; в този случай вие сте отговорни да предоставите вашата собствена валидация на заглавката на хоста (може би в междинния софтуер; ако е така, този междинен софтуер трябва да бъде посочен първи в MIDDLEWARE). Низ, представляващ езиков код за тази инсталация. Това трябва да е в стандартен езиков ID формат. Например американският английски е „en-us“. Той служи за две цели: Ако междинният софтуер за локална мрежа не се използва, списъкът решава кой превод да служи на всички потребители. Ако междинният софтуер за локална мрежа е активен, той предоставя резервен език в случай, че предпочитаният език на потребителя не може да бъде определен или не се поддържа от уебсайта. Той също така осигурява резервен превод, когато превод за даден буква не съществува за предпочитания от потребителя език. Низ, представляващ часовата зона за тази инсталация. Обърнете внимание, че това не е непременно часовата зона на сървъра. Например един сървър може да обслужва множество сайтове, захранвани от Django, всеки с отделна настройка на часовата зона. Поредицата, представляваща комбинация от HTTP заглавка / стойност, която представлява заявка, е защитена. Това контролира поведението на метода is_secure () на обекта на заявка. Предупреждение: Промяната на тази настройка може да компрометира сигурността на вашия сайт. Уверете се, че напълно разбирате вашата настройка, преди да я промените. По подразбиране По подразбиране: &#39;&#39; (празен низ). Парола за SMTP сървър, дефиниран в EMAIL_HOST. Тази настройка се използва заедно с EMAIL_HOST_USER, когато се прави удостоверяване на SMTP сървъра. Ако някоя от тези настройки е празна, Django няма да прави опит за удостоверяване. По подразбиране: &#39;&#39; (празен низ). Потребителско име за SMTP сървър, дефиниран в EMAIL_HOST. Ако е празно, Django няма да прави опит за удостоверяване. По подразбиране: &#39;/accounts/login/&#39; URL адресът, при който заявките са пренасочени за вход, особено при използване на декоратора login_required(). Тази настройка приема също именувани модели на URL адреси, които могат да се използват за намаляване на дублирането на конфигурацията, тъй като не е необходимо да определяте URL адреса на две места (настройки и URLconf). По подразбиране:  '/accounts/profile/'; URL адресът, където заявките са пренасочени след влизане, когато изгледът contrib.auth.login не получи следващ параметър. Това се използва например от декоратора login_required(). Тази настройка приема и именувани модели на URL адреси, които могат да се използват за намаляване на дублирането на конфигурацията, тъй като не е необходимо да определяте URL адреса на две места (настройки и URLconf). По подразбиране: &#39;django.contrib.sesions.backends.db&#39;. Контролира къде Django съхранява данни от сесията. По подразбиране: &#39;django.core.mail.backends.smtp.EmailBackend&#39;. Бекенд, който да използвате за изпращане на имейли. По подразбиране: &#39;localhost&#39;. Хостът, който да използвате за изпращане на имейл. По подразбиране: &#39;sessionid&#39;. Името на бисквитката, която да използвате за сесии. Това може да бъде каквото искате (стига да е различно от другите имена на бисквитки във вашето приложение). По подразбиране: &#39;webmaster@localhost&#39; По подразбиране имейл адрес, който да се използва за различни автоматизирани кореспонденции от мениджъра(ите) на сайта. Това не включва съобщения за грешки, изпратени до ADMINS и MANAGERS; за това вижте SERVER_EMAIL. По подразбиране: 25. Порт, който да се използва за SMTP сървър, дефиниран в EMAIL_HOST. По подразбиране: 2621440 (т.е. 2,5 MB). Максималният размер (в байтове), който ще бъде качен, преди да бъде пуснат към файловата система. Вижте Управление на файлове за подробности. Вижте също DATA_UPLOAD_MAX_MEMORY_SIZE. По подразбиране: 2621440 (т.е. 2,5 MB). Максималният размер в байтове, който тялото на заявката може да бъде, преди да се повдигне SuspiciousOperation (RequestDataTooBig). Проверката се извършва при достъп до request.body или request.POST и се изчислява спрямо общия размер на заявката, с изключение на евентуални данни за качването на файлове. Можете да зададете това като None, за да деактивирате проверката. Приложенията, които се очаква да получават необичайно големи текстове във формуляра, трябва да настройват тази настройка. Количеството данни на заявката е свързано с обема памет, необходима за обработка на заявката и попълване на GET и POST речниците. Големите заявки могат да бъдат използвани като вектор за атака на отказ на услуга, ако се остави без отметка. Тъй като уеб сървърите обикновено не извършват дълбока проверка на заявката, не е възможно да се извърши подобна проверка на това ниво. Вижте също FILE_UPLOAD_MAX_MEMORY_SIZE. По подразбиране: Грешно. Дали да използвате TLS (сигурна) връзка, когато говорите със SMTP сървъра. Това се използва за изрични TLS връзки, обикновено на порт 587. Ако имате зависващи връзки, вижте неявната настройка на TLS EMAIL_USE_SSL. По подразбиране: Грешно. Дали да използвате неявна TLS (сигурна) връзка, когато говорите със SMTP сървъра. В повечето имейл документации този тип TLS връзка се нарича SSL. Обикновено се използва на порт 465. Ако имате проблеми, вижте изричната настройка на TLS EMAIL_USE_TLS. Обърнете внимание, че EMAIL_USE_TLS / EMAIL_USE_SSL са взаимно изключващи се, така че задайте само една от тези настройки като True. По подразбиране: Няма. Посочва изчакване в секунди за блокиране на операции като опит за свързване. По подразбиране: Няма. URL адресът, където заявките са пренасочени, след като потребителят излезе от LogoutView (ако изгледът не получи аргумент next_page). Ако е Няма, няма да се извърши пренасочване и изгледът ще се изведе. Тази настройка приема и именувани модели на URL адреси, които могат да се използват за намаляване на дублирането на конфигурацията, тъй като не е необходимо да определяте URL адреса на две места (настройки и URLconf). По подразбиране: [] (празен списък). Списък на компилирани обекти на регулярни изрази, представляващи низове на User-Agent, на които не е разрешено да посещават никоя страница в цялата система. Използвайте това за лоши роботи/пълзящи роботи . Това се използва само ако е инсталиран CommonMiddleware (вижте Middleware). Джанго Редактиране Редактиране на настройката: %s Редактиране на настройките Английски Въведете новата стойност на настройката. Отменя ли се тази настройка от променлива на средата? Име Именно пространство: %s, не е намерено Именни пространства Заменена Брой на настройките Задаване на именни пространства Настройката е актуализирана успешно. Настройки Настройки в именното пространството: %s Настройките, наследени от системна променлива имат предимство и не могат да бъдат променени в този изглед. Настройките са актуализирани, рестартирайте инсталацията и опреснете браузъра си, за да влязат в сила промените. Умни настройки Двигателят за съхранение на файлове, който да се използва при събиране на статични файлове с командата за управление collectstatic. Готов за използване екземпляр на резервния архив за съхранение, дефиниран в тази настройка, може да бъде намерен на django.contrib.staticfiles.storage.staticfiles_storage. Пълният Python път на обекта на приложението WSGI, който ще използва вградените сървъри на Django (например runserver). Командата за управление django-admin startproject ще създаде прост файл wsgi.py с приложение, което може да се извиква в него и ще насочи тази настройка към това приложение. Списък на валидаторите, които се използват за проверка на силата на паролите на потребителя. URL адрес, който да използвате, когато се позовавате на статични файлове, разположени в STATIC_ROOT. Пример: "/static/"; или "http://static.example.com/" Ако не е None, адресът ще бъде използвано като основен път за дефинициите на активите (клас Media) и приложението staticfiles. Трябва да завършва с наклонена черта, ако е зададен на непразна стойност. Стойност Преглед на настройките Предупреждение Когато е зададено като True, ако URL адресът на заявката не съвпада с който и да е от шаблоните в URLconf и не завършва с наклонена черта, HTTP пренасочване се издава на същия URL адрес с добавена наклонена черта. Имайте предвид, че пренасочването може да доведе до загуба на данни, изпратени в POST заявка. Настройката APPEND_SLASH се използва само ако е инсталиран CommonMiddleware (вижте Middleware). Вижте също PREPEND_WWW. 