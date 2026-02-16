def sum_nodes_two_lists(linked_list_1, linked_list_2):
    if linked_list_1.len() != linked_list_2.len():
        return None
    node_1 = linked_list_1.head
    node_2 = linked_list_2.head
    result_list = []
    while node_1 and node_2:
        summ_nodes_values = node_1.value + node_2.value
        result_list.append(summ_nodes_values)
        node_1 = node_1.next
        node_2 = node_2.next
    return result_list
