# """
# Interesting idea to use Enums and map status of icecream to value to then compare,
# Enum Class doc seems to indicate it's not the right tool for this, but worth exploring
# A foot note to comeback for later follows:
# """

# # from enum import Enum

# # class Chocolate(Enum):
# #     WATERY = 0
# #     WATERY = 1
# #     ALMOST_READY = 4-5
# #     READY = 6
# #     OVER_CHURNED = 7
# #     BUTTER = 8

# test = Chocolate(1)
# print(test)
#     {

#         0: 'watery',
#         1: 'almost_ready',
#         2: 'ready',
#         3: 'over churned',
#         4: 'butter'
#     }

#     vanilla_dict = {
#         0: 'watery',
#         1: 'almost_ready',
#         2: 'almost_ready',
#         3: 'almost_ready',
#         4: 'almost_ready',
#         5: 'ready',
#         6: 'over churned',
#         7: 'butter'
#     }

#     strawberry_dict = {
#         0: 'watery',
#         1: 'almost_ready',
#         2: 'ready',
#         3: 'ready',
#         4: 'ready',
#         5: 'over churned',
#         6: 'butter'
#     }

#     peanut_butter_dict = {
#         0: 'watery',
#         1: 'almost_ready',
#         2: 'ready',
#         3: 'over churned',
#         4: 'butter'
#     }
