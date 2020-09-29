
class ID:

    def __init__(self, taz):
        self.taz = taz

    def return_check_digit(self):
        sum_taz = 0
        taz_list = list(self.taz)[::-1]
        for index in range(0, 8):
            current_digit = int(taz_list[index])
            if not(index % 2):
                twice = current_digit * 2
                sum_taz += twice % 10 + twice // 10
            else:
                sum_taz += current_digit

        if not(sum_taz % 10):
            return 0
        return 10 - sum_taz % 10



