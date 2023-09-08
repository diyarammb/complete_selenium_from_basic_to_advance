# data_list = []
#     a = model_Refference
#     a.Heading = "Tutorial"
#     a = model_RatingScale()
#     a.Ratings_Scale = "dict_object['Rating Scale']"
#
#     Datalist = []
#     Datalist.append(a)
#     pr = Processing_Status()
#     pr.Heading = "RatingScale
#     pr.Status = "Pending"
#     prlist = []
#     prlist.append(pr)
#
#     pending_record = [obj.Heading for obj in prlist if obj.Status == 'Pending']
#     a = model_RatingScale()
#     a.Ratings_Scale = 'Pip RatingScale'
#     Datalist.append(a)
#     rating_scale_list = [obj for obj in Datalist if obj.Ratings_Scale == 'RatingScale']
#     rating_scale_list = [obj for obj in Datalist if obj.Ratings_Scale == 'Pip RatingScale