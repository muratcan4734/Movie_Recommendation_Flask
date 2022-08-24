import math
import database


class User:
    def __init__(self, id, email, ratings):
        self.id = id
        self.email = email
        self.ratings = ratings


class Ratings:
    def __init__(self, movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10, movie11, movie12, movie13,
                 movie14, movie15, movie16, movie17, movie18, movie19, movie20, movie21, movie22, movie23, movie24, movie25, movie26, movie27,
                 movie28, movie29, movie30, movie31, movie32, movie33, movie34, movie35, movie36, movie37, movie38, movie39, movie40, movie41,
                 movie42, movie43, movie44, movie45, movie46, movie47, movie48, movie49, movie50, movie51, movie52, movie53, movie54, movie55,
                 movie56, movie57, movie58, movie59, movie60, movie61, movie62, movie63, movie64, movie65, movie66, movie67, movie68, movie69,
                 movie70, movie71, movie72, movie73, movie74, movie75, movie76, movie77, movie78, movie79, movie80, movie81, movie82, movie83,
                 movie84, movie85, movie86, movie87, movie88, movie89, movie90, movie91, movie92, movie93, movie94, movie95, movie96, movie97,
                 movie98, movie99, movie100):
        self.movie1 = movie1
        self.movie2 = movie2
        self.movie3 = movie3
        self.movie4 = movie4
        self.movie5 = movie5
        self.movie6 = movie6
        self.movie7 = movie7
        self.movie8 = movie8
        self.movie9 = movie9
        self.movie10 = movie10
        self.movie11 = movie11
        self.movie12 = movie12
        self.movie13 = movie13
        self.movie14 = movie14
        self.movie15 = movie15
        self.movie16 = movie16
        self.movie17 = movie17
        self.movie18 = movie18
        self.movie19 = movie19
        self.movie20 = movie20
        self.movie21 = movie21
        self.movie22 = movie22
        self.movie23 = movie23
        self.movie24 = movie24
        self.movie25 = movie25
        self.movie26 = movie26
        self.movie27 = movie27
        self.movie28 = movie28
        self.movie29 = movie29
        self.movie30 = movie30
        self.movie31 = movie31
        self.movie32 = movie32
        self.movie33 = movie33
        self.movie34 = movie34
        self.movie35 = movie35
        self.movie36 = movie36
        self.movie37 = movie37
        self.movie38 = movie38
        self.movie39 = movie39
        self.movie40 = movie40
        self.movie41 = movie41
        self.movie42 = movie42
        self.movie43 = movie43
        self.movie44 = movie44
        self.movie45 = movie45
        self.movie46 = movie46
        self.movie47 = movie47
        self.movie48 = movie48
        self.movie49 = movie49
        self.movie50 = movie50
        self.movie51 = movie51
        self.movie52 = movie52
        self.movie53 = movie53
        self.movie54 = movie54
        self.movie55 = movie55
        self.movie56 = movie56
        self.movie57 = movie57
        self.movie58 = movie58
        self.movie59 = movie59
        self.movie60 = movie60
        self.movie61 = movie61
        self.movie62 = movie62
        self.movie63 = movie63
        self.movie64 = movie64
        self.movie65 = movie65
        self.movie66 = movie66
        self.movie67 = movie67
        self.movie68 = movie68
        self.movie69 = movie69
        self.movie70 = movie70
        self.movie71 = movie71
        self.movie72 = movie72
        self.movie73 = movie73
        self.movie74 = movie74
        self.movie75 = movie75
        self.movie76 = movie76
        self.movie77 = movie77
        self.movie78 = movie78
        self.movie79 = movie79
        self.movie80 = movie80
        self.movie81 = movie81
        self.movie82 = movie82
        self.movie83 = movie83
        self.movie84 = movie84
        self.movie85 = movie85
        self.movie86 = movie86
        self.movie87 = movie87
        self.movie88 = movie88
        self.movie89 = movie89
        self.movie90 = movie90
        self.movie91 = movie91
        self.movie92 = movie92
        self.movie93 = movie93
        self.movie94 = movie94
        self.movie95 = movie95
        self.movie96 = movie96
        self.movie97 = movie97
        self.movie98 = movie98
        self.movie99 = movie99
        self.movie100 = movie100

