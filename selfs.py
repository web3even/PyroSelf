3
� Q^DP  �               @   s
  d dl mZmZmZmZmZ d dlmZmZ d dl	m
Z
 d dlZd dlZd dlZd dlZd dlZd dl	Z	d dlZd dlZd dlZd dlZd dlmZ d dlmZ d dlmZ d dlT d d	lmZ d d
lmZ e� Zejd�r�ejd� nRed�Zed�Z ed�Z!ed�Z"ee e!e"d�ed< e#dd��Z$ej%e$� W dQ R X ed d Zed d Z ed d Z"dRZ&dZ'edee �Z(e	j
dddddd�Z)e*ed d!�� dZ+ej,� Z-ej,� Z.e.e- j/d" Z0d#d$d%d&d'd(d)d*d+d,d-d.j1e0�gZ2d/d0� Z3d1d2� Z4d3d4� Z5d5d6� Z6d7d8� Z7e(j8ej9ej:e'�@ �d9d:� �Z;e(j8ej<d;d<�ej=@ �d=d;� �Z>e(j8ej<d>d<�ej=@ �d?d@� �Z?e(j8ej<dAd<�ej=@ �dBdC� �Z@e(j8ej<dDd<�ej=@ �dEdF� �ZAe(j8ej9ddG�dHdI� �ZBe(j8ej9dJdG�dKdL� �ZCe(j8ej<dMd<�ej=@ �dNdO� �ZDe(j8� dPdQ� �ZEe(jF�  dS )S�    )�Client�Message�Filters�Chat�InputPhoneContact)�	functions�types)�StrictRedisN)�path)�sleep)�datetime)�*)�ConfigParser)�coloredz./config.iniz
config.inizPlease Send Api-Id : zPlease Send Api-Hash : zPlease Send User-Id Sudo : zPlease Send User-Id log : )�api_id�api_hash�sudo�gplogz	Pyro-Self�wr   r   r   �&https://github.com/attavakoli/PyroSelf�masteri(� Z	localhosti�  �   zUTF-8T)�hostZportZdb�charsetZdecode_responsesu�  
░█▀▀█ ─▀─ █▀▀▄ ─▀─ ░█▀▀█ █▀▀ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀█ █▀▄▀█
░█▄▄█ ▀█▀ █──█ ▀█▀ ░█─▄▄ █▀▀ █▄▄▀ ─░█── █▀▀ █▄▄█ █─▀─█
░█─── ▀▀▀ ▀──▀ ▀▀▀ ░█▄▄█ ▀▀▀ ▀─▀▀ ─░█── ▀▀▀ ▀──▀ ▀───▀
Dev : @Sigris & @Salazar
Zredi�  z           %00u   █          %10u   ██         %20u   ███        %30u   ████       %40u   █████      %50u   ██████     %60u   ███████    %70u   ████████   %80u    █████████  %90u#   ██████████ %100z~ Reloaded! {} msc             C   s*   t d d jd�}t| �|kr"dS dS d S )Nz	Pyro-Selfr   �,TF)�config�split�str)�user_idZ
sudo_users� r   �self.py�SUDO<   s    r!   c             C   s    d}t jdt| � |�rd}|S )NFzself:muteallT)�database�	sismemberr   )�chat_idr   �varr   r   r    �muteallC   s    r&   c             C   s"   g }x| D ]}|j |j� q
W |S )N)�append�
message_id)Zmsg_listZlist_ids�msgr   r   r    �get_idsI   s    
r*   c             C   s   | j ||� d S )N)�delete_messages)�appr$   Zmsg_idsr   r   r    �delmsgO   s    r-   c             C   s|   | j dd�} | j dd�} | j dd�} | j dd�} | j d	d
�} | j dd�} | j dd�} | j dd�} | j dd�} | j dd�} | S )N�0u   0️⃣�1u   1️⃣�2u   2️⃣�3u   3️⃣�4u   4️⃣�5u   5️⃣�6u   6️⃣�7u   7️⃣�8u   8️⃣�9u   9️⃣)�replace)r)   r   r   r    �	number_toR   s    r9   c             C   s   t |� d S )N)�print)�client�messager   r   r    �pv_telegram_   s    r=   �upgrade� c             C   s�   |j d�}tjd� tjd� tjd� |j d� tjd� tjd�j� }|d }|j d	|� �� tjd
� tj	t
jt
jft
j��  t`d S )Nz~ Updating robot please wait...z
./selfs.py�   z$wget http://piniger.ml/self/selfs.pyz~ Applying update changes...�   z http://piniger.ml/self/txtup.phpZResultzf~ The latest version of gitHub has been downloaded and implemented and the robot is ready to work! 

 r   )�edit�os�remove�timer   �popen�requests�get�json�execl�sys�
executable�argv�	threadingZThread)r;   r<   �arH   Zverr   r   r    r>   c   s    






Zsetnamec             C   sH   t tj� k rDdj|jdd � �}tjtjj|d�� |j	dj
|�� d S )N� r   )�
first_namez*~ Name changed succesfully! 

 ~ name : {})�	sleeptimerE   �join�commandr,   �sendr   �account�UpdateProfilerB   �format)r;   r<   �namer   r   r    �set_namer   s    rZ   Zsetprofc             C   s<   |j r|j j� }n|j� }tj|� |jd� tj|� d S )Nz"~ Profile Picture Set Succesfully!)�reply_to_message�downloadr,   Zset_profile_photorB   rC   rD   )r;   r<   �picr   r   r    �set_profile_picy   s    

r^   Zsetbioc             C   s`   t tj� k r\dj|jdd � �}t|�dkr8|jd� n$| jtjj	|d�� |jdj
|�� d S )NrP   r   �F   z%~ Bio too long maximum 70 characters!)Zaboutz(~ Bio succesfully changed! 

 ~ bio : {})rR   rE   rS   rT   �lenrB   rU   r   rV   rW   rX   )r;   r<   Zbior   r   r    �set_bio�   s    ra   )�groupc          	   C   sh   yNt j� }|j}tjd�}|dkrL|dkrLtjd�p6d}t j|jj|� qLn W n   td� Y nX d S )Nzmonshi-mode�offline�onz
