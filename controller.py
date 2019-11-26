import dao
def sort_out(sel_id:str):
    mydata = dao.pupper_select(sel_id)
    return mydata