def getSuggestion(userId):
    userId = int(userId)
    userList = []
    mostSimilar = []
    allUsers = database.getAllUsers()
    lastUser = None

    for user in allUsers:
        if user['email'] != "admin@admin.com":
            if user['id'] == userId:
                ratings = database.getRatings(user['id'])
                if len(ratings) >= 10:
                    rating = Ratings(ratings[0]['rating'], ratings[1]['rating'], ratings[2]['rating'], ratings[3]['rating'], ratings[4]['rating'],
                                     ratings[5]['rating'], ratings[6]['rating'], ratings[7]['rating'], ratings[8]['rating'], ratings[9]['rating'],
                                     ratings[10]['rating'], ratings[11]['rating'], ratings[12][
                                         'rating'], ratings[13]['rating'], ratings[14]['rating'],
                                     ratings[15]['rating'], ratings[16]['rating'], ratings[17][
                                         'rating'], ratings[18]['rating'], ratings[19]['rating'],
                                     ratings[20]['rating'], ratings[21]['rating'], ratings[22][
                                         'rating'], ratings[23]['rating'], ratings[24]['rating'],
                                     ratings[25]['rating'], ratings[26]['rating'], ratings[27][
                                         'rating'], ratings[28]['rating'], ratings[29]['rating'],
                                     ratings[30]['rating'], ratings[31]['rating'], ratings[32][
                                         'rating'], ratings[33]['rating'], ratings[34]['rating'],
                                     ratings[35]['rating'], ratings[36]['rating'], ratings[37][
                                         'rating'], ratings[38]['rating'], ratings[39]['rating'],
                                     ratings[40]['rating'], ratings[41]['rating'], ratings[42][
                                         'rating'], ratings[43]['rating'], ratings[44]['rating'],
                                     ratings[45]['rating'], ratings[46]['rating'], ratings[47][
                                         'rating'], ratings[48]['rating'], ratings[49]['rating'],
                                     ratings[50]['rating'], ratings[51]['rating'], ratings[52][
                                         'rating'], ratings[53]['rating'], ratings[54]['rating'],
                                     ratings[55]['rating'], ratings[56]['rating'], ratings[57][
                                         'rating'], ratings[58]['rating'], ratings[59]['rating'],
                                     ratings[60]['rating'], ratings[61]['rating'], ratings[62][
                                         'rating'], ratings[63]['rating'], ratings[64]['rating'],
                                     ratings[65]['rating'], ratings[66]['rating'], ratings[67][
                                         'rating'], ratings[68]['rating'], ratings[69]['rating'],
                                     ratings[70]['rating'], ratings[71]['rating'], ratings[72][
                                         'rating'], ratings[73]['rating'], ratings[74]['rating'],
                                     ratings[75]['rating'], ratings[76]['rating'], ratings[77][
                                         'rating'], ratings[78]['rating'], ratings[79]['rating'],
                                     ratings[80]['rating'], ratings[81]['rating'], ratings[82][
                                         'rating'], ratings[83]['rating'], ratings[84]['rating'],
                                     ratings[85]['rating'], ratings[86]['rating'], ratings[87][
                                         'rating'], ratings[88]['rating'], ratings[89]['rating'],
                                     ratings[90]['rating'], ratings[91]['rating'], ratings[92][
                                         'rating'], ratings[93]['rating'], ratings[94]['rating'],
                                     ratings[95]['rating'], ratings[96]['rating'], ratings[97][
                                         'rating'], ratings[98]['rating'], ratings[99]['rating'])

                    lastUser = User(user['id'], user['email'], rating)
            else:
                ratings = database.getRatings(user['id'])
                if len(ratings) >= 10:
                    rating = Ratings(ratings[0]['rating'], ratings[1]['rating'], ratings[2]['rating'], ratings[3]['rating'], ratings[4]['rating'],
                                     ratings[5]['rating'], ratings[6]['rating'], ratings[7]['rating'], ratings[8]['rating'], ratings[9]['rating'],
                                     ratings[10]['rating'], ratings[11]['rating'], ratings[12][
                                         'rating'], ratings[13]['rating'], ratings[14]['rating'],
                                     ratings[15]['rating'], ratings[16]['rating'], ratings[17][
                                         'rating'], ratings[18]['rating'], ratings[19]['rating'],
                                     ratings[20]['rating'], ratings[21]['rating'], ratings[22][
                                         'rating'], ratings[23]['rating'], ratings[24]['rating'],
                                     ratings[25]['rating'], ratings[26]['rating'], ratings[27][
                                         'rating'], ratings[28]['rating'], ratings[29]['rating'],
                                     ratings[30]['rating'], ratings[31]['rating'], ratings[32][
                                         'rating'], ratings[33]['rating'], ratings[34]['rating'],
                                     ratings[35]['rating'], ratings[36]['rating'], ratings[37][
                                         'rating'], ratings[38]['rating'], ratings[39]['rating'],
                                     ratings[40]['rating'], ratings[41]['rating'], ratings[42][
                                         'rating'], ratings[43]['rating'], ratings[44]['rating'],
                                     ratings[45]['rating'], ratings[46]['rating'], ratings[47][
                                         'rating'], ratings[48]['rating'], ratings[49]['rating'],
                                     ratings[50]['rating'], ratings[51]['rating'], ratings[52][
                                         'rating'], ratings[53]['rating'], ratings[54]['rating'],
                                     ratings[55]['rating'], ratings[56]['rating'], ratings[57][
                                         'rating'], ratings[58]['rating'], ratings[59]['rating'],
                                     ratings[60]['rating'], ratings[61]['rating'], ratings[62][
                                         'rating'], ratings[63]['rating'], ratings[64]['rating'],
                                     ratings[65]['rating'], ratings[66]['rating'], ratings[67][
                                         'rating'], ratings[68]['rating'], ratings[69]['rating'],
                                     ratings[70]['rating'], ratings[71]['rating'], ratings[72][
                                         'rating'], ratings[73]['rating'], ratings[74]['rating'],
                                     ratings[75]['rating'], ratings[76]['rating'], ratings[77][
                                         'rating'], ratings[78]['rating'], ratings[79]['rating'],
                                     ratings[80]['rating'], ratings[81]['rating'], ratings[82][
                                         'rating'], ratings[83]['rating'], ratings[84]['rating'],
                                     ratings[85]['rating'], ratings[86]['rating'], ratings[87][
                                         'rating'], ratings[88]['rating'], ratings[89]['rating'],
                                     ratings[90]['rating'], ratings[91]['rating'], ratings[92][
                                         'rating'], ratings[93]['rating'], ratings[94]['rating'],
                                     ratings[95]['rating'], ratings[96]['rating'], ratings[97][
                                         'rating'], ratings[98]['rating'], ratings[99]['rating'])
                    userList.append(User(user['id'], user['email'], rating))
    for user in userList:
        if user.id != userId:
            mostSimilar.append(
                {"userId": user.id, "similarity": cosine_similarity(user, lastUser)})

    # get the top5 most similar Users
    mostSimilar.sort(key=lambda x: x['similarity'], reverse=True)

    top5 = mostSimilar[:5]

    return top5


def cosine_similarity(user1, user2):
    numerator = 0
    user1 = user1.ratings
    user2 = user2.ratings
    for firstUser, secondUser in zip(user1.__dict__.items(), user2.__dict__.items()):
        numerator += firstUser[1] * secondUser[1]

    denominator = 0
    for firstUser in user1.__dict__.values():
        denominator += firstUser * firstUser
    denominator = math.sqrt(denominator)

    temp = 0
    for secondtUser in user2.__dict__.values():
        temp += secondtUser * secondtUser

    denominator *= math.sqrt(temp)

    return numerator / denominator

