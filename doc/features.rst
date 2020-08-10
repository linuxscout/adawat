Adawat: Arabic Language Toolkit
===============================

مكتبة أدوات اللغة العربية
=========================

Adawat: Arabic Language Toolkit

مزايا:
------

تجمع هذه المكتبة كل الأدوات المستعملة في معالجة النص العربي مثل:

-  التشكيل
    -  تشكيل النص العربي، يستحسن استعمال مكتبة مشكال، أو برنامج مشكال
    
    -  تشكيل مع اقتراحات تشكيلات أخرى لكل كلمة
    -  اختزال الحركات من النص المشكول
    -  إزالة التشكيل
    -  مقارنة جملة مشكولة يدويا مع ما ينتج عن برنامج التشكيل
-  وظائف التحويل
    -  نقحرة النص العربي بحروف لاتينية
    -  تعريب نص مكتوب بحروف لاتينية
    -  قلب نص
    -  تفقيط: تحويل عدد إلى نص
    -  تنميط النص: توحيد الهمزات والألفات
    -  فك تشابك الحروف العربية
-  التحليل والتوليد
    -  تحليل صرفي للنص
    -  تفريق النص إلى كلمات وعلامات
    -  تصنيف الكلمات إلى اسم وفعل وحرف
    -  توليد كل الأشكال المختلفة للكلمة
-  استخلاص
    -  استخلاص المتلازمات اللفظية
    -  كشف اللغات المختلفة
    -  استخلاص المسميات
    -  استخلاص العبارات العددية
-  متفرقات
    -  ضبط قصيدة شعرية عمودية
    -  توليد نص عشوائي 

Features
~~~~~~~~    
-  Tashkeel
    -  tashkeel : vocalize text, we recomand to use mishkal-console instead.
    -  tashkeel with suggestions for every word.
    -  reduce : strip unnecessary tashkeel from avocalized text
    -  strip : remove all harakat and shadda
    -  compare : Compare Tashkeel between input text and the automatic
       vocalized text
-  Transformation and Converion
-  romanize : convert an arabic script text to latin representation
    -  arabize : convert an transliterated arabic script text to arabic
    -  inverse : inverse text
    -  numbers to words : convert numeric value to words
    -  normalize : normalize letters in arabic text
    -  unshape : unshape arabic letters
-  Analysis and generation
    -  stem : morphology analysis of given texts
    -  tokenize : tokenize a text to words
    -  wordtag : classify words into (nouns, verbs, stopwords)
    -  affixate : generate all word forms by affixation
-  Extraction
    -  collocation : extract collocations from text
    -  language : detect arabic and latin clauses in text
    -  named : extract named enteties from text
    -  numbered : extarct numbred clauses from text
-  Divers
    -  affixate : generate all word forms by affixation
    -  poetry : format poetry texts to columns poetry
    -  random : get a random text
    
Usage
-----

install
-------

.. code:: shell

    pip install adawat

import
~~~~~~

.. code:: python

    >>> import adawat.adaat

Example
-------

Tashkeel
~~~~~~~~

-  tashkeel : vocalize text, we recomand to use mishkal-console instead.
-  tashkeel with suggestions for every word.
-  reduce : strip unnecessary tashkeel from avocalized text
-  strip : remove all harakat and shadda
-  compare : Compare Tashkeel between input text and the automatic
   vocalized text


-  tashkeel
   
  .. code:: python

    >>> lastmark = True
    >>> text = u"تطلع الشمس صباحا"
    >>> adawat.adaat.tashkeel_text(text, lastmark)
    ' تَطْلُعُ الشَّمْسُ صَبَاحًا'