self:mtextz*User is offline please send message later!rP   )	r,   �get_me�statusr"   rH   �send_message�chat�idr:   )r;   r<   �merf   �monshi�txtr   r   r    rc   �   s    
rc   r@   c             C   s$   t jd�}|dkr tj|jj� d S )Nzself:markreadallrd   )r"   rH   r,   Zread_historyrh   ri   )r;   r<   �markreadr   r   r    rm   �   s    
rm   Zecoec             C   s|   ybd}|j jdd�d }|jd�}x<|D ]4}||7 }|jd|� d��}|jd|j� � d��}q(W W n   td� Y nX d S )Nr?   rP   r   z`|`�`z|`)�textr   rB   �stripr:   )r;   r<   Zchrl   Zms�ir   r   r    ro   �   s    

ro   c          �  C   s:  y4t jd|jj�r2|jdkr2t|jj�s2|jd� W n4 tk
rh } zt	j
tdj|�� W Y d d }~X nX y(t jd|jj�r�|r�t	j|jjd� W n4 tk
r� } zt	j
tdj|�� W Y d d }~X nX yT|jdk�rt	j|jjdd	�d
 }t	j|jj|j|jdj|jj|jj|jj�� W n6 tk
�rR } zt	j
tdj|�� W Y d d }~X nX y|jdk�rl|jd� W n6 tk
�r� } zt	j
tdj|�� W Y d d }~X nX t|jj��r�|jdk�r�|j�r�|j�  |jj� }t	jt|� tj|� yB|jdk�r0|j�r0|jjj}|jdj|�� t	j|jj|� W n6 tk
�rh } zt	j
tdj|�� W Y d d }~X nX y<|jdk�r�|j�r�|jjj}t	j|� |jdj|�� W n6 tk
�r� } zt	j
tdj|�� W Y d d }~X nX y<|jdk�r|j�r|jjj}t	j|� |jdj|�� W n6 tk
�rP } zt	j
tdj|�� W Y d d }~X nX yN|jdk�r�x"tD ]}t	j|jj|j|� �qfW t j!}tj"||ft j#��  W n6 tk
�r� } zt	j
tdj|�� W Y d d }~X nX yJ|jdk�r |j�r |jjj}|jdj|�� t j$dt%|jj� |� W n6 tk
�rX } zt	j
tdj|�� W Y d d }~X nX yJ|jd k�r�|j�r�|jjj}|jd!j|�� t j&dt%|jj� |� W n6 tk
�r� } zt	j
td"j|�� W Y d d }~X nX y�|jd#k�r\t j'dt%|jj� �t(d
�k�r|jd$� nFd%}x0t j)dt%|jj� �D ]}|d&j||�7 }�q2W |j|d'd(d)� W n6 tk
�r� } zt	j
td*j|�� W Y d d }~X nX y�|j�rHt*j+d+|j��rH|jj,dd,�}	t(|	�}|jjj}t jdt%|jj� |��r�|jd-� nR|jd.j||	�� t j$dt%|jj� |� |d/ }
t-|
� t j&dt%|jj� |� W n6 tk
�r� } zt	j
td0j|�� W Y d d }~X nX yL|jd1k�r�t j.d2�d3k�r�t j/d2d4� d5}	nt j/d2d3� d6}	|j|	� W n6 tk
�r } zt	j
td7j|�� W Y d d }~X nX yF|j�rJt*j+d8|j��rJ|jj,d9d,�}	|jd:j|	�� t j/d;|	� W n6 tk
�r� } zt	j
td<j|�� W Y d d }~X nX y$|jd=k�r�|jd>� t jd;� W n6 tk
�r� } zt	j
td?j|�� W Y d d }~X nX y(|jd@k�r|jdA� t	j0|jj� W n6 tk
�r> } zt	j
tdBj|�� W Y d d }~X nX yH|jdCk�r�t jd|jj��rl|jdD� n|jdE� t j$d|jj� W n6 tk
�r� } zt	j
tdFj|�� W Y d d }~X nX y*|jdGk�r�|jdH� t j&d|jj� W n6 tk
�	r  } zt	j
tdIj|�� W Y d d }~X nX y&|jdJk�	s<|jdKk�	rF|jdL� W n6 tk
�	r~ } zt	j
tdMj|�� W Y d d }~X nX y�|j�
r@t*j+dN|j��
r@|jj,dNd,�}	|jdO� t-dP� |jdQ� t-dP� |jdR� t-dP� |jdS� t-dP� |jdT� t-dP� dU}x8|	D ]0}t1t%|��}|dVj|�7 }|jdWj|�� �
qW W n6 tk
�
rx } zt	j
tdXj|�� W Y d d }~X nX y(|jdYk�
r�t	j2� }|jdZj|�� W n6 tk
�
r� } zt	j
td[j|�� W Y d d }~X nX y8|jd\k�r|j�rt	j3|jjj�}|jdZj|�� W n6 tk
�rH } zt	j
td]j|�� W Y d d }~X nX yT|jd^k�sd|jd_k�r�|jj}t	j2� }t	j4|jj|j� t	j5|jj|j6|j� W n6 tk
�r� } zt	j
td`j|�� W Y d d }~X nX y�|jdak�rxt	j7|jj�}|db } x<t8| �D ]0}t9t	|jjt:t	j;|jjdb��� t<j-dc� �qW t9t	|jjt:t	j;|jj|| db  ��� |j�  t	j
|jjdd� W n6 tk
�r� } zt	j
tdej|�� W Y d d }~X nX yF|jdfk�r�t=j>� }t?j@� }|jdgj|jA|jB|jC|jD|jE|jF�� W n6 tk
�r. } zt	j
tdhj|�� W Y d d }~X nX yH|jdik�rvt jd|jj��r\|jdj� n|jdk� t j$d|jj� W n6 tk
�r� } zt	j
tdlj|�� W Y d d }~X nX y*|jdmk�r�|jdn� t j&d|jj� W n6 tk
�r } zt	j
tdoj|�� W Y d d }~X nX y6|jdpk�rF|j�rF|jdq� t	jG|jj|jj� W n6 tk
�r~ } zt	j
tdrj|�� W Y d d }~X nX y�|jdsk�s�|jdtk�r>t	j2� }t jd|jj��r�du}ndv}t jd|jj��r�du}ndv}t jdw|j��r�du}ndv}t j.d2�d3k�r
du}ndv}|jdxj|j|j|j||||t j)d;��p8dy�� W n6 tk
�rv } zt	j
tdhj|�� W Y d d }~X nX y(|jdzk�r�t j/dwd3��r�|jd{� W n6 tk
�r� } zt	j
td|j|�� W Y d d }~X nX y&|jd}k�r�|jd~� t j/dwd4� W n6 tk
�r4 } zt	j
tdj|�� W Y d d }~X nX yf|jd�k�sP|jd�k�r�|jj}|j�r�|j|jj|jd�� t	jHtIt%|jjJj6�t%|jjJj��g� W n6 tk
�r� } zt	j
td�j|�� W Y d d }~X nX y*tK|jj|jj��r�t	j4|jj|j� W n6 tk
�r4 } zt	j
td�j|�� W Y d d }~X nX d S )�Nz
self:pokeru   😐z #self 
 #poker 
 {}zself:typingZtypingz #self 
 #typing action 
 {}ri   r   )�limitr   uo   ایدی عددی شما : [ {} ] 
 
 نام اکانت شما : [ {} ] 
 
 نام کاربری شما: [ @{} ]z #self 
 #id 
 {}�selfz.Hi 
 I Am Alireza 
 this Is my Self 
 @Salazarz #self 
 #information : 
 {}zp i cZkickz ~ User {} Kicked This Chat!z #self 
 #kick : 
 {}�blockz ~ User {} Blocked!z #self 
 #block : 
 {}Zunblockz ~ User {} Unblocked!z #self 
 #unblock : 
 {}�reloadz #self 
 #reload : 
 {}Zmutez+ ~ User {} Added Too The Mute List On Self!zself:muteallz #self 
 #mute : 
 {}Zunmutez) ~ User {} Removed The Mute List On Self!z #self 
 #unmute : 
 {}Zmutelistz~ Mute List Is Empty!z~ Mute List: 
z2 ------ <a href='tg://user?id={}'>{}</a> ------ 
 ZHTMLT)Z
parse_modeZdisable_web_page_previewz #self 
 #mutelist : 
 {}zmute r?   z(~ This User is already in the Mute list!z6~ User [ {} ] Added To The Mutelist For [ {} ] Minute!�<   z #self 
 #mute min : 
 {}rk   zmonshi-moderd   Zoffz~ Self Monshi Is Off!z~ Self Monshi Is On!z #self 
 #monshi off : 
 {}z
setmonshi Z	setmonshiz~ Text [ {} ] Seted For Monshi!z
self:mtextz #self 
 #monshitext : 
 {}Zcleanmonshitextz~ Monshi Text Is Deleted!z  #self 
 #cleanmonshitext : 
 {}Zleavez~ Bye!z #self 
 #leave : 
 {}zpoker onz~ Poker Mode Already On!z~ Poker Mode Is Activited!z #self 
 #poker on : 
 {}z	poker offz~ Poker Mode Is Deactived!z #self 
 #poker off : 
 {}ZHelp�helpu>
  ~ GIOUTiN Self Help:


 [ self ]
 اطلاعات سورس!

 [ stats ]
اطلاعات سلف شما!

 [ kick ]
!  اخراج کردن فرد در صورت داشتن مجوز (در سوپر گروه ها)

 [ block | unblock ]
 بلاک کردن و آنبلاک کردن افراد!

 [ reload ]
 ریلود و چک کردن سورس!

 [ mute | unmute ]
 افزودن فرد درون لیست سکوت (در سوپر گروه ها)!

 [ mutelist ]
 به دست آوردن لیست افراد سکوت شده در آن گروه!

 [ mute زمان ]
 به جای "زمان" میتوانید مقدار دقیقه ای که میخواهید فرد در سکوت باشد را قرار دهید!


 [ Share ]
 به اشتراک گذاشتن شماره شما!

 [ Addc ]
 اضافه شدن شماره به مخاطبین!

 [ setprof ]
 قرار دادن عکس بر روی پروفایل با ریپلی!


 [ monshi ]
 خاموش|روشن کردن حالت منشی

 [ setmonshi متن|cleanmonshitext ]
 قرار دادن| پاک کردن متن منشی (به جای کلمه "متن" متن منشی خود را جایگذاری کنید)!


 [ id ]
 به دست آوردن اطلاعات خود!

 [ markreadall on|markreadall off ]
 فعال کردن و غیرفعال کردن تیک دوم داخل پیوی!

 [ cleanmsgs ]
 پاکسازی پیام های گروه!

 [ typing on|typing off ]
  فعال کردن و غیر فعال کردن تایپینگ!

 [ poker on|poker off ]
 فعال کردن و غیر فعال کردن حالت پوکر!

 [ leave ]
 خروج از گروه!

 [ pin ]
 سنجاق کردن پیام در یک گروه!

 [ time ]
 نشان دادن ساعت!

[ setbio متن ]
تغییر دادن بیو! به جای "متن" بیو جدید خود را بزارید!

[ setname اسم ]
برای تغیر دادن اسمتون کافیه به جای "اسم" اسم جدیدتونو جایگزین کنید!

[ p i c ]
میتونید بر روی یه عکس که به صورت تایمر دار ارسال شده ریپلی کنید و این دستور رو به کار ببرید ، بعدش اون عکس بدون تایم داخل پیوی خودتون از طرف سلف فرستاده میشه!

[ ecoe متن]
متنی ک جلوی این دستور جایگزین میکنین به صورت ادیت مسیج نشون داده میشه!

[ upgrade ]
هروقت
@Salazar و   @Sigaris
خبر از آپدیت دادن میتونید با این دستور سلفتون رو به اخرین نسخه بروز کنید!

~ Coder : @Salazar & @Sigaris
~ Ch : @Pinigerteam & @GIOUTiN
z #self 
 #Help : 
 {}zincode u   ~ Your String Is Incoding 🌑r@   u   ~ Your String Is Incoding 🌒u   ~ Your String Is Incoding 🌓u   ~ Your String Is Incoding 🌔u   ~ Your String Is Incoding 🌕z~ Your String Is Incoded : 
 z{}	z{}z #self 
 #incoding : 
 {}Zgetmez~ This is Answer : 
 
 {}z #self 
 #GetMe : 
 {}Zgetuserz #self 
 #Getuser : 
 {}ZshareZSharez #self 
 #share : 
 {}Z	cleanmsgs�c   g333333�?z~ All Chats Cleared!z #self 
 #cleanmsgs : 
 {}rE   z�~ Time : [ {}:{}:{} ] 
 ~ Year: [ {} ] 
 ~ Month : [ {} ] 
 ~ Day : [ {} ] 
 
 ~ Coder: @Salazar 
 ~ Channel : @GIOUTiN & @Pinigerteamz #self 
 #session : 
 {}z	typing onz~ Typing Action Is Already On!z"~ Typing Action Activited This Gp!z! #self 
 #typing on one gp : 
 {}z
typing offz%~ Typing Action Is Deactived This Gp!z" #self 
 #typing off one gp : 
 {}Zpinz~ This Message Is Pinned!z #self 
 #pin : 
 {}ZstatsZStatsu   ✔️u   ❌zself:markreadalluG  ~ Your Account Information: 
 
 
 • Name: [ {} ] 
 
 • Username: [ {} ] 
 
 • Userid: [ {} ] 
 
 • Typing In This Gp: [ {} ] 
 
 • Poker In This Gp: [ {} ] 
 
 • Markread In All Spgs & PV: [ {} ] 
 
 • Monshi Action: [ {} ] 
 
 • Monshi Text: [ {} ] 
 
 
 ~ Coder: @Salazar 
 ~ Channel : @GIOUTiN & @Pinigerteamz*User is offline please send message later!zmarkreadall onz~ Markread All Is Activited!z #self 
 #markreadall on : 
 {}zmarkreadall offz~ Markread All Is Deactived!z  #self 
 #markreadall off : 
 {}ZaddcZAddcz!~ This Number Added Too Contacts!z #self 
 #addcontact : 
 {}z #self 
 #delmute : 
 {})Lr"   r#   rh   ri   ro   r!   Z	from_userZ
reply_text�	Exceptionr,   rg   r   rX   Zsend_chat_actionZget_profile_photosZ
send_photoZfile_idZfile_refrQ   Zusernamer[   �deleter\   rC   rD   rB   Zkick_chat_memberZ
block_userZunblock_user�reloadlZedit_message_textr(   rK   rL   rJ   rM   Zsaddr   ZsremZscard�intZsmembers�re�searchr8   r   rH   �setZ
leave_chat�ordre   Z	get_usersr+   Zsend_contactZphone_numberZget_history_count�ranger-   r*   Zget_historyrE   r   �nowZ
JalaliDateZtodayZhourZminute�secondZyearZmonthZdayZpin_chat_messageZadd_contactsr   Zcontactr&   )�cr<   �er]   Zidsrq   �pythonro   �allrl   �min�bZmy�userZmyidZall_msgZtmZjdate�typZpkrZmrkallZmnshr   r   r    �cmd�   s(   
$$2$$


$

$

$
$
$
$ $
$$$
$
$
$
$X
$





$$$$ ($*$
$
$
$4$$
$*$r�   )r   r   )GZpyrogramr   r   r   r   r   Zpyrogram.apir   r   Zredisr	   rC   rK   rG   r}   rE   �
subprocessrN   rI   r
   r   r   Zkhayyam�configparserr   Z	termcolorr   r   �isfile�read�inputr   r   r   r   �openZ
configfile�writeZgitpullZtelegramr,   r"   r:   rR   r�   Z	starttimeZendtimeZmicrosecondsZmstimerX   r{   r!   r&   r*   r-   r9   Z
on_messageZprivater�   r=   rT   rj   r>   rZ   r^   ra   rc   rm   ro   r�   Zrunr   r   r   r    �<module>   s�   P

   
 
    +