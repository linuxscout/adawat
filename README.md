# Adawat: Arabic Language Toolkit

# مكتبة أدوات اللغة العربية
Adawat: Arabic Language Toolkit

![adawat logo](doc/adawat_header.png  "adawat logo")

![PyPI - Downloads](https://img.shields.io/pypi/dm/adawat)


  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com

  
Features |   value
---------|---------------------------------------------------------------------------------
Authors  | [Authors.md](https://github.com/linuxscout/adawat-arabic-syntax/master/AUTHORS.md)
Release  | 0.1
License  |[GPL](https://github.com/linuxscout/adawat-arabic-syntax/master/LICENSE)
Tracker  |[linuxscout/adawat/Issues](https://github.com/linuxscout/adawat-arabic-syntax/issues)
Source  |[Github](http://github.com/linuxscout/adawat-arabic-syntax)
Feedbacks  |[Comments](https://github.com/linuxscout/adawat-arabic-syntax/)
Accounts  |[@Twitter](https://twitter.com/linuxscout))

## Description

Adawat: Arabic Language Toolkit


###  مزايا:
 تجمع هذه المكتبة كل الأدوات المستعملة في معالجة النص العربي
 مثل:
 
 * التشكيل
  * تشكيل النص العربي، يستحسن استعمال مكتبة مشكال، أو برنامج مشكال

  * تشكيل مع اقتراحات تشكيلات أخرى لكل كلمة
  * اختزال الحركات من النص المشكول
  * إزالة التشكيل
  * مقارنة جملة مشكولة يدويا مع ما ينتج عن برنامج التشكيل
* وظائف التحويل
  * نقحرة النص العربي بحروف لاتينية
  * تعريب نص مكتوب بحروف لاتينية
  * قلب نص
  * تفقيط: تحويل عدد إلى نص
  * تنميط النص: توحيد الهمزات والألفات
  * فك تشابك الحروف العربية
* التحليل والتوليد
  * تحليل صرفي للنص
  * تفريق النص إلى كلمات وعلامات
  * تصنيف الكلمات إلى اسم وفعل وحرف
  * توليد كل الأشكال المختلفة للكلمة
* استخلاص
  * استخلاص المتلازمات اللفظية
  * كشف اللغات المختلفة
  * استخلاص المسميات
  * استخلاص العبارات العددية
* متفرقات
  * ضبط قصيدة شعرية عمودية
  * توليد نص عشوائي
## Features

* Tashkeel
  * tashkeel     : vocalize text, we recomand to use mishkal-console instead.
  * tashkeel    with suggestions for every word.
  * reduce       : strip unnecessary tashkeel from avocalized text 
  * strip        : remove all harakat and shadda
  * compare      : Compare Tashkeel between input text and the automatic vocalized text
* Transformation and Converion
  * romanize     : convert an arabic script text to latin representation
  * arabize      : convert an transliterated arabic script text to arabic
  * inverse      : inverse text
  * numbers to words     : convert numeric value to words
  * normalize    : normalize letters in arabic text
  * unshape      : unshape arabic letters
* Analysis and generation
  * stem         : morphology analysis of given texts 
  * tokenize     : tokenize a text to words
  * wordtag      : classify words into (nouns, verbs, stopwords)
  * affixate     : generate all word forms by affixation
* Extraction
  * collocation  : extract collocations from text 
  * language     : detect arabic and latin clauses in text
  * named        : extract named enteties from text
  * numbered     : extarct numbred clauses from text
* Divers
  * affixate     : generate all word forms by affixation
  * poetry       : format poetry texts to columns poetry
  * random       : get a random text

## Citation

```bibtex
@thesis{zerrouki2020adawat,
author = {Taha Zerrouki},
title = {Towards An Open Platform For Arabic Language Processing},
type = {PhD thesis},
institution = {Ecole Nationale Supérieure d'informatique, Alger, Algérie},
date = {2020},
}
```

### Usage

### install
```shell
pip install adawat
```

#### import
```python
>>> import adawat.adaat
```
## Examples

Detailed examples and features in [Features](doc/features.md) 

### Tashkeel
* tashkeel     : vocalize text, we recomand to use mishkal-console instead.
* tashkeel    with suggestions for every word.
* reduce       : strip unnecessary tashkeel from avocalized text 
* strip        : remove all harakat and shadda
* compare      : Compare Tashkeel between input text and the automatic vocalized text

```python
>>> lastmark = True
>>> text = u"تطلع الشمس صباحا"
>>> adawat.adaat.tashkeel_text(text, lastmark)
' تَطْلُعُ الشَّمْسُ صَبَاحًا'

```

#### [requirement]
```
asmai>=0.1
mishkal>=0.3
naftawayh>=0.4
pyarabic>=0.6.8
qalsadi>=0.3.6
repr>=0.3.1
spellcheck>=1.0.2
sylajone>=0.2
tashaphyne>=0.3.4.1
```

