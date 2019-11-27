import dao
def view_contlr(sel_id:str):
    mydata = dao.pupper_select(sel_id)
    return mydata
def ins_contlr(ins_id:str):
    mydata = dao.breed_insert(ins_id)
    return mydata
def del_contlr(del_id:str):
    mydata = dao.pupper_adopt(del_id)
    return mydata