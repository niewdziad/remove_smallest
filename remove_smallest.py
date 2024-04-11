def remove_smallest(list_):
    smallest = min(list_)  # Znajdujemy najmniejszy element w liście
    removed = False  # Flaga określająca, czy najmniejszy element został już usunięty
    result = []  # Lista wynikowa

    for item in list_:
        if not removed and item == smallest:  # Jeśli nie usunięto jeszcze najmniejszego elementu i aktualny element jest najmniejszy
            removed = True  # Ustawiamy flagę jako True, aby oznaczyć, że najmniejszy element został usunięty
        else:
            result.append(item)  # Dodajemy aktualny element do listy wynikowej
    
    return result

# Testy
tests = [([1,2,3,4,5], [2,3,4,5]), ([5,4,1,3], [5,4,3]), ([1,2,1], [2,1])]

for test in tests:
    result = remove_smallest(test[0])
    assert result == test[1], "Wrong :("
    assert result is not test[0], "You can't change original list"

print("All tests passed!")