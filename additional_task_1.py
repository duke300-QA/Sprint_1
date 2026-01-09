types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def tickets_by_type(types_dict, tickets_dict):
    used = []
    result = {}
    for level in sorted(tickets_dict.keys()):
        unique = []
        for ticket in tickets_dict[level]:
            if ticket not in used:
                unique.append(ticket)
                used.append(ticket)
        result[types_dict[level]] = unique
    return result
print(tickets_by_type(types, tickets))