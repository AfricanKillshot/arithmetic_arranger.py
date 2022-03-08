def arithmetic_arranger(value, *result):
    data_list = value
    sign = ''
    for x in data_list:
        data_dict = {}
        for y in x:
            if y == '+' or y == '-':
                sign = y
        x_1 = x.split(' ')
        data_dict[x_1[0]] = x_1[2]
        if sign == '+':
            items = data_dict.items()
            final_items = tuple(items)
            final_final_items = final_items[0]
            result_sum1 = final_final_items[0]
            result_sum2 = final_final_items[1]
            result_sum_total = (int(result_sum1)) + (int(result_sum2))
            print('\n{0:>5}\n{1:<0}{2:>4}\n-----'.format(result_sum1, sign, result_sum2))
            printresult = (str(result_sum_total))
            if result is True:
                print('{0:>5} \n'.format(printresult))
        else:
            items = data_dict.items()
            final_items = tuple(items)
            final_final_items = final_items[0]
            result_sum1 = final_final_items[0]
            result_sum2 = final_final_items[1]
            result_sum_total = (int(result_sum1)) + (int(result_sum2))
            print('\n{0:>5}\n{1:<0}{2:>4}\n-----'.format(result_sum1, sign, result_sum2))
            printresult = (str(result_sum_total))
            if result is True:
                print('{0:>5} \n'.format(printresult))


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

