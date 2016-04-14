# Семестровое задание №1 по курсу Natural Language Processing
###F1. Обучить языковую модель на заданном корпусе:
* --src-texts <путь к корпусу, обязательный аргумент>
* --text-encoding <кодировка-текста в файлах корпуса>
* --word-type <surface_all | surface_no_pm | stem | suffix_X>, где в случае surface_all в качестве слов берутся все токены как есть, в случае surface_no_pm – все токены, кроме знаков пунктуаций, в случае stem – “стемма” (см. http://snowball.tartarus.org/ ), в случае suffix_X – окончания слов длиной X
* -n <n-грамность>
* --laplace // при наличии этого аргумента использовать сглаживание по Лапласу
* --good-turing // при наличии этого аргумента использовать сглаживание по Гуд-Тьюрингу (это опционально, за бонусы, см. ниже)
// если ни один вид сглаживания не указан, сглаживать частоты не нужно
* --unknown-word-freq <частота, ниже которой слова в обуч. множестве считаются неизвестными>
* -o <путь-куда-сохранить-сериализованную-языковую-модель, обязательный аргумент>.


###F2. Восстановить порядок слов в предложении. Аргументы:
*   --lm <путь-к-сериализованной языковой-модели>
*  <список-токенов-разделенных-пробелом>

    **Вывод: восстановленное предложение.**
  

###F3. Показать наиболее вероятные слова в местах предложения, обозначенных пропуском. Пропуск во входном предложении может быть несколько. Аргументы:
*  --lm <путь-к-сериализованной языковой-модели>
*  --guess-num <количество комбинаций слов, которые можно подставить в пропуски>
    <предложение в виде токенов разделенных пробелом, пропуск обозначается спец. строкой \<SKIP\> >
*  Вывод программы: упорядоченные по вероятности варианты восстановленного предложения, т.е., где вместо \<SKIP\> подставлены предсказанные слова.

**Пример входа:**
>  --guess-num=2 “Серию статей об \<SKIP\> я начал с \<SKIP\>”.
>
>   Тогда, пример выхода:
>
    Серию статей об \<UNK\> я начал с негатива.
>
    Серию статей об излучении я начал с введения.

###F4. Генерация случайного предложения. Аргументы:
*  --lm <путь-к-сериализованной языковой-модели>
    
    **На выходе: предложение.**

###F5. [Опционально] Реализовать подсчет perplexity на заданном корпусе. Аргументы:
*  --lm <путь-к-сериализованной языковой-модели>
*  <путь-к-тестовой-коллекции>.
    
    **Выход: значение perplexity.**
