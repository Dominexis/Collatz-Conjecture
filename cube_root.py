import p_adics



def cube_root(target: list[int], places: int) -> list[int]:
    terms = [[(0,0,0)]]
    result: list[int] = []
    carry: list[int] = []

    for i in range(places):
        print(i, end="\r")
        # print(f'Terms: {terms[i]}')
        result.append(0)
        total = sum_terms(terms[i], result, carry[i - 1] if i > 0 else 0)
        if total % 2 != (target[i] if len(target) > i else 0):
            result[i] = 1
            total = sum_terms(terms[i], result, carry[i - 1] if i > 0 else 0)
        carry.append(total//2)
        # print(f'Total: {total}')
        terms.append(create_new_terms(terms[i]))

    return result


def sum_terms(terms: list[tuple[int, int, int]], result: list[int], carry: int) -> int:
    total = carry
    for term in terms:
        total += result[term[0]]*result[term[1]]*result[term[2]]
    return total


def create_new_terms(terms: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    new_terms: list[tuple[int, int, int]] = []
    for term in terms:
        new_terms.append((term[0] + 1, term[1], term[2]))
        if term[0] == 0:
            new_terms.append((term[0], term[1] + 1, term[2]))
            if term[1] == 0:
                new_terms.append((term[0], term[1], term[2] + 1))
    return new_terms



if __name__ == "__main__":
    result = cube_root([1,1], 1000)
    print(p_adics.convert_bits_to_string(result))