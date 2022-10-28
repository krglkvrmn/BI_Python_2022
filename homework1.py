def test_rna_or_dna(lst):
    dna = {'a','t','g','c','A','T','G','C'}
    rna = {'a','u','g','c','A','U','G','C'}
    st_set = set(lst)
    if st_set.issubset(dna) and lst != '':
        result = 'dna'
    elif st_set.issubset(rna) and lst != '':
        result = 'rna'
    else:
        result = 'Invalid Alphabet. Try again!'
    return result
    if result == 'rna':
        trna = 'You have entered an RNA sequence, but this function only works with DNA. Try again and enter DNA sequence.'
        return trna
    elif result != 'dna':
        return result
    rna_dic = {'t':'u', 'T':'U'}
    trna = ''
    for i in lst:
        if i in rna_dic:
            trna = trna + rna_dic[i]
        else:
            trna = trna + i
    return trna
