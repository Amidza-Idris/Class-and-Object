count_msg = 0
msg_list = []

class SMS_store:

    def __init__(self, viewed, from_number, time_arrived, text_SMS):
        global count_msg
        self.viewed = viewed
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_SMS = text_SMS

        count_msg += 1

        msg_list.append((self.viewed, self.from_number, self.time_arrived, self.text_SMS))

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.viewed, self.from_number, self.time_arrived, self.text_SMS)

    def add_new(self, from_number, time_arrived, text_SMS):
        global count_msg
        self.viewed = False
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_SMS = text_SMS

        count_msg += 1

        msg_list.append((self.viewed, self.from_number, self.time_arrived, self.text_SMS))

    def message_count(self):
        return count_msg

    def get_unread(self):
        global msg_list
        index_of_unread = []

        for i in range(len(msg_list)):
            if msg_list[i][0] == False:
                index_of_unread.append(i)

        return index_of_unread

    def get_message(self, i):
        if msg_list[i][0] == True:
            return msg_list[i]

        elif msg_list[i][0] == False:
            temp_list = []
            temp_list.insert(0, True)
            new = msg_list[i][1:4]

            for elem in new:
                temp_list.append(elem)
            msg_list[i] = tuple(temp_list)
            return msg_list[i]

    def delete(self, to_delete):
        del msg_list[to_delete]
        return msg_list

    def clear(self):
        global msg_list
        msg_list = []
        return msg_list


# ______________________________________________________________________________________________________________________
# TESTING THE CLASS

my_inbox = SMS_store(True, 302455678, "09.10.2022", "Hello")
# print(str(my_inbox))

my_inbox.add_new(62385977, "09.11.2022", "Hello 2")
# print(str(my_inbox))

print(my_inbox.message_count())

print(my_inbox.get_unread())

print(my_inbox.get_message(0))
print(my_inbox.get_message(1))

print(msg_list)

print(my_inbox.delete(0))

print(my_inbox.clear())