-  Tashkeel with suggestions for every word

   .. code:: python

       ... lastmark = True
       >>> text = u"تطلع الشمس صباحا"
       >>> adawat.adaat.tashkeel2(text, lastmark)
       [{'link': '', 'suggest': 'تَطَلَّعَ;تَطَلَّعْ;تَطَلُّعٌ;تَطَلُّعٍ;تَطَلُّعَ;تَطَلُّعُ;تَطَلُّعِ;تَطَّلِعَ;تَطَّلِعُ;تَطَّلِعْ;تَطْلَعَ;تَطْلَعُ;تَطْلَعْ;تَطْلُعَ;تَطْلُعُ;تَطْلُعْ;تُطَلَّعَ;تُطَلَّعُ;تُطَلَّعْ;تُطَلِّعَ;تُطَلِّعُ;تُطَلِّعْ;تُطُلِّعَ;تُطَّلَعَ;تُطَّلَعُ;تُطَّلَعْ;تُطْلَعَ;تُطْلَعُ;تُطْلَعْ;تُطْلِعَ;تُطْلِعُ;تُطْلِعْ', 'inflect': '[V-1;F1H-faU;---]{فعل مرفوع}<br/>Verb:المضارع المعلوم:هي:y:T2G2N1', 'rule': 100, 'chosen': 'تَطْلُعُ', 'semi': 'تَطْلُع'}, {'link': ' 10علاقة فعل وفاعل', 'suggest': 'الشَّمِسَ;الشَّمِسُ;الشَّمِسِ;الشَّمْسَ;الشَّمْسُ;الشَّمْسِ;الشُّمُسَ;الشُّمُسُ;الشُّمُسِ', 'inflect': '[NJ-;------U;--L]{اسم مرفوع}<br/>Noun:جامد:تعريف:مرفوع:متحرك:ينون::T4G1N1', 'rule': 6, 'chosen': 'الشَّمْسُ', 'semi': 'الشَّمْس'}, {'link': '', 'suggest': 'صَبَاحًا;صَبَاحَا;صِبَاحًا;صِبَاحَا', 'inflect': '[NJ-;---E--A;---]{اسم منصوب}<br/>Noun:جامد:تنوين:تنوين الألف:منصوب:متحرك::T4G1N1', 'rule': 31, 'chosen': 'صَبَاحًا', 'semi': 'صَبَاحا'}]

-  CompareTashkeel 

   .. code:: python

       >>> text = u"تَطْلُعُ الشَّمْسُ   صَبَاحًا"
       >>> adawat.adaat.compare\_tashkeel(text)
        تَطْلُعُ الشَّمْسُ  صَبَاحًا [" Verb:المضارع المعلوم:هي:y:T2G2N1' link=''
        rule='100'>تَطْلُعُ Noun:جامد:تعريف:مرفوع:متحرك:ينون::T4G1N1' link='
        10علاقة فعل وفاعل' rule='6'>الشَّمْسُ Noun:جامد:تنوين:تنوين
        الألف:منصوب:متحرك::T4G1N1' link='' rule='31'>صَبَاحًا",
        'correct:100.00%, incorrect:0.00%']

-  Reduced Tashkeel

   .. code:: python
   
       >>> text = u"تَطْلُعُ الشَّمْسُ صَبَاحًا"
       >>> adawat.adaat.reduced\_tashkeel\_text(text) 'تطلُعُ الشّمسُ صباحًا'


-  Strip Harakat

  .. code:: python
  
       >>> text = u"تَطْلُعُ الشَّمْسُ صَبَاحًا"
       >>> adawat.adaat.araby.strip_tashkeel(text)
       'تطلع الشمس صباحا'

Transformation and Converion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  romanize : convert an arabic script text to latin representation
-  arabize : convert an transliterated arabic script text to arabic
-  inverse : inverse text
-  numbers to words : convert numeric value to words
-  normalize : normalize letters in arabic text
-  unshape : unshape arabic letters

-  Romanize

   .. code:: python

       >>> text = u"تَطْلُعُ الشَّمْسُ صَبَاحًا"
       >>> adawat.adaat.romanize(text)
       'taToluEu Al$~amosu SabaAHFA'

-  Arabize

   .. code:: python

       >>> text = 'taToluEu Al$~amosu SabaAHFA'
       >>> adawat.adaat.arabize(text)
       'تَطْلُعُ الشَّمْسُ صَبَاحًا'

