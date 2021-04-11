# individual-project-2-njamalii
individual-project-2-njamalii created by GitHub Classroom
# پروژه دوم - جیمز باند


### کتابخانه های استفاده شده
1) time --> برای محاسبه زمان اجرا
2) json --> برای خواندن دیتا از فایل کلمات انگلیسی
3) redis --> برای برقراری ارتباط با دیتابیس ردیس در پایتون

## وصل شدن به دیتابیس
`redis_connection = redis.Redis('localhost')`
با استفاده از کتابخانه ردیس در پایتون یک کانکشن با دیتابیس ردیس در لوکال هاست برقرار می کنیم

## انتقال کلمات انگلیسی به دیتابیس از فایل جیسون

    with open('words_dictionary.json') as json_file:  
	    words_dictionary = json.load(json_file) 
    redis_connection.mset(words_dictionary)
 با استفاده از متود داخلی پایتون قایل جیسون را در متغیر ریخته و سپس با استفاده از کانکشن ردیس دیتا ها را مستقیم به دیتابیس انتقال میدهیم


## چک کردن کلمات

    def valid(string: str) -> bool:   
    if redis_connection.exists(string.lower()) == 0:  
        return False  
	 else:  
	    meaning_full_words.append(string)  
	    return True
با استفاده از متود بالا میتوانیم کلمات را به این متود پاس داده و پس از جست و جو آن در دیتابیس نتیجه را دریافت کنیم

  
  ## ارسال کلمات به متود valid

    for i in range(0, len(user_text)):  
    temp = []  
    for j in range(0, len(user_text) + 2):  
        temp = []  
        valid(''.join(temp))  
        if len(temp) == i:  
            valid(''.join(temp))  
        else:  
            temp.append(user_text[i-1:j])  
            valid(''.join(temp))

در آخر با استفاده از دو حلقه تو در تو تمامی حروف و حالت های امتحانی کلمات را از متن استخراج کرده و آن ها را جهت چک کردن به متود بالا ارسال میکنیم و در صورتی که کلمه انگلیسی باشد آن را به متغیر اضافه میکنیم



> `meaning_full_words = list(set(meaning_full_words))` حذف کلمات تکراری 
