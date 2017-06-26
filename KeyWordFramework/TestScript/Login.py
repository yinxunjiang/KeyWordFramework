#encoding=utf-8
from ProjectVar.Var import *
from Util.Excel import *
from Action.Action import *
test_data_excel_file=ParseExcel(test_data_excel_path)
test_data_excel_file.set_sheet_by_name("Sheet1")

for row in test_data_excel_file.get_all_rows()[1:]:
    action_name=row[action_no].value
    locator_type=row[locator_type_no].value
    locator_expression=row[locator_expression_no].value
    action_value=row[value_no].value
    if locator_type is None and locator_expression is None and action_value is not None:
        command_line="%s(u'%s')"%(action_name,action_value)
        print command_line
    elif locator_type is not None and locator_expression is not None and action_value is None:
        command_line="%s('%s','%s')"%(action_name,locator_type,locator_expression)
        print command_line
    elif locator_type is not None and locator_expression is not None and action_value is not None:
        command_line='%s("%s","%s","%s")'%(action_name,locator_type,locator_expression,action_value)
    else:
        command_line=action_name+"()"
        print command_line
    try:
        start=time.time()
        exec(command_line)
        end=time.time()
        execute_time="%.2f"%(end-start)
        row[execute_time_no].value=str(execute_time)+'s'
        row[result_no].value=u'成功'
        row[result_no].font= Font(color="00FF00")#设置成绿色
        #picturepath=get_screen_shot(capturepicturepath,dates(),times())
        #row[shot_picture_no].value=picturepath
    except Exception,e:
        print traceback.format_exc()
        row[execute_time_no].value=str(execute_time)+'s'
        row[result_no].value=u'失败'
        row[result_no].font= Font(color="FF0000")#设置成红色
        row[shot_picture_no].value=get_screen_shot(errorpicturepath,dates(),times())
        row[exception_no].value=traceback.format_exc()
        #test_data_excel_file.add_images(get_screen_shot(errorpicturepath,dates(),times()),row[shot_picture_no])
    test_data_excel_file.workbook_save()
