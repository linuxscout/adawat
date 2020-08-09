#!/usr/bin/python
# -*- coding=UTF-8 -*-
import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '../')) # used for core
import adawat.adaat

text = u"تطلع الشمس صباحا"
####TashkeelText
lastmark = True
text = u"تطلع الشمس صباحا"
adawat.adaat.tashkeel_text(text, lastmark)
####Tashkeel2
lastmark = True
text = u"تطلع الشمس صباحا"
adawat.adaat.tashkeel2(text, lastmark)
####SpellCheck
# lastmark= options.get('lastmark', "0")
#~ text = u"تطلع الشمسس"
#~ adawat.adaat.spellcheck(text)
####CompareTashkeel
text = u"تَطْلُعُ الشَّمْسُ صَبَاحًا"
adawat.adaat.compare_tashkeel(text)
####ReduceTashkeel
text = u"تَطْلُعُ الشَّمْسُ صَبَاحًا"
adawat.adaat.reduced_tashkeel_text(text)
####StripHarakat
text = u"تَطْلُعُ الشَّمْسُ صَبَاحًا"
adawat.adaat.araby.strip_tashkeel(text)
####Romanize
text = u"تَطْلُعُ الشَّمْسُ صَبَاحًا"
adawat.adaat.romanize(text)
text = u"تَطْلُعُ الشَّمْسُ صَبَاحًا"
adawat.adaat.arabize(text)
####NumberToLetters
text="2021"
adawat.adaat.number2letters(text)
####LightStemmer
text = u"تطلع الشمس صباحا"
lastmark = True
adawat.adaat.full_stemmer(text, lastmark)
####Tokenize
text = u"تطلع الشمس صباح"
adawat.adaat.tokenize(text)
####Poetry
text = u"""يا لائِمي في الهَوى العُذريّ مَعذِرَةً \t مِنّي إليكَ و لَو أَنصَفتَ لَم تَلُمِ
مَحَّضتَني النُّصحَ لكن لَستُ اسمَعُهُ \t إنَّ المُحِبَّ عَن العُذّالِ في صَمَمِ
أمِنْ تَذَكُّرِ جِيرانٍ بِذي سَلَمٍ \t مَزجْتَ دَمعاً جَرَى مِن مُقلَةٍ بِدَمِ"""
adawat.adaat.justify_poetry(text)
####Unshape
adawat.adaat.pyarabic.unshape.unshaping_text(text)
####Affixate
word="شمس"
adawat.adaat.affixate(word)
####Normalize
text = "سؤال أحد الأئمة عن الإسلام"
adawat.adaat.normalize(text)
####Wordtag
text = u"تطلع الشمس صباحا"
adawat.adaat.wordtag(text)
####Inverse
text = u"تطلع الشمس صباحا"
adawat.adaat.inverse(text)
####Language
text = u"""السلام عليكم how are you, لم اسمع أخبارك منذ مدة, where are you going"""
adawat.adaat.segment_language(text)
####RandomText
adawat.adaat.random_text()
####showCollocations
text=u"""أمضى عمير بن سعد عاماً كاملاً في ولايته على حمص بالشام ، ولم تصل إلى عمر أية أخبار عنه طوال هذه المدة ، ولم يرسل عُمَير الخراج إليه ، ولا تصل عنه أية أنباء . فقال عمر لكاتبه : اكتب إلى عمير فإني أخاف أن يكون خاننا ، وأرسل إليه يستدعيه . 
"""
adawat.adaat.show_collocations(text)
####extractEnteties
text = u"""خَبَّرني ثُمامةُ عَن أمير المؤمنين المأمون أنَّه قال:‏ ‏ قالَ لي بختيشوع بن جبريل الطبيب: إنَّ الذُبابَ إذا دُلِك بِهِ مَوضِعُ لَسْعَةِ الدَّبورِ سَكَن. فَلَسَعَني دَبّورٌ، فَحَكَكتُ على مَوضِعِه أكثَرُ مِن عِشرينَ ذُبابةً فما سَكَن إلا في قَدْرِ الزمانِ الذي كان يسكُنُ فيه مِن غَيرِ عِلاج. فَلَمْ يَبقَ إلا أنْ يَقول بختيشوع: كان هذا الدّبور حتفاً قاضياً، ولولا هذا العلاجُ لَقَتَلك!‏ ‏ وكذلك الأطباءُ: إذا سَقَوا دواءً فَضرَّ، أو قطعوا عِرْقاً فضرّ، قالوا: أنت مع هذا العلاج الصَّوابِ تجِدُ ما تجد، فلولا ذلك العلاجُ كُنتَ الساعةَ في نَارِ جهنم! ‏ ‏ ‏ 
"""
adawat.adaat.extract_enteties(text)
####extractNamed
text = u"""خَبَّرني ثُمامةُ عَن أمير المؤمنين المأمون أنَّه قال:‏ ‏ قالَ لي بختيشوع بن جبريل الطبيب: إنَّ الذُبابَ إذا دُلِك بِهِ مَوضِعُ لَسْعَةِ الدَّبورِ سَكَن. فَلَسَعَني دَبّورٌ، فَحَكَكتُ على مَوضِعِه أكثَرُ مِن عِشرينَ ذُبابةً فما سَكَن إلا في قَدْرِ الزمانِ الذي كان يسكُنُ فيه مِن غَيرِ عِلاج. فَلَمْ يَبقَ إلا أنْ يَقول بختيشوع: كان هذا الدّبور حتفاً قاضياً، ولولا هذا العلاجُ لَقَتَلك!‏ ‏ وكذلك الأطباءُ: إذا سَقَوا دواءً فَضرَّ، أو قطعوا عِرْقاً فضرّ، قالوا: أنت مع هذا العلاج الصَّوابِ تجِدُ ما تجد، فلولا ذلك العلاجُ كُنتَ الساعةَ في نَارِ جهنم! ‏ ‏ ‏ 
"""
adawat.adaat.extractNamed(text)
####chunk
text=u"""أمضى عمير بن سعد عاماً كاملاً في ولايته على حمص بالشام ، ولم تصل إلى عمر أية أخبار عنه طوال هذه المدة ، ولم يرسل عُمَير الخراج إليه ، ولا تصل عنه أية أنباء . فقال عمر لكاتبه : اكتب إلى عمير فإني أخاف أن يكون خاننا ، وأرسل إليه يستدعيه . 
"""
adawat.adaat.chunksplit(text)
####extractNumbered
text = u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا"
adawat.adaat.extractNumbered(text)   

####bigrams
text = u"تطلع الشمس صباحا"
adawat.adaat.bigrams(text)