-  Number To Words \`\`\`python

            text="2021" adawat.adaat.number2letters(text) 'ألفان و واحد
            و عشرون' \`\`\`

-  Normalize text

   .. code:: python

       ... text = "سؤال أحد الأئمة عن الإسلام"
       >>> adawat.adaat.normalize(text)
       'سءال احد الاءمه عن الاسلام'

-  Inverse

   .. code:: python

       >>> ####Inverse
       ... text = u"تطلع الشمس صباحا"
       >>> adawat.adaat.inverse(text)
       ['صباحا', 'الشمس', 'تطلع']

Analysis and generation
~~~~~~~~~~~~~~~~~~~~~~~

-  stem : morphology analysis of given texts
-  tokenize : tokenize a text to words
-  wordtag : classify words into (nouns, verbs, stopwords)
-  affixate : generate all word forms by affixation

-  Morphology analysis

   .. code:: python

       >>> text = u"تطلع الشمس صباحا"
       >>> lastmark = True
       >>> adawat.adaat.full_stemmer(text, lastmark)

-  Wordtag

   .. code:: python

       >>> text = u"تطلع الشمس صباحا"
       >>> adawat.adaat.wordtag(text)
       [{'tag': 'vn2', 'word': 'تطلع'}, {'tag': 'n', 'word': 'الشمس'}, {'tag': 'n', 'word': 'صباحا'}]

-  Tokenize

   .. code:: python

       >>> text = u"تطلع الشمس صباح"
       >>> adawat.adaat.token_text(text)
       ['تطلع', 'الشمس', 'صباح']

-  Affixate

   .. code:: python

       >>> word="شمس"
       >>> adawat.adaat.affixate(word)
       [{'affixed': 'شمسَ', 'standard': 'شمسَ'},
        {'affixed': 'شمسُ', 'standard': 'شمسُ'},
        {'affixed': 'شمسِ', 'standard': 'شمسِ'},
        {'affixed': 'ب-شمسِ', 'standard': 'بشمسِ'},
        {'affixed': 'ك-شمسِ', 'standard': 'كشمسِ'},
        {'affixed': 'ل-شمسِ', 'standard': 'لشمسِ'},
        {'affixed': 'و-شمسَ', 'standard': 'وشمسَ'},
       ...
       [dict length 456]

   .. rubric:: Extraction
      :name: extraction

-  collocation : extract collocations from text
-  language : detect arabic and latin clauses in text
-  named : extract named enteties from text
-  numbered : extarct numbred clauses from text

-  Language

   .. code:: python

       >>> text = u"""السلام عليكم how are you, لم اسمع أخبارك منذ مدة, where are you going"""
       >>> adawat.adaat.segment_language(text)
       [('arabic', 'السلام عليكم'), ('latin', ' how are you, '), ('arabic', 'لم اسمع أخبارك منذ مدة'), ('latin', ', where are you going')]

-  Random Text

   .. code:: python

       >>> adawat.adaat.random_text()
       'أضحى الشارع مزدحما .'
       >>> 

-  Collocations

   .. code:: python

       >>> text=u"""أمضى عمير بن سعد عاماً كاملاً في ولايته على حمص بالشام ، ولم تصل إلى عمر أية أخبار عنه طوال هذه المدة ، ولم يرسل عُمَير الخراج إليه ، ولا تصل عنه أية أنباء . فقال عمر لكاتبه : اكتب إلى عمير فإني أخاف أن يكون خاننا ، وأرسل إليه يستدعيه . 
       ... """
       >>> adawat.adaat.show_collocations(text)
       'أمضى عمير بن سعد عاماً كاملاً في ولايته على حمص بالشام ، ولم تصل إلى عمر أية أخبار عنه طوال هذه المدة ، ولم يرسل عُمَير الخراج إليه ، ولا تصل عنه أية أنباء . فقال عمر لكاتبه : اكتب إلى عمير فإني أخاف أن يكون خاننا ، وأرسل إليه يستدعيه .\n '

-  Extract enteties

   .. code:: python

       >>> text = u"""خَبَّرني ثُمامةُ عَن أمير المؤمنين المأمون أنَّه قال:  قالَ لي بختيشوع بن جبريل الطبيب: إنَّ الذُبابَ إذا دُلِك بِهِ مَوضِعُ لَسْعَةِ الدَّبورِ سَكَن. فَلَسَعَني دَبّورٌ، فَحَكَكتُ على مَوضِعِه أكثَرُ مِن عِشرينَ ذُبابةً فما سَكَن إلا في قَدْرِ الزمانِ الذي كان يسكُنُ فيه مِن غَيرِ عِلاج. فَلَمْ يَبقَ إلا أنْ يَقول بختيشوع: كان هذا الدّبور حتفاً قاضياً، ولولا هذا العلاجُ لَقَتَلك!  وكذلك الأطباءُ: إذا سَقَوا دواءً فَضرَّ، أو قطعوا عِرْقاً فضرّ، قالوا: أنت مع هذا العلاج الصَّوابِ تجِدُ ما تجد، فلولا ذلك العلاجُ كُنتَ الساعةَ في نَارِ جهنم!    
       ... """
       >>> adawat.adaat.extract_enteties(text)
       "خَبَّرني ثُمامةُ عَن <mark class='coll'> أَمِيرِ الْمُؤْمِنِينَ </mark> المأمون أنَّه قال : قالَ لي <mark class='named'> بختيشوع بْن جبريل </mark> الطبيب : إنَّ الذُبابَ إذا دُلِك بِهِ مَوضِعُ لَسْعَةِ الدَّبورِ سَكَن . فَلَسَعَني دَبّورٌ ، فَحَكَكتُ على مَوضِعِه أكثَرُ مِن <mark class='number'> عِشْرِينَ </mark> ذُبابةً فما سَكَن إلا في قَدْرِ الزمانِ الذي كان يسكُنُ فيه مِن غَيرِ عِلاج . فَلَمْ يَبقَ إلا أنْ يَقول بختيشوع : كان هذا الدّبور حتفاً قاضياً ، ولولا هذا العلاجُ لَقَتَلك ! وكذلك الأطباءُ : إذا سَقَوا دواءً فَضرَّ ، أو قطعوا عِرْقاً فضرّ ، قالوا : أنت مع هذا العلاج الصَّوابِ تجِدُ ما تجد ، فلولا ذلك العلاجُ كُنتَ الساعةَ في نَارِ جهنم !\n"

-  Extract Named Enteties

   .. code:: python

       >>> text = u"""خَبَّرني ثُمامةُ عَن أمير المؤمنين المأمون أنَّه قال:  قالَ لي بختيشوع بن جبريل الطبيب: إنَّ الذُبابَ إذا دُلِك بِهِ مَوضِعُ لَسْعَةِ الدَّبورِ سَكَن. فَلَسَعَني دَبّورٌ، فَحَكَكتُ على مَوضِعِه أكثَرُ مِن عِشرينَ ذُبابةً فما سَكَن إلا في قَدْرِ الزمانِ الذي كان يسكُنُ فيه مِن غَيرِ عِلاج. فَلَمْ يَبقَ إلا أنْ يَقول بختيشوع: كان هذا الدّبور حتفاً قاضياً، ولولا هذا العلاجُ لَقَتَلك!  وكذلك الأطباءُ: إذا سَقَوا دواءً فَضرَّ، أو قطعوا عِرْقاً فضرّ، قالوا: أنت مع هذا العلاج الصَّوابِ تجِدُ ما تجد، فلولا ذلك العلاجُ كُنتَ الساعةَ في نَارِ جهنم!    
       ... """
       >>> adawat.adaat.extractNamed(text)
       "خَبَّرني ثُمامةُ عَن أمير المؤمنين المأمون أنَّه قال : قالَ لي <mark class='named'>بختيشوع بن جبريل </mark>الطبيب : إنَّ الذُبابَ إذا دُلِك بِهِ مَوضِعُ لَسْعَةِ الدَّبورِ سَكَن . فَلَسَعَني دَبّورٌ ، فَحَكَكتُ على مَوضِعِه أكثَرُ مِن عِشرينَ ذُبابةً فما سَكَن إلا في قَدْرِ الزمانِ <mark class='named'>الذي </mark>كان يسكُنُ فيه مِن غَيرِ عِلاج . فَلَمْ يَبقَ إلا أنْ يَقول بختيشوع : كان هذا الدّبور حتفاً قاضياً ، ولولا هذا العلاجُ لَقَتَلك ! وكذلك الأطباءُ : إذا سَقَوا دواءً فَضرَّ ، أو قطعوا عِرْقاً فضرّ ، قالوا : أنت مع هذا العلاج الصَّوابِ تجِدُ ما تجد ، فلولا ذلك العلاجُ كُنتَ الساعةَ في نَارِ جهنم !\n "

-  Chunking

   .. code:: python

       >>> text=u"""أمضى عمير بن سعد عاماً كاملاً في ولايته على حمص بالشام ، ولم تصل إلى عمر أية أخبار عنه طوال هذه المدة ، ولم يرسل عُمَير الخراج إليه ، ولا تصل عنه أية أنباء . فقال عمر لكاتبه : اكتب إلى عمير فإني أخاف أن يكون خاننا ، وأرسل إليه يستدعيه . 
       ... """
       >>> adawat.adaat.chunksplit(text)
       ['أمضى عمير', 'بن سعد عاما كاملا', 'في ولايته', 'على حمص بالشام ،', '', 'ولم تصل', 'إلى عمر', 'أية أخبار', 'عنه طوال', 'هذه المدة ،', '', 'ولم يرسل عُمَير الخراج', 'إليه ،', '', 'ولا تصل', 'عنه', 'أية أنباء .', '', 'فقال عمر لكاتبه :', 'اكتب', 'إلى عمير', 'فإني أخاف', 'أن يكون خاننا ،', '', 'وأرسل', 'إليه يستدعيه .\n']

-  Extract numbered words

   .. code:: python

       >>> text = u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا"
       >>> adawat.adaat.extractNumbered(text)   
       "وجدت <mark class='number'>خمسمئة وثلاثة وعشرين </mark>دينارا فاشتريت <mark class='number'>ثلاثة عشر </mark>دفترا "

-  Extract bigrams 

   .. code:: python

      >>> text = u"تطلع الشمس صباحا"
      >>>
       adawat.adaat.bigrams(text) ['الشمس صباحا 1', 'تطلع الشمس 1'] >>>


Divers
~~~~~~
-  poetry : format poetry texts to columns poetry
-  random : get a random text

-  Poetry

   .. code:: python

       >>> text = u"""يا لائِمي في الهَوى العُذريّ مَعذِرَةً \t مِنّي إليكَ و لَو أَنصَفتَ لَم تَلُمِ
       ... مَحَّضتَني النُّصحَ لكن لَستُ اسمَعُهُ \t إنَّ المُحِبَّ عَن العُذّالِ في صَمَمِ
       ... أمِنْ تَذَكُّرِ جِيرانٍ بِذي سَلَمٍ \t مَزجْتَ دَمعاً جَرَى مِن مُقلَةٍ بِدَمِ"""
       >>> adawat.adaat.justify_poetry(text)
       [['يا لائِمي في الهَوى العُذريّ مَعذِرَةً ', ' مِنّي إليكَ و لَو أَنصَفتَ لَم تَلُمِ'], ['مَحَّضتَني النُّصحَ لكن لَستُ اسمَعُهُ ', ' إنَّ المُحِبَّ عَن العُذّالِ في صَمَمِ'], ['أمِنْ تَذَكُّرِ جِيرانٍ بِذي سَلَمٍ ', ' مَزجْتَ دَمعاً جَرَى مِن مُقلَةٍ بِدَمِ']]

-  RandomText

   .. code:: python

       >>> adawat.adaat.random_text()
       'أضحى الشارع مزدحما .'
       >>> 

   .. rubric:: [requirement]
      :name: requirement

-  asmai>=0.1
-  mishkal>=0.3
-  naftawayh>=0.4
-  pyarabic>=0.6.8
-  qalsadi>=0.3.6
-  repr>=0.3.1
-  spellcheck>=1.0.2
-  sylajone>=0.2
-  tashaphyne>=0.3.4.1
