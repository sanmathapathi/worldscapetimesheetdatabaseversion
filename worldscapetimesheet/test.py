from tkinter import *
from tkcalendar import *
import datetime
import shutil
import re
import mysql.connector
import smtplib
from email.mime.text import MIMEText


window =Tk()
window.title("Worldscape Timesheet Login")
window.configure(background="white")

#connecting to the database
w_t_db = mysql.connector.connect(
    host="sql3.freemysqlhosting.net",
    user="sql3354636",
    passwd="amIxjTZ3iV",
    db="sql3354636"
)

global cursor
cursor = w_t_db.cursor()

def force_close_session():
    window4.destroy()

def cancel_logout():
    confirmlabel.destroy()
    confirmbutton.destroy()
    cancelbutton.destroy()

def logout():
    window4.destroy()


def close_queuedtimesheetdata():
    queued_timesheetselectedlabel.config(text = " ")
    queued_hourtypeselectedlabel.config(text = " ")
    queued_hoursinfo1label.config(text = " ")
    queued_hoursinfo2label.config(text = " ")
    queued_hoursinfo3label.config(text = " ")
    queued_hoursinfo4label.config(text = " ")
    queued_hoursinfo5label.config(text = " ")
    queued_hoursinfo6label.config(text = " ")
    queued_hoursinfo7label.config(text = " ")
    queued_hoursnoteslabel.config( text = " ")
    close_data.destroy()

def close_approvedtimesheetdata():
    approved_timesheetselectedlabel.config(text = " ")
    approved_hourtypeselectedlabel.config(text = " ")
    approved_hoursinfo1label.config(text = " ")
    approved_hoursinfo2label.config(text = " ")
    approved_hoursinfo3label.config(text = " ")
    approved_hoursinfo4label.config(text = " ")
    approved_hoursinfo5label.config(text = " ")
    approved_hoursinfo6label.config(text = " ")
    approved_hoursinfo7label.config(text = " ")
    approved_hoursnoteslabel.config(text = " ")
    approval_dateinfolabel.config(text = " ")
    close_data1.destroy()

def close_rejectedtimesheetdata():
    rejected_timesheetselectedlabel.config(text = " ")
    rejected_hourtypeselectedlabel.config(text = " ")
    rejected_hoursinfo1label.config(text = " ")
    rejected_hoursinfo2label.config(text = " ")
    rejected_hoursinfo3label.config(text = " ")
    rejected_hoursinfo4label.config(text = " ")
    rejected_hoursinfo5label.config(text = " ")
    rejected_hoursinfo6label.config(text = " ")
    rejected_hoursinfo7label.config(text = " ")
    rejected_hoursnoteslabel.config(text = " ")
    rejection_dateinfolabel.config(text = " ")
    edit_resubmit_timesheetbutton.destroy()
    close_data2.destroy()

def queued_timesheetselect():
    #Opening the selected queued timesheet in the database and defining its data
    timesheetselected = (queued_timesheetlistbox.get(ANCHOR),)
    timesheetselected_string = str(timesheetselected)
    timesheet_selected = timesheetselected_string.replace("(", "")
    timesheet_selected1 = timesheet_selected.replace(")", "")
    timesheet_selected2 = timesheet_selected1.replace("'", "")
    timesheet_selected_label = timesheet_selected2.replace(",", "")

    #getting the saved hourtype
    hourtype_get = "SELECT hourtype_selected FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(hourtype_get, timesheetselected)
    hourtype = cursor.fetchall()

    hourtype_string = str(hourtype)
    hourtype1 = hourtype_string.replace("[", "")
    hourtype2 = hourtype1.replace("]", "")
    hourtype3 = hourtype2.replace("(", "")
    hourtype4 = hourtype3.replace(")", "")
    hourtype5 = hourtype4.replace("'", "")
    hourtype_final = hourtype5.replace(",", "")

    #getting day1 hours saved
    day1_get = "SELECT day1 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day1_get, timesheetselected)
    day1 = cursor.fetchall()

    day1_string = str(day1)
    day1_1 = day1_string.replace("[", "")
    day1_2 = day1_1.replace("]", "")
    day1_3 = day1_2.replace("(", "")
    day1_4 = day1_3.replace(")", "")
    day1_5 = day1_4.replace("'", "")
    day1_final = day1_5.replace(",", "")

    #getting day2 hours saved
    day2_get = "SELECT day2 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day2_get, timesheetselected)
    day2 = cursor.fetchall()

    day2_string = str(day2)
    day2_1 = day2_string.replace("[", "")
    day2_2 = day2_1.replace("]", "")
    day2_3 = day2_2.replace("(", "")
    day2_4 = day2_3.replace(")", "")
    day2_5 = day2_4.replace("'", "")
    day2_final = day2_5.replace(",", "")

    #getting day3 hours saved
    day3_get = "SELECT day3 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day3_get, timesheetselected)
    day3 = cursor.fetchall()

    day3_string = str(day3)
    day3_1 = day3_string.replace("[", "")
    day3_2 = day3_1.replace("]", "")
    day3_3 = day3_2.replace("(", "")
    day3_4 = day3_3.replace(")", "")
    day3_5 = day3_4.replace("'", "")
    day3_final = day3_5.replace(",", "")

    #getting day4 hours saved
    day4_get = "SELECT day4 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day4_get, timesheetselected)
    day4 = cursor.fetchall()

    day4_string = str(day4)
    day4_1 = day4_string.replace("[", "")
    day4_2 = day4_1.replace("]", "")
    day4_3 = day4_2.replace("(", "")
    day4_4 = day4_3.replace(")", "")
    day4_5 = day4_4.replace("'", "")
    day4_final = day4_5.replace(",", "")

    #getting day5 hours saved
    day5_get = "SELECT day5 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day5_get, timesheetselected)
    day5 = cursor.fetchall()

    day5_string = str(day5)
    day5_1 = day5_string.replace("[", "")
    day5_2 = day5_1.replace("]", "")
    day5_3 = day5_2.replace("(", "")
    day5_4 = day5_3.replace(")", "")
    day5_5 = day5_4.replace("'", "")
    day5_final = day5_5.replace(",", "")

    #getting day6 hours saved
    day6_get = "SELECT day6 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day6_get, timesheetselected)
    day6 = cursor.fetchall()

    day6_string = str(day6)
    day6_1 = day6_string.replace("[", "")
    day6_2 = day6_1.replace("]", "")
    day6_3 = day6_2.replace("(", "")
    day6_4 = day6_3.replace(")", "")
    day6_5 = day6_4.replace("'", "")
    day6_final = day6_5.replace(",", "")

    #getting day7 hours_saved
    day7_get = "SELECT day7 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day7_get, timesheetselected)
    day7 = cursor.fetchall()

    day7_string = str(day7)
    day7_1 = day7_string.replace("[", "")
    day7_2 = day7_1.replace("]", "")
    day7_3 = day7_2.replace("(", "")
    day7_4 = day7_3.replace(")", "")
    day7_5 = day7_4.replace("'", "")
    day7_final = day7_5.replace(",", "")

    #getting notes that were saved
    notes_get = "SELECT notes FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(notes_get, timesheetselected)
    notes = cursor.fetchall()

    notes_string = str(notes)
    notes_1 = notes_string.replace("[", "")
    notes_2 = notes_1.replace("]", "")
    notes_3 = notes_2.replace("(", "")
    notes_4 = notes_3.replace(")", "")
    notes_5 = notes_4.replace("'", "")
    notes_final = notes_5.replace(",", "")

    #Labeling the screen with defined data
    queued_timesheetselectedlabel.config(text = timesheet_selected_label)
    queued_hourtypeselectedlabel.config(text = "Hourtype Selected: " + hourtype_final)
    queued_hoursinfo1label.config(text = "Day 1: " + day1_final + " hour(s)")
    queued_hoursinfo2label.config(text = "Day 2: " + day2_final + " hour(s)")
    queued_hoursinfo3label.config(text = "Day 3: " + day3_final + " hour(s)")
    queued_hoursinfo4label.config(text = "Day 4: " + day4_final + " hour(s)")
    queued_hoursinfo5label.config(text = "Day 5: " + day5_final + " hour(s)")
    queued_hoursinfo6label.config(text = "Day 6: " + day6_final + " hour(s)")
    queued_hoursinfo7label.config(text = "Day 7: " + day7_final + " hour(s)")
    queued_hoursnoteslabel.config(text = "Notes: " + notes_final)

    global close_data
    close_data= Button(window6, text="Close", command=close_queuedtimesheetdata )
    close_data.place(x=125, y=600)

def approved_timesheetselect():
    #Opening the selected approved timesheet in the database and defining its data
    timesheetselected = (approved_timesheetlistbox.get(ANCHOR),)
    timesheetselected_string = str(timesheetselected)
    timesheet_selected = timesheetselected_string.replace("(", "")
    timesheet_selected1 = timesheet_selected.replace(")", "")
    timesheet_selected2 = timesheet_selected1.replace("'", "")
    timesheet_selected_label = timesheet_selected2.replace(",", "")

    #getting the saved hourtype
    hourtype_get = "SELECT hourtype_selected FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(hourtype_get, timesheetselected)
    hourtype = cursor.fetchall()

    hourtype_string = str(hourtype)
    hourtype1 = hourtype_string.replace("[", "")
    hourtype2 = hourtype1.replace("]", "")
    hourtype3 = hourtype2.replace("(", "")
    hourtype4 = hourtype3.replace(")", "")
    hourtype5 = hourtype4.replace("'", "")
    hourtype_final = hourtype5.replace(",", "")

    #getting day1 hours saved
    day1_get = "SELECT day1 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day1_get, timesheetselected)
    day1 = cursor.fetchall()

    day1_string = str(day1)
    day1_1 = day1_string.replace("[", "")
    day1_2 = day1_1.replace("]", "")
    day1_3 = day1_2.replace("(", "")
    day1_4 = day1_3.replace(")", "")
    day1_5 = day1_4.replace("'", "")
    day1_final = day1_5.replace(",", "")

    #getting day2 hours saved
    day2_get = "SELECT day2 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day2_get, timesheetselected)
    day2 = cursor.fetchall()

    day2_string = str(day2)
    day2_1 = day2_string.replace("[", "")
    day2_2 = day2_1.replace("]", "")
    day2_3 = day2_2.replace("(", "")
    day2_4 = day2_3.replace(")", "")
    day2_5 = day2_4.replace("'", "")
    day2_final = day2_5.replace(",", "")

    #getting day3 hours saved
    day3_get = "SELECT day3 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day3_get, timesheetselected)
    day3 = cursor.fetchall()

    day3_string = str(day3)
    day3_1 = day3_string.replace("[", "")
    day3_2 = day3_1.replace("]", "")
    day3_3 = day3_2.replace("(", "")
    day3_4 = day3_3.replace(")", "")
    day3_5 = day3_4.replace("'", "")
    day3_final = day3_5.replace(",", "")

    #getting day4 hours saved
    day4_get = "SELECT day4 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day4_get, timesheetselected)
    day4 = cursor.fetchall()

    day4_string = str(day4)
    day4_1 = day4_string.replace("[", "")
    day4_2 = day4_1.replace("]", "")
    day4_3 = day4_2.replace("(", "")
    day4_4 = day4_3.replace(")", "")
    day4_5 = day4_4.replace("'", "")
    day4_final = day4_5.replace(",", "")

    #getting day5 hours saved
    day5_get = "SELECT day5 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day5_get, timesheetselected)
    day5 = cursor.fetchall()

    day5_string = str(day5)
    day5_1 = day5_string.replace("[", "")
    day5_2 = day5_1.replace("]", "")
    day5_3 = day5_2.replace("(", "")
    day5_4 = day5_3.replace(")", "")
    day5_5 = day5_4.replace("'", "")
    day5_final = day5_5.replace(",", "")

    #getting day6 hours saved
    day6_get = "SELECT day6 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day6_get, timesheetselected)
    day6 = cursor.fetchall()

    day6_string = str(day6)
    day6_1 = day6_string.replace("[", "")
    day6_2 = day6_1.replace("]", "")
    day6_3 = day6_2.replace("(", "")
    day6_4 = day6_3.replace(")", "")
    day6_5 = day6_4.replace("'", "")
    day6_final = day6_5.replace(",", "")

    #getting day7 hours_saved
    day7_get = "SELECT day7 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day7_get, timesheetselected)
    day7 = cursor.fetchall()

    day7_string = str(day7)
    day7_1 = day7_string.replace("[", "")
    day7_2 = day7_1.replace("]", "")
    day7_3 = day7_2.replace("(", "")
    day7_4 = day7_3.replace(")", "")
    day7_5 = day7_4.replace("'", "")
    day7_final = day7_5.replace(",", "")

    #getting notes that were saved
    notes_get = "SELECT notes FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(notes_get, timesheetselected)
    notes = cursor.fetchall()

    notes_string = str(notes)
    notes_1 = notes_string.replace("[", "")
    notes_2 = notes_1.replace("]", "")
    notes_3 = notes_2.replace("(", "")
    notes_4 = notes_3.replace(")", "")
    notes_5 = notes_4.replace("'", "")
    notes_final = notes_5.replace(",", "")

    #Labeling the screen with defined data
    approved_timesheetselectedlabel.config(text = timesheet_selected_label)
    approved_hourtypeselectedlabel.config(text = "Hourtype Selected: " + hourtype_final)
    approved_hoursinfo1label.config(text = "Day 1: " + day1_final + " hour(s)")
    approved_hoursinfo2label.config(text = "Day 2: " + day2_final + " hour(s)")
    approved_hoursinfo3label.config(text = "Day 3: " + day3_final + " hour(s)")
    approved_hoursinfo4label.config(text = "Day 4: " + day4_final + " hour(s)")
    approved_hoursinfo5label.config(text = "Day 5: " + day5_final + " hour(s)")
    approved_hoursinfo6label.config(text = "Day 6: " + day6_final + " hour(s)")
    approved_hoursinfo7label.config(text = "Day 7: " + day7_final + " hour(s)")
    approved_hoursnoteslabel.config(text = "Notes: " + notes_final)

    global close_data1
    close_data1= Button(window6, text="Close", command=close_approvedtimesheetdata )
    close_data1.place(x=750, y=600)

def rejected_timesheetselect():
    #Opening the selected rejected timesheet in the database and defining its data
    timesheetselected = (rejected_timesheetlistbox.get(ANCHOR),)
    timesheetselected_string = str(timesheetselected)
    timesheet_selected = timesheetselected_string.replace("(", "")
    timesheet_selected1 = timesheet_selected.replace(")", "")
    timesheet_selected2 = timesheet_selected1.replace("'", "")
    timesheet_selected_label = timesheet_selected2.replace(",", "")

    #getting the saved hourtype
    hourtype_get = "SELECT hourtype_selected FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(hourtype_get, timesheetselected)
    hourtype = cursor.fetchall()

    hourtype_string = str(hourtype)
    hourtype1 = hourtype_string.replace("[", "")
    hourtype2 = hourtype1.replace("]", "")
    hourtype3 = hourtype2.replace("(", "")
    hourtype4 = hourtype3.replace(")", "")
    hourtype5 = hourtype4.replace("'", "")
    hourtype_final = hourtype5.replace(",", "")

    #getting day1 hours saved
    day1_get = "SELECT day1 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day1_get, timesheetselected)
    day1 = cursor.fetchall()

    day1_string = str(day1)
    day1_1 = day1_string.replace("[", "")
    day1_2 = day1_1.replace("]", "")
    day1_3 = day1_2.replace("(", "")
    day1_4 = day1_3.replace(")", "")
    day1_5 = day1_4.replace("'", "")
    day1_final = day1_5.replace(",", "")

    #getting day2 hours saved
    day2_get = "SELECT day2 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day2_get, timesheetselected)
    day2 = cursor.fetchall()

    day2_string = str(day2)
    day2_1 = day2_string.replace("[", "")
    day2_2 = day2_1.replace("]", "")
    day2_3 = day2_2.replace("(", "")
    day2_4 = day2_3.replace(")", "")
    day2_5 = day2_4.replace("'", "")
    day2_final = day2_5.replace(",", "")

    #getting day3 hours saved
    day3_get = "SELECT day3 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day3_get, timesheetselected)
    day3 = cursor.fetchall()

    day3_string = str(day3)
    day3_1 = day3_string.replace("[", "")
    day3_2 = day3_1.replace("]", "")
    day3_3 = day3_2.replace("(", "")
    day3_4 = day3_3.replace(")", "")
    day3_5 = day3_4.replace("'", "")
    day3_final = day3_5.replace(",", "")

    #getting day4 hours saved
    day4_get = "SELECT day4 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day4_get, timesheetselected)
    day4 = cursor.fetchall()

    day4_string = str(day4)
    day4_1 = day4_string.replace("[", "")
    day4_2 = day4_1.replace("]", "")
    day4_3 = day4_2.replace("(", "")
    day4_4 = day4_3.replace(")", "")
    day4_5 = day4_4.replace("'", "")
    day4_final = day4_5.replace(",", "")

    #getting day5 hours saved
    day5_get = "SELECT day5 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day5_get, timesheetselected)
    day5 = cursor.fetchall()

    day5_string = str(day5)
    day5_1 = day5_string.replace("[", "")
    day5_2 = day5_1.replace("]", "")
    day5_3 = day5_2.replace("(", "")
    day5_4 = day5_3.replace(")", "")
    day5_5 = day5_4.replace("'", "")
    day5_final = day5_5.replace(",", "")

    #getting day6 hours saved
    day6_get = "SELECT day6 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day6_get, timesheetselected)
    day6 = cursor.fetchall()

    day6_string = str(day6)
    day6_1 = day6_string.replace("[", "")
    day6_2 = day6_1.replace("]", "")
    day6_3 = day6_2.replace("(", "")
    day6_4 = day6_3.replace(")", "")
    day6_5 = day6_4.replace("'", "")
    day6_final = day6_5.replace(",", "")

    #getting day7 hours_saved
    day7_get = "SELECT day7 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day7_get, timesheetselected)
    day7 = cursor.fetchall()

    day7_string = str(day7)
    day7_1 = day7_string.replace("[", "")
    day7_2 = day7_1.replace("]", "")
    day7_3 = day7_2.replace("(", "")
    day7_4 = day7_3.replace(")", "")
    day7_5 = day7_4.replace("'", "")
    day7_final = day7_5.replace(",", "")

    #getting notes that were saved
    notes_get = "SELECT notes FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(notes_get, timesheetselected)
    notes = cursor.fetchall()

    notes_string = str(notes)
    notes_1 = notes_string.replace("[", "")
    notes_2 = notes_1.replace("]", "")
    notes_3 = notes_2.replace("(", "")
    notes_4 = notes_3.replace(")", "")
    notes_5 = notes_4.replace("'", "")
    notes_final = notes_5.replace(",", "")

    #Labeling the screen with defined data
    rejected_timesheetselectedlabel.config(text = timesheet_selected_label)
    rejected_hourtypeselectedlabel.config(text = "Hourtype Selected: " + hourtype_final)
    rejected_hoursinfo1label.config(text = "Day 1: " + day1_final + " hour(s)")
    rejected_hoursinfo2label.config(text = "Day 2: " + day2_final + " hour(s)")
    rejected_hoursinfo3label.config(text = "Day 3: " + day3_final + " hour(s)")
    rejected_hoursinfo4label.config(text = "Day 4: " + day4_final + " hour(s)")
    rejected_hoursinfo5label.config(text = "Day 5: " + day5_final + " hour(s)")
    rejected_hoursinfo6label.config(text = "Day 6: " + day6_final + " hour(s)")
    rejected_hoursinfo7label.config(text = "Day 7: " + day7_final + " hour(s)")
    rejected_hoursnoteslabel.config(text = "Notes: " + notes_final)

    #for the rejected timesheet view, users will have the option to edit and resubmit their data by clicking this button
    global edit_resubmit_timesheetbutton
    edit_resubmit_timesheetbutton = Button(window6, text="Edit + Resubmit this timesheet", command=open_editrejectmenu)
    edit_resubmit_timesheetbutton.place(x=1325, y=600)

    global close_data2
    close_data2= Button(window6, text="Close", command=close_rejectedtimesheetdata )
    close_data2.place(x=1325, y=630)

def save_editedtimesheet():
    remove_rejected = "DELETE FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(remove_rejected, rejected_timesheetselected)

    w_t_db.commit()

    rejected_timesheet_selected_string = str(rejected_timesheetselected)
    rejected_timesheet_selected1 = rejected_timesheet_selected_string.replace("(", "")
    rejected_timesheet_selected2 = rejected_timesheet_selected1.replace(")", "")
    rejected_timesheet_selected3 = rejected_timesheet_selected2.replace("'", "")
    rejected_timesheet_selected4 = rejected_timesheet_selected3.replace(",", "")

    hoursentry_data1 = rejected_hoursentrydata1.get()
    hoursentry_data2 = rejected_hoursentrydata2.get()
    hoursentry_data3 = rejected_hoursentrydata3.get()
    hoursentry_data4 = rejected_hoursentrydata4.get()
    hoursentry_data5 = rejected_hoursentrydata5.get()
    hoursentry_data6 = rejected_hoursentrydata6.get()
    hoursentry_data7 = rejected_hoursentrydata7.get()
    hoursentry_datanotes = rejected_hoursentry_notes.get()
    print(hoursentry_datanotes)

    timesheet_data_write = "INSERT INTO " + nameinfo1 + "_timesheetdata" + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    timesheet_data = (rejected_timesheet_selected4, str(rejected_hourtype_selected), str(hoursentry_data1), str(hoursentry_data2), str(hoursentry_data3), str(hoursentry_data4), str(hoursentry_data5), str(hoursentry_data6), str(hoursentry_data7), str(hoursentry_datanotes), 'Rejected')

    cursor.execute(timesheet_data_write, timesheet_data)

    w_t_db.commit()

    rejected_hourtype_listbox.config(background="light gray")
    rejected_hoursentry1.config(background="light gray")
    rejected_hoursentry2.config(background="light gray")
    rejected_hoursentry3.config(background="light gray")
    rejected_hoursentry4.config(background="light gray")
    rejected_hoursentry5.config(background="light gray")
    rejected_hoursentry6.config(background="light gray")
    rejected_hoursentry7.config(background="light gray")
    rejected_hoursentrynotes.config(background="light gray")
    Label(window7, text = "Your edited timesheet has been saved; please don't forget to come back and resubmit it when you're ready.", bg="white", font="none 12 bold") .place(x=485, y=225)

def resubmit_timesheet():

    remove_rejected = "DELETE FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(remove_rejected, rejected_timesheetselected)

    w_t_db.commit()

    rejected_timesheet_selected_string = str(rejected_timesheetselected)
    rejected_timesheet_selected1 = rejected_timesheet_selected_string.replace("(", "")
    rejected_timesheet_selected2 = rejected_timesheet_selected1.replace(")", "")
    rejected_timesheet_selected3 = rejected_timesheet_selected2.replace("'", "")
    rejected_timesheet_selected4 = rejected_timesheet_selected3.replace(",", "")

    hoursentry_data1 = rejected_hoursentrydata1.get()
    hoursentry_data2 = rejected_hoursentrydata2.get()
    hoursentry_data3 = rejected_hoursentrydata3.get()
    hoursentry_data4 = rejected_hoursentrydata4.get()
    hoursentry_data5 = rejected_hoursentrydata5.get()
    hoursentry_data6 = rejected_hoursentrydata6.get()
    hoursentry_data7 = rejected_hoursentrydata7.get()
    hoursentry_datanotes = rejected_hoursentry_notes.get()

    timesheet_data_write = "INSERT INTO " + nameinfo1 + "_timesheetdata" + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    timesheet_data = (rejected_timesheet_selected4, str(rejected_hourtype_selected), str(hoursentry_data1), str(hoursentry_data2), str(hoursentry_data3), str(hoursentry_data4), str(hoursentry_data5), str(hoursentry_data6), str(hoursentry_data7), str(hoursentry_datanotes), 'Queued')

    cursor.execute(timesheet_data_write, timesheet_data)

    w_t_db.commit()

    rejected_hourtype_listbox.config(background="light gray")
    rejected_hoursentry1.config(background="light gray")
    rejected_hoursentry2.config(background="light gray")
    rejected_hoursentry3.config(background="light gray")
    rejected_hoursentry4.config(background="light gray")
    rejected_hoursentry5.config(background="light gray")
    rejected_hoursentry6.config(background="light gray")
    rejected_hoursentry7.config(background="light gray")
    rejected_hoursentrynotes.config(background="light gray")
    Label(window7, text = "Your edited timesheet has been resubmitted.", bg="white", font="none 12 bold") .place(x=485, y=225)


def open_editrejectmenu():
    global window7
    window7 = Toplevel(window)

    global rejected_timesheetselected
    rejected_timesheetselected = (rejected_timesheetlistbox.get(ANCHOR),)

    rejected_timesheet_string = str(rejected_timesheetselected)
    rejected_timesheet = rejected_timesheet_string.replace("'", "")
    rejected_timesheet1 = rejected_timesheet.replace("(", "")
    rejected_timesheet2 = rejected_timesheet1.replace(")", "")
    rejected_timesheet3 = rejected_timesheet2.replace(",", "")

    window7.title("Edit + Resubmit Timesheet")
    window7.configure(background="white")
    Label (window7, image=logo, bg="white", justify="left") .pack()

    Label(window7, text = rejected_timesheet3, bg="white", font="none 20 bold") .pack()

    Label(window7, text="Hourtype Select", bg="white", font="none 12 bold") .place(x=325, y=125)
    rejected_hourtype_frame = Frame(window7)
    rejected_hourtype_scrollbar = Scrollbar(rejected_hourtype_frame, orient=VERTICAL)
    global rejected_hourtype_listbox
    global rejected_hourtype_list
    rejected_hourtype_listbox = Listbox(rejected_hourtype_frame, yscrollcommand=rejected_hourtype_scrollbar.set)
    rejected_hourtype_scrollbar.config(command=rejected_hourtype_listbox.yview)
    rejected_hourtype_scrollbar.pack(side=RIGHT, fill=Y)
    rejected_hourtype_frame.place(x=325, y=150)
    rejected_hourtype_listbox.pack()
    rejected_hourtype_list = ["Standard", "Double", "Overtime", "Other"]
    for rejected_hourtype in hourtype_list:
        rejected_hourtype_listbox.insert(END, rejected_hourtype)
    Button(window7, text="Select", command=rejected_hourtype_select) .place(x=365, y=325)
    global rejected_hourtype_label
    rejected_hourtype_label = Label(window7, text='', bg="white", fg="green", font="none 12 bold")
    rejected_hourtype_label.place(x=300, y=325)

    global rejected_hoursentrydata1
    global rejected_hoursentry1
    rejected_hoursentrydata1 = StringVar()

    rejected_hoursentry1 = Entry(window7, textvariable = rejected_hoursentrydata1, width=5)
    rejected_hoursentry1.place(x=500, y=150)

    global rejected_hoursentrydata2
    global rejected_hoursentry2
    rejected_hoursentrydata2 = StringVar()
    rejected_hoursentry2 = Entry(window7, textvariable = rejected_hoursentrydata2, width=5)
    rejected_hoursentry2.place(x=575, y=150)

    global rejected_hoursentrydata3
    global rejected_hoursentry3
    rejected_hoursentrydata3 = StringVar()
    rejected_hoursentry3 = Entry(window7, textvariable = rejected_hoursentrydata3, width=5)
    rejected_hoursentry3.place(x=650, y=150)

    global rejected_hoursentrydata4
    global rejected_hoursentry4
    rejected_hoursentrydata4 = StringVar()
    rejected_hoursentry4 = Entry(window7, textvariable = rejected_hoursentrydata4, width=5)
    rejected_hoursentry4.place(x=725, y=150)

    global rejected_hoursentrydata5
    global rejected_hoursentry5
    rejected_hoursentrydata5 = StringVar()
    rejected_hoursentry5 = Entry(window7, textvariable = rejected_hoursentrydata5, width=5)
    rejected_hoursentry5.place(x=800, y=150)

    global rejected_hoursentrydata6
    global rejected_hoursentry6
    rejected_hoursentrydata6 = StringVar()
    rejected_hoursentry6 = Entry(window7, textvariable = rejected_hoursentrydata6, width=5)
    rejected_hoursentry6.place(x=875, y=150)

    global rejected_hoursentrydata7
    global rejected_hoursentry7
    rejected_hoursentrydata7 = StringVar()
    rejected_hoursentry7 = Entry(window7, textvariable = rejected_hoursentrydata7, width=5)
    rejected_hoursentry7.place(x=950, y=150)

    global rejected_hoursentry_notes
    global rejected_hoursentrynotes
    rejected_hoursentry_notes = StringVar()
    Label(window7, text="Notes", bg="white", fg="black", font="none 12 bold") .place(x=1020, y=125)
    rejected_hoursentrynotes = Entry(window7, textvariable = rejected_hoursentry_notes, width=20)
    rejected_hoursentrynotes.place(x=1025, y=150)

    savetimesheet = Button(window7, text = "Save Resubmit Draft", command = save_editedtimesheet) .place(x=1175, y=150)

    locktimesheet = Button(window7, text="Resubmit Timesheet", command = resubmit_timesheet) .place(x=1300, y=150)

    edit_rejectedtimesheet()

def userviewtimesheet():
    global window6
    window6 = Toplevel(window)
    window6.title("View Previous Timesheets")
    window6.configure(background = "white")
    Label(window6, text="View Previous Timesheets", bg="white", font="none 20 bold") .pack()

    #Opening Queued timesheets
    get_queued = "SELECT timesheet FROM " + nameinfo1 + """_timesheetdata WHERE approval_status = 'Queued'"""
    cursor.execute(get_queued)
    all_queued_timesheets = cursor.fetchall()

    #Yet to be approved/rejected Timesheets Listbox
    Label(window6, text="Queued for Approval", bg="white", fg="gray", font="none 12 bold") .place(x=200, y=75)

    queued_timesheetframe = Frame(window6)
    queued_timesheetscrollbar = Scrollbar(queued_timesheetframe, orient=VERTICAL)
    global queued_timesheetlistbox
    queued_timesheetlistbox = Listbox(queued_timesheetframe, yscrollcommand=queued_timesheetscrollbar.set, width=38)
    queued_timesheetscrollbar.config(command=queued_timesheetlistbox.yview)
    queued_timesheetscrollbar.pack(side=RIGHT, fill=Y)
    queued_timesheetframe.place(x=160, y=100)
    queued_timesheetlistbox.pack()

    #Insert queued_timesheet from database - all replace commands are modifying the string to be more visually pleasing
    for queued_timesheet in all_queued_timesheets:
        queued_timesheet_string = str(queued_timesheet)
        queued_timesheet = queued_timesheet_string.replace("'", "")
        queued_timesheet1 = queued_timesheet.replace("(", "")
        queued_timesheet2 = queued_timesheet1.replace(")", "")
        queued_timesheet3 = queued_timesheet2.replace(",", "")
        queued_timesheetlistbox.insert(0, queued_timesheet3)

    Button(window6, text="Select", command=queued_timesheetselect) .place(x=265, y=275)

    #Creating configurable labels that will change according to what timesheet the user selects
    global queued_timesheetselectedlabel
    queued_timesheetselectedlabel = Label(window6, text = '', bg="white", font="none 12 bold")
    queued_timesheetselectedlabel.place(x=125, y=325)

    global queued_hourtypeselectedlabel
    queued_hourtypeselectedlabel = Label(window6, text = " ", bg="white", font="none 12")
    queued_hourtypeselectedlabel.place(x=125, y=350)

    global queued_hoursinfo1label
    queued_hoursinfo1label = Label(window6, text = " ", bg="white", font="none 12")
    queued_hoursinfo1label.place(x=125, y=375)

    global queued_hoursinfo2label
    queued_hoursinfo2label = Label(window6, text = " ", bg="white", font="none 12")
    queued_hoursinfo2label.place(x=125, y=400)

    global queued_hoursinfo3label
    queued_hoursinfo3label = Label(window6, text = " ", bg="white", font="none 12")
    queued_hoursinfo3label.place(x=125, y=425)

    global queued_hoursinfo4label
    queued_hoursinfo4label = Label(window6, text = " ", bg="white", font="none 12")
    queued_hoursinfo4label.place(x=125, y=450)

    global queued_hoursinfo5label
    queued_hoursinfo5label = Label(window6, text = " ", bg="white", font="none 12")
    queued_hoursinfo5label.place(x=125, y=475)

    global queued_hoursinfo6label
    queued_hoursinfo6label = Label(window6, text = " ", bg="white", font="none 12")
    queued_hoursinfo6label.place(x=125, y=500)

    global queued_hoursinfo7label
    queued_hoursinfo7label = Label(window6, text = " ", bg="white", font="none 12")
    queued_hoursinfo7label.place(x=125, y=525)

    global queued_hoursnoteslabel
    queued_hoursnoteslabel = Label(window6, text = " ", bg="white", font="none 12")
    queued_hoursnoteslabel.place(x=125, y=550)

    #Opening Approved timesheets
    get_approved = "SELECT timesheet FROM " + nameinfo1 + """_timesheetdata WHERE approval_status = 'Approved'"""
    cursor.execute(get_approved)
    all_approved_timesheets = cursor.fetchall()

    #Approved Timesheet Listbox
    Label(window6, text="Approved", bg="white", fg="green", font="none 12 bold") .place(x=870, y=75)

    approved_timesheetframe = Frame(window6)
    approved_timesheetscrollbar = Scrollbar(approved_timesheetframe, orient=VERTICAL)
    global approved_timesheetlistbox
    approved_timesheetlistbox = Listbox(approved_timesheetframe, yscrollcommand=approved_timesheetscrollbar.set, width=38)
    approved_timesheetscrollbar.config(command=approved_timesheetlistbox.yview)
    approved_timesheetscrollbar.pack(side=RIGHT, fill=Y)
    approved_timesheetframe.place(x=790, y=100)
    approved_timesheetlistbox.pack()

    #Insert approved_timesheet from database - all replace commands are modifying the string to be more visually pleasing
    for approved_timesheet in all_approved_timesheets:
        approved_timesheet_string = str(approved_timesheet)
        approved_timesheet = approved_timesheet_string.replace("'", "")
        approved_timesheet1 = approved_timesheet.replace("(", "")
        approved_timesheet2 = approved_timesheet1.replace(")", "")
        approved_timesheet3 = approved_timesheet2.replace(",", "")
        approved_timesheetlistbox.insert(0, approved_timesheet3)

    Button(window6, text="Select", command=approved_timesheetselect) .place(x=890, y=275)

    #Creating configurable labels that will change according to what timesheet the user selects
    global approved_timesheetselectedlabel
    approved_timesheetselectedlabel = Label(window6, text = '', bg="white", font="none 12 bold")
    approved_timesheetselectedlabel.place(x=750, y=325)

    global approved_hourtypeselectedlabel
    approved_hourtypeselectedlabel = Label(window6, text = " ", bg="white", font="none 12")
    approved_hourtypeselectedlabel.place(x=750, y=350)

    global approved_hoursinfo1label
    approved_hoursinfo1label = Label(window6, text = " ", bg="white", font="none 12")
    approved_hoursinfo1label.place(x=750, y=375)

    global approved_hoursinfo2label
    approved_hoursinfo2label = Label(window6, text = " ", bg="white", font="none 12")
    approved_hoursinfo2label.place(x=750, y=400)

    global approved_hoursinfo3label
    approved_hoursinfo3label = Label(window6, text = " ", bg="white", font="none 12")
    approved_hoursinfo3label.place(x=750, y=425)

    global approved_hoursinfo4label
    approved_hoursinfo4label = Label(window6, text = " ", bg="white", font="none 12")
    approved_hoursinfo4label.place(x=750, y=450)

    global approved_hoursinfo5label
    approved_hoursinfo5label = Label(window6, text = " ", bg="white", font="none 12")
    approved_hoursinfo5label.place(x=750, y=475)

    global approved_hoursinfo6label
    approved_hoursinfo6label = Label(window6, text = " ", bg="white", font="none 12")
    approved_hoursinfo6label.place(x=750, y=500)

    global approved_hoursinfo7label
    approved_hoursinfo7label = Label(window6, text = " ", bg="white", font="none 12")
    approved_hoursinfo7label.place(x=750, y=525)

    global approved_hoursnoteslabel
    approved_hoursnoteslabel = Label(window6, text = " ", bg="white", font="none 12")
    approved_hoursnoteslabel.place(x=750, y=550)

    global approval_dateinfolabel
    approval_dateinfolabel = Label(window6, text = " ", bg="white", font="none 12")
    approval_dateinfolabel.place(x=750, y=575)

    #Opening Rejected timesheets
    get_rejected = "SELECT timesheet FROM " + nameinfo1 + """_timesheetdata WHERE approval_status = 'Rejected'"""
    cursor.execute(get_rejected)
    all_rejected_timesheets = cursor.fetchall()

    #Rejected Timesheet Listbox
    Label(window6, text="Rejected*", bg="white", fg="red", font="none 12 bold") .place(x=1450, y=75)

    rejected_timesheetframe = Frame(window6)
    rejected_timesheetscrollbar = Scrollbar(rejected_timesheetframe, orient=VERTICAL)
    global rejected_timesheetlistbox
    rejected_timesheetlistbox = Listbox(rejected_timesheetframe, yscrollcommand=rejected_timesheetscrollbar.set, width=38)
    rejected_timesheetscrollbar.config(command=rejected_timesheetlistbox.yview)
    rejected_timesheetscrollbar.pack(side=RIGHT, fill=Y)
    rejected_timesheetframe.place(x=1365, y=100)
    rejected_timesheetlistbox.pack()

    #Insert rejected_timesheet from database - all replace commands are modifying the string to be more visually pleasing
    for rejected_timesheet in all_rejected_timesheets:
        rejected_timesheet_string = str(rejected_timesheet)
        rejected_timesheet = rejected_timesheet_string.replace("'", "")
        rejected_timesheet1 = rejected_timesheet.replace("(", "")
        rejected_timesheet2 = rejected_timesheet1.replace(")", "")
        rejected_timesheet3 = rejected_timesheet2.replace(",", "")
        rejected_timesheetlistbox.insert(0, rejected_timesheet3)

    Button(window6, text="Select", command=rejected_timesheetselect) .place(x=1470, y=275)

    #Creating configurable labels that will change according to what timesheet the user selects
    global rejected_timesheetselectedlabel
    rejected_timesheetselectedlabel = Label(window6, text = '', bg="white", font="none 12 bold")
    rejected_timesheetselectedlabel.place(x=1325, y=325)

    global rejected_hourtypeselectedlabel
    rejected_hourtypeselectedlabel = Label(window6, text = " ", bg="white", font="none 12")
    rejected_hourtypeselectedlabel.place(x=1325, y=350)

    global rejected_hoursinfo1label
    rejected_hoursinfo1label = Label(window6, text = " ", bg="white", font="none 12")
    rejected_hoursinfo1label.place(x=1325, y=375)

    global rejected_hoursinfo2label
    rejected_hoursinfo2label = Label(window6, text = " ", bg="white", font="none 12")
    rejected_hoursinfo2label.place(x=1325, y=400)

    global rejected_hoursinfo3label
    rejected_hoursinfo3label = Label(window6, text = " ", bg="white", font="none 12")
    rejected_hoursinfo3label.place(x=1325, y=425)

    global rejected_hoursinfo4label
    rejected_hoursinfo4label = Label(window6, text = " ", bg="white", font="none 12")
    rejected_hoursinfo4label.place(x=1325, y=450)

    global rejected_hoursinfo5label
    rejected_hoursinfo5label = Label(window6, text = " ", bg="white", font="none 12")
    rejected_hoursinfo5label.place(x=1325, y=475)

    global rejected_hoursinfo6label
    rejected_hoursinfo6label = Label(window6, text=" ", bg="white", font="none 12")
    rejected_hoursinfo6label.place(x=1325, y=500)

    global rejected_hoursinfo7label
    rejected_hoursinfo7label = Label(window6, text = " ", bg="white", font="none 12")
    rejected_hoursinfo7label.place(x=1325, y=525)

    global rejected_hoursnoteslabel
    rejected_hoursnoteslabel = Label(window6, text = " ", bg="white", font="none 12")
    rejected_hoursnoteslabel.place(x=1325, y=550)

    global rejection_dateinfolabel
    rejection_dateinfolabel = Label(window6, text = " ", bg="white", font="none 12")
    rejection_dateinfolabel.place(x=1325, y=575)

    #Quick note to remind users how to edit rejected timesheets
    Label(window6, text = "*You can edit and resubmit rejected timesheets by selecting a rejected timesheet normally and then selecting to edit it.", bg="white", fg="red", font="none 12") .place(x=0, y=1100)
def session_datawrite():

    sessiondatapath = 'C:\\Users\\sanma\\worldscapetimesheet\\usersessiondata\\' + nameinfo + ' sessiondata\\queued_sessiondata'
    hourtype_selected = hourtype_listbox.get(ANCHOR)
    hoursentry_data1 = hoursentrydata1.get()
    hoursentry_data2 = hoursentrydata2.get()
    hoursentry_data3 = hoursentrydata3.get()
    hoursentry_data4 = hoursentrydata4.get()
    hoursentry_data5 = hoursentrydata5.get()
    hoursentry_data6 = hoursentrydata6.get()
    hoursentry_data7 = hoursentrydata7.get()
    hoursentry_datanotes = hoursentry_notes.get()

    timesheet_data_write = "INSERT INTO " + nameinfo1 + "_timesheetdata" + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    timesheet_data = (nameinfo + " Timesheet " + str(datetime.datetime.now()), str(hourtype_selected), int(hoursentry_data1), int(hoursentry_data2), int(hoursentry_data3), int(hoursentry_data4), int(hoursentry_data5), int(hoursentry_data6), int(hoursentry_data7), str(hoursentry_datanotes), 'Queued')

    cursor.execute(timesheet_data_write, timesheet_data)

    w_t_db.commit()

def saved_sessiondatawrite():

    hoursentry_data1 = hoursentrydata1.get()
    hoursentry_data2 = hoursentrydata2.get()
    hoursentry_data3 = hoursentrydata3.get()
    hoursentry_data4 = hoursentrydata4.get()
    hoursentry_data5 = hoursentrydata5.get()
    hoursentry_data6 = hoursentrydata6.get()
    hoursentry_data7 = hoursentrydata7.get()
    hoursentry_datanotes = hoursentry_notes.get()

    timesheet_data_write = "INSERT INTO " + nameinfo1 + "_saveddrafts" + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    timesheet_data = (str(nameinfo + " Timesheet " + datetime.datetime.now()), str(hourtype_selected), str(hoursentry_data1), str(hoursentry_data2), str(hoursentry_data3), str(hoursentry_data4), str(hoursentry_data5), str(hoursentry_data6), str(hoursentry_data7), str(hoursentry_datanotes), 'Saved Draft')

    cursor.execute(timesheet_data_write, timesheet_data)

    w_t_db.commit()

def rejected_hourtype_select():
    global rejected_hourtype_selected
    rejected_hourtype_selected = rejected_hourtype_listbox.get(ANCHOR)
    rejected_hourtype_label.config(text="HOURTYPE SELECTED:\n" + rejected_hourtype_selected)
    Button(window7, text="Change", command=rejected_hourtype_select) .place(x=365, y=370)

def hourtype_select():
    global hourtype_selected
    hourtype_selected = hourtype_listbox.get(ANCHOR)
    hourtype_label.config(text="HOURTYPE SELECTED:\n" + hourtype_selected)
    Button(window4, text="Change", command=hourtype_select) .place(x=365, y=370)

def close_savedtimesheetselect():
    select_save_file_label.destroy()
    saved_timesheetframe.destroy()
    select_saved_timesheet.destroy()
    close_save_select.destroy()

def saved_timesheetselect():
    saved_timesheetselected = (saved_timesheetlistbox.get(ANCHOR),)

    #getting the saved hourtype
    hourtype_get = "SELECT hourtype_selected FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    cursor.execute(hourtype_get, saved_timesheetselected)
    saved_hourtype = cursor.fetchall()

    saved_hourtype_string = str(saved_hourtype)
    saved_hourtype1 = saved_hourtype_string.replace("[", "")
    saved_hourtype2 = saved_hourtype1.replace("]", "")
    saved_hourtype3 = saved_hourtype2.replace("(", "")
    saved_hourtype4 = saved_hourtype3.replace(")", "")
    saved_hourtype5 = saved_hourtype4.replace("'", "")
    saved_hourtype_final = saved_hourtype5.replace(",", "")

    #getting day1 hours saved
    day1_get = "SELECT day1 FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    cursor.execute(day1_get, saved_timesheetselected)
    saved_day1 = cursor.fetchall()

    saved_day1_string = str(saved_day1)
    saved_day1_1 = saved_day1_string.replace("[", "")
    saved_day1_2 = saved_day1_1.replace("]", "")
    saved_day1_3 = saved_day1_2.replace("(", "")
    saved_day1_4 = saved_day1_3.replace(")", "")
    saved_day1_5 = saved_day1_4.replace("'", "")
    saved_day1_final = saved_day1_5.replace(",", "")

    #getting day2 hours saved
    day2_get = "SELECT day2 FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    cursor.execute(day2_get, saved_timesheetselected)
    saved_day2 = cursor.fetchall()

    saved_day2_string = str(saved_day2)
    saved_day2_1 = saved_day2_string.replace("[", "")
    saved_day2_2 = saved_day2_1.replace("]", "")
    saved_day2_3 = saved_day2_2.replace("(", "")
    saved_day2_4 = saved_day2_3.replace(")", "")
    saved_day2_5 = saved_day2_4.replace("'", "")
    saved_day2_final = saved_day2_5.replace(",", "")

    #getting day3 hours saved
    day3_get = "SELECT day3 FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    cursor.execute(day3_get, saved_timesheetselected)
    saved_day3 = cursor.fetchall()

    saved_day3_string = str(saved_day3)
    saved_day3_1 = saved_day3_string.replace("[", "")
    saved_day3_2 = saved_day3_1.replace("]", "")
    saved_day3_3 = saved_day3_2.replace("(", "")
    saved_day3_4 = saved_day3_3.replace(")", "")
    saved_day3_5 = saved_day3_4.replace("'", "")
    saved_day3_final = saved_day3_5.replace(",", "")

    #getting day4 hours saved
    day4_get = "SELECT day4 FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    cursor.execute(day4_get, saved_timesheetselected)
    saved_day4 = cursor.fetchall()

    saved_day4_string = str(saved_day4)
    saved_day4_1 = saved_day4_string.replace("[", "")
    saved_day4_2 = saved_day4_1.replace("]", "")
    saved_day4_3 = saved_day4_2.replace("(", "")
    saved_day4_4 = saved_day4_3.replace(")", "")
    saved_day4_5 = saved_day4_4.replace("'", "")
    saved_day4_final = saved_day4_5.replace(",", "")

    #getting day5 hours saved
    day5_get = "SELECT day5 FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    cursor.execute(day5_get, saved_timesheetselected)
    saved_day5 = cursor.fetchall()

    saved_day5_string = str(saved_day5)
    saved_day5_1 = saved_day5_string.replace("[", "")
    saved_day5_2 = saved_day5_1.replace("]", "")
    saved_day5_3 = saved_day5_2.replace("(", "")
    saved_day5_4 = saved_day5_3.replace(")", "")
    saved_day5_5 = saved_day5_4.replace("'", "")
    saved_day5_final = saved_day5_5.replace(",", "")

    #getting day6 hours saved
    day6_get = "SELECT day6 FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    cursor.execute(day6_get, saved_timesheetselected)
    saved_day6 = cursor.fetchall()

    saved_day6_string = str(saved_day6)
    saved_day6_1 = saved_day6_string.replace("[", "")
    saved_day6_2 = saved_day6_1.replace("]", "")
    saved_day6_3 = saved_day6_2.replace("(", "")
    saved_day6_4 = saved_day6_3.replace(")", "")
    saved_day6_5 = saved_day6_4.replace("'", "")
    saved_day6_final = saved_day6_5.replace(",", "")

    #getting day7 hours_saved
    day7_get = "SELECT day7 FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    cursor.execute(day7_get, saved_timesheetselected)
    saved_day7 = cursor.fetchall()

    saved_day7_string = str(saved_day7)
    saved_day7_1 = saved_day7_string.replace("[", "")
    saved_day7_2 = saved_day7_1.replace("]", "")
    saved_day7_3 = saved_day7_2.replace("(", "")
    saved_day7_4 = saved_day7_3.replace(")", "")
    saved_day7_5 = saved_day7_4.replace("'", "")
    saved_day7_final = saved_day7_5.replace(",", "")

    #getting notes that were saved
    notes_get = "SELECT notes FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    cursor.execute(notes_get, saved_timesheetselected)
    saved_notes = cursor.fetchall()

    saved_notes_string = str(saved_notes)
    saved_notes_1 = saved_notes_string.replace("[", "")
    saved_notes_2 = saved_notes_1.replace("]", "")
    saved_notes_3 = saved_notes_2.replace("(", "")
    saved_notes_4 = saved_notes_3.replace(")", "")
    saved_notes_5 = saved_notes_4.replace("'", "")
    saved_notes_final = saved_notes_5.replace(",", "")

    #changing hourtype to the one on the save file
    hourtype_label.config(text="HOURTYPE SELECTED:\n" + saved_hourtype_final)
    Button(window4, text="Change", command=hourtype_select) .place(x=365, y=370)

    #clearing all entries so they can be replaced by the ones on the save file
    hoursentry1.delete(0, END)
    hoursentry2.delete(0, END)
    hoursentry3.delete(0, END)
    hoursentry4.delete(0, END)
    hoursentry5.delete(0, END)
    hoursentry6.delete(0, END)
    hoursentry7.delete(0, END)
    hoursentrynotes.delete(0, END)

    #replacing the entries with save file data from database
    hoursentry1.insert(END, saved_day1_final)
    hoursentry2.insert(END, saved_day2_final)
    hoursentry3.insert(END, saved_day3_final)
    hoursentry4.insert(END, saved_day4_final)
    hoursentry5.insert(END, saved_day5_final)
    hoursentry6.insert(END, saved_day6_final)
    hoursentry7.insert(END, saved_day7_final)
    hoursentrynotes.insert(END, saved_notes_final)

def timesheet_datetime():

    numweeks = 1

    global start_date
    start_date = start_date_mode

    weeks = {}

    offset = datetime.timedelta(days=0)

    for week in range(numweeks):
        this_week = []
        for day in range(1):
            date = start_date + offset
            date = date.strftime("%m-%d")
            this_week.append(date)
            offset += datetime.timedelta(days=1)

            weeks[week] = this_week

            global sunday_date
            sunday_date_string = str(this_week)[1:-1]
            sunday_date = sunday_date_string.translate({ord("'"): None})

            Label(window4, text = weeks[week], bg="white", font="none 12 bold") .place(x=495, y=125)

    for week in range(numweeks):
        this_week = []
        for day in range(1,2):
            date = start_date + offset
            date = date.strftime("%m-%d")
            this_week.append(date)
            offset += datetime.timedelta(days=1)

            weeks[week] = this_week

            global monday_date
            monday_date_string= str(this_week)[1:-1]
            monday_date = monday_date_string.translate({ord("'"): None})

            Label(window4, text = weeks[week], bg="white", font="none 12 bold") .place(x=570, y=125)

    for week in range(numweeks):
        this_week = []
        for day in range(2,3):
            date = start_date + offset
            date = date.strftime("%m-%d")
            this_week.append(date)
            offset += datetime.timedelta(days=1)

            weeks[week] = this_week

            global tuesday_date
            tuesday_date_string = str(this_week)[1:-1]
            tuesday_date = tuesday_date_string.translate({ord("'"): None})

            Label(window4, text = weeks[week], bg="white", font="none 12 bold") .place(x=645, y=125)

    for week in range(numweeks):
        this_week = []
        for day in range(3,4):
            date = start_date + offset
            date = date.strftime("%m-%d")
            this_week.append(date)
            offset += datetime.timedelta(days=1)

            weeks[week] = this_week

            global wednesday_date
            wednesday_date_string = str(this_week)[1:-1]
            wednesday_date = wednesday_date_string.translate({ord("'"): None})

            Label(window4, text = weeks[week], bg="white", font="none 12 bold") .place(x=720, y=125)

    for week in range(numweeks):
        this_week = []
        for day in range(4,5):
            date = start_date + offset
            date = date.strftime("%m-%d")
            this_week.append(date)
            offset += datetime.timedelta(days=1)

            weeks[week] = this_week

            global thursday_date
            thursday_date_string= str(this_week)[1:-1]
            thursday_date = thursday_date_string.translate({ord("'"): None})

            Label(window4, text = weeks[week], bg="white", font="none 12 bold") .place(x=795, y=125)

    for week in range(numweeks):
        this_week = []
        for day in range(5,6):
            date = start_date + offset
            date = date.strftime("%m-%d")
            this_week.append(date)
            offset += datetime.timedelta(days=1)

            weeks[week] = this_week

            global friday_date
            friday_date_string = str(this_week)[1:-1]
            friday_date = friday_date_string.translate({ord("'"): None})

            Label(window4, text = weeks[week], bg="white", font="none 12 bold") .place(x=870, y=125)

    for week in range(numweeks):
        this_week = []
        for day in range(6,7):
            date = start_date + offset
            date = date.strftime("%m-%d")
            this_week.append(date)
            offset += datetime.timedelta(days=1)

            weeks[week] = this_week

            global saturday_date
            saturday_date_string = str(this_week)[1:-1]
            saturday_date = saturday_date_string.translate({ord("'"): None})

            Label(window4, text = weeks[week], bg="white", font="none 12 bold") .place(x=945, y=125)
def open_saved_timesheet():
    #opening database and finding saved drafts

    open_saveddrafts_db = "SELECT timesheet FROM " + nameinfo1 + """_saveddrafts"""

    cursor.execute(open_saveddrafts_db)

    saveddrafts = cursor.fetchall()

    global select_save_file_label
    select_save_file_label = Label(window4, text="Select Save File", bg="white", font="none 12 bold")
    select_save_file_label.place(x=745, y=275)

    #Creating Listbox with all saved drafts
    global saved_timesheetframe
    saved_timesheetframe = Frame(window4)
    saved_timesheetscrollbar = Scrollbar(saved_timesheetframe, orient=VERTICAL)
    global saved_timesheetlistbox
    saved_timesheetlistbox = Listbox(saved_timesheetframe, yscrollcommand=saved_timesheetscrollbar.set, width=50)
    saved_timesheetscrollbar.config(command=saved_timesheetlistbox.yview)
    saved_timesheetscrollbar.pack(side=RIGHT, fill=Y)
    saved_timesheetframe.place(x=745, y=300)
    saved_timesheetlistbox.pack()
    for saved_draft in saveddrafts:
        saved_draft_string = str(saved_draft)
        saved_draft1 = saved_draft_string.replace("(", "")
        saved_draft2 = saved_draft1.replace(")", "")
        saved_draft3 = saved_draft2.replace("'", "")
        saved_draft4 = saved_draft3.replace(",", "")
        saved_timesheetlistbox.insert(0, saved_draft4)

    global select_saved_timesheet
    select_saved_timesheet = Button(window4, text="Select", command=saved_timesheetselect)
    select_saved_timesheet.place(x=880, y=470)

    global close_save_select
    close_save_select = Button(window4, text="Close", command=close_savedtimesheetselect)
    close_save_select.place(x=880, y=505)

def current_week_reset():
    global start_date_mode
    start_date_mode = datetime.datetime(year=2020, month=7, day=5)
    timesheet_datetime()

def close_week_select():
    week_select_calendar.destroy()
    week_select_instructions.destroy()
    week_select_button.destroy()
    currentweekreset.destroy()
    closeweekselect.destroy()


def change_week():
    #Creating calendar to select week of choice
    global week_select_calendar
    week_select_calendar = Calendar(window4, selectmode="day", year=2020, firstweekday="sunday", weekendbackground="light green", othermonthwebackground="light green")
    week_select_calendar.place(x=745, y=300)

    def week_select():
        date_selected = week_select_calendar.get_date()
        if len(date_selected) == 6:
            month_selected = int(date_selected[0])
            day_selected = int(date_selected[2])
            year_selected_string= "20" + date_selected[4] + date_selected[5]
            year_selected = int(year_selected_string)

        if len(date_selected) == 7:
            month_selected = int(date_selected[0])
            day_selected = int(date_selected[2] + date_selected[3])
            year_selected_string= "20" + date_selected[5] + date_selected[6]
            year_selected = int(year_selected_string)

        global start_date_mode
        start_date_mode = datetime.datetime(year=year_selected, month=month_selected, day=day_selected)
        timesheet_datetime()

    global week_select_instructions
    week_select_instructions= Label(window4, text = "Select the SUNDAY of the Week you would like to change the timesheet to.", bg="white", font="none 10")
    week_select_instructions.place(x=650, y=275)

    global week_select_button
    week_select_button = Button(window4, text="Select", command=week_select)
    week_select_button.place(x=850, y=500)

    global currentweekreset
    currentweekreset = Button(window4, text = "Reset to Current Week", command=current_week_reset)
    currentweekreset.place(x=807, y=540)

    global closeweekselect
    closeweekselect = Button(window4, text= "Close Week Select", command=close_week_select)
    closeweekselect.place(x=815, y=580)

def save_timesheet():
    saved_sessiondatawrite()
    hourtype_listbox.config(background="light gray")
    hoursentry1.config(background="light gray")
    hoursentry2.config(background="light gray")
    hoursentry3.config(background="light gray")
    hoursentry4.config(background="light gray")
    hoursentry5.config(background="light gray")
    hoursentry6.config(background="light gray")
    hoursentry7.config(background="light gray")
    hoursentrynotes.config(background="light gray")
    Label(window4, text = "Your timesheet has been saved.", bg="white", font="none 12 bold") .place(x=485, y=225)

def lock_timesheet():
    session_datawrite()
    hourtype_listbox.config(background="light gray")
    hoursentry1.config(background="light gray")
    hoursentry2.config(background="light gray")
    hoursentry3.config(background="light gray")
    hoursentry4.config(background="light gray")
    hoursentry5.config(background="light gray")
    hoursentry6.config(background="light gray")
    hoursentry7.config(background="light gray")
    hoursentrynotes.config(background="light gray")
    Label(window4, text = "Your timesheet has been sent to an Manager for approval and will be updated shortly.", bg="white", font="none 12 bold") .place(x=485, y=225)

def session():
    global window4
    global sessioninfo1
    global nameinfo
    global nameinfo1
    window1.destroy()
    window4 = Toplevel(window)

    window4.title("Dashboard")
    window4.configure(background="white")
    Label (window4, image=logo, bg="white", justify="left") .pack()

    #Opening Database to get user's name

    get_name = "SELECT name FROM userinfo WHERE username = %s"
    username = (username1,)

    cursor.execute(get_name, username)

    name = cursor.fetchall()

    for result in name:
        name_string = str(result)
        name_label = name_string.replace("'", "")
        name_label1 = name_label.replace("(", "")
        name_label2 = name_label1.replace(")", "")
        name_label3 = name_label2.replace(",", "")

    nameinfo = name_label3
    nameinfo1 = name_label3.replace(" ", "")


    Label(window4, text = name_label3 + "\'s Timesheet", bg="white", font="none 20 bold") .pack()

    #making Calendar on screen function

    global start_date_mode
    start_date_mode = datetime.datetime(year=2020, month=7, day=5)
    timesheet_datetime()

    global logoutbutton
    logoutbutton = Button(window4, text="Log Out", width=20, height=1, command=logout)
    logoutbutton.place(x=1300, y=75)
    Label(window4, text=" ", bg="white") .pack()

    Label(window4, text="Hourtype Select", bg="white", font="none 12 bold") .place(x=325, y=125)
    hourtype_frame = Frame(window4)
    hourtype_scrollbar = Scrollbar(hourtype_frame, orient=VERTICAL)
    global hourtype_listbox
    global hourtype_list
    hourtype_listbox = Listbox(hourtype_frame, yscrollcommand=hourtype_scrollbar.set)
    hourtype_scrollbar.config(command=hourtype_listbox.yview)
    hourtype_scrollbar.pack(side=RIGHT, fill=Y)
    hourtype_frame.place(x=325, y=150)
    hourtype_listbox.pack()
    hourtype_list = ["Standard", "Double", "Overtime", "Other"]
    for hourtype in hourtype_list:
        hourtype_listbox.insert(END, hourtype)
    Button(window4, text="Select", command=hourtype_select) .place(x=365, y=325)
    global hourtype_label
    hourtype_label = Label(window4, text='', bg="white", fg="green", font="none 12 bold")
    hourtype_label.place(x=300, y=325)

    global hoursentrydata1
    global hoursentry1
    hoursentrydata1 = StringVar()

    hoursentry1 = Entry(window4, textvariable = hoursentrydata1, width=5)
    hoursentry1.place(x=500, y=150)

    global hoursentrydata2
    global hoursentry2
    hoursentrydata2 = StringVar()
    hoursentry2 = Entry(window4, textvariable = hoursentrydata2, width=5)
    hoursentry2.place(x=575, y=150)

    global hoursentrydata3
    global hoursentry3
    hoursentrydata3 = StringVar()
    hoursentry3 = Entry(window4, textvariable = hoursentrydata3, width=5)
    hoursentry3.place(x=650, y=150)

    global hoursentrydata4
    global hoursentry4
    hoursentrydata4 = StringVar()
    hoursentry4 = Entry(window4, textvariable = hoursentrydata4, width=5)
    hoursentry4.place(x=725, y=150)

    global hoursentrydata5
    global hoursentry5
    hoursentrydata5 = StringVar()
    hoursentry5 = Entry(window4, textvariable = hoursentrydata5, width=5)
    hoursentry5.place(x=800, y=150)

    global hoursentrydata6
    global hoursentry6
    hoursentrydata6 = StringVar()
    hoursentry6 = Entry(window4, textvariable = hoursentrydata6, width=5)
    hoursentry6.place(x=875, y=150)

    global hoursentrydata7
    global hoursentry7
    hoursentrydata7 = StringVar()
    hoursentry7 = Entry(window4, textvariable = hoursentrydata7, width=5)
    hoursentry7.place(x=950, y=150)

    global hoursentry_notes
    global hoursentrynotes
    hoursentry_notes = StringVar()
    Label(window4, text="Notes", bg="white", fg="black", font="none 12 bold") .place(x=1020, y=125)
    hoursentrynotes = Entry(window4, textvariable = hoursentry_notes, width=20)
    hoursentrynotes.place(x=1025, y=150)

    open_savedtimesheet = Button(window4, text="Open Saved Timesheet", command=open_saved_timesheet)  .place(x=325, y=75)

    changeweek = Button(window4, text="Change Week", command=change_week) .place(x=500, y=75)

    savetimesheet = Button(window4, text = "Save Timesheet", command = save_timesheet) .place(x=1175, y=150)

    locktimesheet = Button(window4, text="Lock Timesheet", command = lock_timesheet) .place(x=1275, y=150)

    Button(window4, text="View Previous Timesheets", command = userviewtimesheet) .place(x=1375, y=150)

    global user_sessiondatapath1
    user_sessiondatapath1 = 'C:\\Users\\sanma\\worldscapetimesheet\\usersessiondata\\' + nameinfo + " sessiondata"

def edit_rejectedtimesheet():
    #getting the rejected hourtype
    hourtype_get = "SELECT hourtype_selected FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(hourtype_get, rejected_timesheetselected)
    rejected_hourtype = cursor.fetchall()

    rejected_hourtype_string = str(rejected_hourtype)
    rejected_hourtype1 = rejected_hourtype_string.replace("[", "")
    rejected_hourtype2 = rejected_hourtype1.replace("]", "")
    rejected_hourtype3 = rejected_hourtype2.replace("(", "")
    rejected_hourtype4 = rejected_hourtype3.replace(")", "")
    rejected_hourtype5 = rejected_hourtype4.replace("'", "")
    rejected_hourtype_final = rejected_hourtype5.replace(",", "")

    #getting day1 hours rejected
    day1_get = "SELECT day1 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day1_get, rejected_timesheetselected)
    rejected_day1 = cursor.fetchall()

    rejected_day1_string = str(rejected_day1)
    rejected_day1_1 = rejected_day1_string.replace("[", "")
    rejected_day1_2 = rejected_day1_1.replace("]", "")
    rejected_day1_3 = rejected_day1_2.replace("(", "")
    rejected_day1_4 = rejected_day1_3.replace(")", "")
    rejected_day1_5 = rejected_day1_4.replace("'", "")
    rejected_day1_final = rejected_day1_5.replace(",", "")

    #getting day2 hours rejected
    day2_get = "SELECT day2 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day2_get, rejected_timesheetselected)
    rejected_day2 = cursor.fetchall()

    rejected_day2_string = str(rejected_day2)
    rejected_day2_1 = rejected_day2_string.replace("[", "")
    rejected_day2_2 = rejected_day2_1.replace("]", "")
    rejected_day2_3 = rejected_day2_2.replace("(", "")
    rejected_day2_4 = rejected_day2_3.replace(")", "")
    rejected_day2_5 = rejected_day2_4.replace("'", "")
    rejected_day2_final = rejected_day2_5.replace(",", "")

    #getting day3 hours rejected
    day3_get = "SELECT day3 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day3_get, rejected_timesheetselected)
    rejected_day3 = cursor.fetchall()

    rejected_day3_string = str(rejected_day3)
    rejected_day3_1 = rejected_day3_string.replace("[", "")
    rejected_day3_2 = rejected_day3_1.replace("]", "")
    rejected_day3_3 = rejected_day3_2.replace("(", "")
    rejected_day3_4 = rejected_day3_3.replace(")", "")
    rejected_day3_5 = rejected_day3_4.replace("'", "")
    rejected_day3_final = rejected_day3_5.replace(",", "")

    #getting day4 hours rejected
    day4_get = "SELECT day4 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day4_get, rejected_timesheetselected)
    rejected_day4 = cursor.fetchall()

    rejected_day4_string = str(rejected_day4)
    rejected_day4_1 = rejected_day4_string.replace("[", "")
    rejected_day4_2 = rejected_day4_1.replace("]", "")
    rejected_day4_3 = rejected_day4_2.replace("(", "")
    rejected_day4_4 = rejected_day4_3.replace(")", "")
    rejected_day4_5 = rejected_day4_4.replace("'", "")
    rejected_day4_final = rejected_day4_5.replace(",", "")

    #getting day5 hours rejected
    day5_get = "SELECT day5 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day5_get, rejected_timesheetselected)
    rejected_day5 = cursor.fetchall()

    rejected_day5_string = str(rejected_day5)
    rejected_day5_1 = rejected_day5_string.replace("[", "")
    rejected_day5_2 = rejected_day5_1.replace("]", "")
    rejected_day5_3 = rejected_day5_2.replace("(", "")
    rejected_day5_4 = rejected_day5_3.replace(")", "")
    rejected_day5_5 = rejected_day5_4.replace("'", "")
    rejected_day5_final = rejected_day5_5.replace(",", "")

    #getting day6 hours rejected
    day6_get = "SELECT day6 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day6_get, rejected_timesheetselected)
    rejected_day6 = cursor.fetchall()

    rejected_day6_string = str(rejected_day6)
    rejected_day6_1 = rejected_day6_string.replace("[", "")
    rejected_day6_2 = rejected_day6_1.replace("]", "")
    rejected_day6_3 = rejected_day6_2.replace("(", "")
    rejected_day6_4 = rejected_day6_3.replace(")", "")
    rejected_day6_5 = rejected_day6_4.replace("'", "")
    rejected_day6_final = rejected_day6_5.replace(",", "")

    #getting day7 hours_rejected
    day7_get = "SELECT day7 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day7_get, rejected_timesheetselected)
    rejected_day7 = cursor.fetchall()

    rejected_day7_string = str(rejected_day7)
    rejected_day7_1 = rejected_day7_string.replace("[", "")
    rejected_day7_2 = rejected_day7_1.replace("]", "")
    rejected_day7_3 = rejected_day7_2.replace("(", "")
    rejected_day7_4 = rejected_day7_3.replace(")", "")
    rejected_day7_5 = rejected_day7_4.replace("'", "")
    rejected_day7_final = rejected_day7_5.replace(",", "")

    #getting notes that were rejected
    notes_get = "SELECT notes FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(notes_get, rejected_timesheetselected)
    rejected_notes = cursor.fetchall()

    rejected_notes_string = str(rejected_notes)
    rejected_notes_1 = rejected_notes_string.replace("[", "")
    rejected_notes_2 = rejected_notes_1.replace("]", "")
    rejected_notes_3 = rejected_notes_2.replace("(", "")
    rejected_notes_4 = rejected_notes_3.replace(")", "")
    rejected_notes_5 = rejected_notes_4.replace("'", "")
    rejected_notes_final = rejected_notes_5.replace(",", "")




    rejected_hourtype_label.config(text="HOURTYPE SELECTED:\n" + rejected_hourtype_final)
    Button(window7, text="Change", command=rejected_hourtype_select) .place(x=365, y=370)

    rejected_hoursentry1.insert(END, rejected_day1_final)
    rejected_hoursentry2.insert(END, rejected_day2_final)
    rejected_hoursentry3.insert(END, rejected_day3_final)
    rejected_hoursentry4.insert(END, rejected_day4_final)
    rejected_hoursentry5.insert(END, rejected_day5_final)
    rejected_hoursentry6.insert(END, rejected_day6_final)
    rejected_hoursentry7.insert(END, rejected_day7_final)
    rejected_hoursentrynotes.insert(END, rejected_notes_final)

    global rejected_hourtype_selected
    rejected_hourtype_selected = rejected_hourtype_final

def approvetimesheet():

    approve_timesheet = "UPDATE " + user_selected1 + "_timesheetdata SET approval_status = 'Approved' WHERE timesheet = %s"

    cursor.execute(approve_timesheet, timesheetselected)

    w_t_db.commit()

    approvalstatus.config(text="You have approved " + user_selected+ "\'s timesheet", bg="white", fg="green", font="none 12 bold")


def rejecttimesheet():

    reject_timesheet = "UPDATE " + user_selected1 + "_timesheetdata SET approval_status = 'Rejected' WHERE timesheet = %s"

    cursor.execute(reject_timesheet, timesheetselected)

    w_t_db.commit()

    approvalstatus.config(text="You have rejected " + user_selected + "\'s timesheet", bg="white", fg="red", font="none 12 bold")

def viewselectedtimesheet():
        global timesheetselected
        timesheetselected = (usertimesheet_listbox.get(ANCHOR),)

        #getting the saved hourtype
        hourtype_get = "SELECT hourtype_selected FROM " + user_selected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(hourtype_get, timesheetselected)
        hourtype = cursor.fetchall()

        hourtype_string = str(hourtype)
        hourtype1 = hourtype_string.replace("[", "")
        hourtype2 = hourtype1.replace("]", "")
        hourtype3 = hourtype2.replace("(", "")
        hourtype4 = hourtype3.replace(")", "")
        hourtype5 = hourtype4.replace("'", "")
        hourtype_final = hourtype5.replace(",", "")

        #getting day1 hours saved
        day1_get = "SELECT day1 FROM " + user_selected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day1_get, timesheetselected)
        day1 = cursor.fetchall()

        day1_string = str(day1)
        day1_1 = day1_string.replace("[", "")
        day1_2 = day1_1.replace("]", "")
        day1_3 = day1_2.replace("(", "")
        day1_4 = day1_3.replace(")", "")
        day1_5 = day1_4.replace("'", "")
        day1_final = day1_5.replace(",", "")

        #getting day2 hours saved
        day2_get = "SELECT day2 FROM " + user_selected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day2_get, timesheetselected)
        day2 = cursor.fetchall()

        day2_string = str(day2)
        day2_1 = day2_string.replace("[", "")
        day2_2 = day2_1.replace("]", "")
        day2_3 = day2_2.replace("(", "")
        day2_4 = day2_3.replace(")", "")
        day2_5 = day2_4.replace("'", "")
        day2_final = day2_5.replace(",", "")

        #getting day3 hours saved
        day3_get = "SELECT day3 FROM " + user_selected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day3_get, timesheetselected)
        day3 = cursor.fetchall()

        day3_string = str(day3)
        day3_1 = day3_string.replace("[", "")
        day3_2 = day3_1.replace("]", "")
        day3_3 = day3_2.replace("(", "")
        day3_4 = day3_3.replace(")", "")
        day3_5 = day3_4.replace("'", "")
        day3_final = day3_5.replace(",", "")

        #getting day4 hours saved
        day4_get = "SELECT day4 FROM " + user_selected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day4_get, timesheetselected)
        day4 = cursor.fetchall()

        day4_string = str(day4)
        day4_1 = day4_string.replace("[", "")
        day4_2 = day4_1.replace("]", "")
        day4_3 = day4_2.replace("(", "")
        day4_4 = day4_3.replace(")", "")
        day4_5 = day4_4.replace("'", "")
        day4_final = day4_5.replace(",", "")

        #getting day5 hours saved
        day5_get = "SELECT day5 FROM " + user_selected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day5_get, timesheetselected)
        day5 = cursor.fetchall()

        day5_string = str(day5)
        day5_1 = day5_string.replace("[", "")
        day5_2 = day5_1.replace("]", "")
        day5_3 = day5_2.replace("(", "")
        day5_4 = day5_3.replace(")", "")
        day5_5 = day5_4.replace("'", "")
        day5_final = day5_5.replace(",", "")

        #getting day6 hours saved
        day6_get = "SELECT day6 FROM " + user_selected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day6_get, timesheetselected)
        day6 = cursor.fetchall()

        day6_string = str(day6)
        day6_1 = day6_string.replace("[", "")
        day6_2 = day6_1.replace("]", "")
        day6_3 = day6_2.replace("(", "")
        day6_4 = day6_3.replace(")", "")
        day6_5 = day6_4.replace("'", "")
        day6_final = day6_5.replace(",", "")

        #getting day7 hours_saved
        day7_get = "SELECT day7 FROM " + user_selected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day7_get, timesheetselected)
        day7 = cursor.fetchall()

        day7_string = str(day7)
        day7_1 = day7_string.replace("[", "")
        day7_2 = day7_1.replace("]", "")
        day7_3 = day7_2.replace("(", "")
        day7_4 = day7_3.replace(")", "")
        day7_5 = day7_4.replace("'", "")
        day7_final = day7_5.replace(",", "")

        #getting notes that were saved
        notes_get = "SELECT notes FROM " + user_selected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(notes_get, timesheetselected)
        notes = cursor.fetchall()

        notes_string = str(notes)
        notes_1 = notes_string.replace("[", "")
        notes_2 = notes_1.replace("]", "")
        notes_3 = notes_2.replace("(", "")
        notes_4 = notes_3.replace(")", "")
        notes_5 = notes_4.replace("'", "")
        notes_final = notes_5.replace(",", "")

        Label(window5, text = user_selected + "\'s Timesheet Data", bg="white", font="none 12 bold") .place(x=675, y=125)
        Label(window5, text = "Hourtype Selected: " + hourtype_final, bg="white", font="none 12") .place(x=675, y=150)
        Label(window5, text = "Day 1: " + day1_final + " hour(s)", bg="white", font="none 12") .place(x=675, y=180)
        Label(window5, text = "Day 2: " + day2_final + " hour(s)", bg="white", font="none 12") .place(x=675, y=210)
        Label(window5, text = "Day 3: " + day3_final + " hour(s)", bg="white", font="none 12") .place(x=675, y=250)
        Label(window5, text = "Day 4: " + day4_final + " hour(s)", bg="white", font="none 12") .place(x=675, y=290)
        Label(window5, text = "Day 5: " + day5_final + " hour(s)", bg="white", font="none 12") .place(x=675, y=330)
        Label(window5, text = "Day 6: " + day6_final + " hour(s)", bg="white", font="none 12") .place(x=675, y=370)
        Label(window5, text = "Day 7: " + day7_final + " hour(s)", bg="white", font="none 12") .place(x=675, y=410)
        Label(window5, text = "Notes: " + notes_final, bg="white", font="none 12") .place(x=675, y=450)

        global approvalstatus
        approvalstatus = Label(window5, text = "Please approve or reject this timesheet.", bg="white", fg="gray", font="none 12 bold")
        approvalstatus.place(x=675, y=480)

        global approvebutton
        global rejectbutton
        approvebutton = Button(window5, text = "Approve", command=approvetimesheet) .place(x=675, y=510)
        rejectbutton = Button(window5, text = "Reject", command=rejecttimesheet) .place(x=675, y=540)

def viewalltimesheets():
    global user_selected
    user_selected = user_listbox.get(ANCHOR)

    #modifying user_selected to be the same as the database name - no spaces
    global user_selected1
    user_selected1 = user_selected.replace(" ", "")

    #opening all timesheets from the user selected in the database
    all_timesheets_select = "SELECT timesheet FROM " + user_selected1 + "_timesheetdata WHERE approval_status = 'Queued'"

    cursor.execute(all_timesheets_select)

    all_timesheets = cursor.fetchall()

    #Creating listbox of all timesheets to be selected from
    usertimesheet_frame = Frame(window5)
    usertimesheet_scrollbar = Scrollbar(usertimesheet_frame, orient=VERTICAL)
    global usertimesheet_listbox
    usertimesheet_listbox = Listbox(usertimesheet_frame, width=45, yscrollcommand=usertimesheet_scrollbar.set)
    usertimesheet_scrollbar.config(command=usertimesheet_listbox.yview)
    usertimesheet_scrollbar.pack(side=RIGHT, fill=Y)
    usertimesheet_frame.place(x=300, y=150)
    usertimesheet_listbox.pack()

    for usertimesheet in all_timesheets:
        usertimesheet_string = str(usertimesheet)
        usertimesheet_name = usertimesheet_string.replace("'", "")
        usertimesheet_name1 = usertimesheet_name.replace("(", "")
        usertimesheet_name2 = usertimesheet_name1.replace(")", "")
        usertimesheet_name3 = usertimesheet_name2.replace(",", "")
        usertimesheet_listbox.insert(0, usertimesheet_name3)

    Button(window5, text="Select", command=viewselectedtimesheet) .place(x=340, y=325)

def approvehours():
    #Opening Database to get all user names
    get_all_users = "SELECT name FROM userinfo"

    cursor.execute(get_all_users)

    all_users = cursor.fetchall()

    user_frame = Frame(window5)
    user_scrollbar = Scrollbar(user_frame, orient=VERTICAL)
    global user_listbox
    global user_list
    user_listbox = Listbox(user_frame, yscrollcommand=user_scrollbar.set)
    user_scrollbar.config(command=user_listbox.yview)
    user_scrollbar.pack(side=RIGHT, fill=Y)
    user_frame.place(x=105, y=150)
    user_listbox.pack()
    for name in all_users:
        name_string = str(name)
        name_label = name_string.replace("'", "")
        name_label1 = name_label.replace("(", "")
        name_label2 = name_label1.replace(")", "")
        name_label3 = name_label2.replace(",", "")
        user_listbox.insert(END, name_label3)

    Button(window5, text="View Timesheet(s)", width=20, command=viewalltimesheets) .place(x=100, y=320)

def logout_manager_():
    window5.destroy()

def manager_session():
    global window5
    window3.destroy()
    window5 = Toplevel(window)

    window5.title("Manager Dashboard")
    window5.configure(background="white")
    Label (window5, image=logo, bg="white", justify="left") .pack()
    Label(window5, text="Manager Dashboard", bg="white", font="none 20 bold") .pack()

    Button(window5, text="Approve Hours", width=20, command=approvehours) .place(x=100, y=100)

    Button(window5, text="Log Out", width=20, height=1, command=logout_manager_) .place(x=1300, y=75)


def login_success():
    session()
def password_not_recognized():
        verificationerror_label.config(text="Password not recognized.", bg="white", fg="red", font="none 12 bold")
def user_not_found():
        verificationerror_label.config(text="User not recognized.", bg="white", fg="red", font="none 12 bold")

def login():
    global window1
    window1 = Toplevel(window)
    window1.title("Login")
    window1.configure(background="white")
    Label(window1, text="Please enter details below to login.", bg="white", font="none 14 bold") .pack()
    Label(window1, text=" ", bg="white") .pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()


    global username_entry1
    global password_entry1

    Label(window1, text = "Username *", bg="white", font="none 12") .pack()
    username_entry1 = Entry(window1, textvariable = username_verify)
    username_entry1.pack()
    Label(window1, text=" ", bg="white") .pack()
    Label(window1, text="Password *", bg="white", font = "none 12") .pack()
    password_entry1 = Entry(window1, textvariable = password_verify)
    password_entry1.pack()
    Label(window1, text=" ", bg="white") .pack()
    Button(window1, text="Login", width=10, height=1, bg="white", command=login_verify) .pack()

    global verificationerror_label
    verificationerror_label = Label(window1, text=" ", bg="white")
    verificationerror_label.pack()

def login_verify():
    global username1

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    username_search = "SELECT password FROM userinfo WHERE username = %s"
    username_entered = (username1,)
    cursor.execute(username_search, username_entered)

    password_returned = cursor.fetchall()

    if len(password_returned) == 0:
        user_not_found()
    else:
         password_string = str(password_returned)
         password_replace1 = password_string.replace("'", "")
         password_replace2 = password_replace1.replace("(", "")
         password_replace3 = password_replace2.replace(")", "")
         password_replace4 = password_replace3.replace("[", "")
         password_replace5 = password_replace4.replace("]","")
         password_final = password_replace5.replace(",", "")
         if password_final == password1:
             login_success()
         else:
             password_not_recognized()

def manager_login():
    global window3
    window3 = Toplevel(window)
    window3.title("Login")
    window3.configure(background="white")
    Label(window3, text="Please enter details below to login.", bg="white", font="none 14 bold") .pack()
    Label(window3, text=" ", bg="white") .pack()

    global manager_username_verify
    global manager_password_verify

    manager_username_verify = StringVar()
    manager_password_verify = StringVar()


    global manager_username_entry1
    global manager_password_entry1

    Label(window3, text = "Manager Username *", bg="white", font="none 12") .pack()
    manager_username_entry1 = Entry(window3, textvariable = manager_username_verify)
    manager_username_entry1.pack()
    Label(window3, text=" ", bg="white") .pack()
    Label(window3, text="Password *", bg="white", font = "none 12") .pack()
    manager_password_entry1 = Entry(window3, textvariable = manager_password_verify)
    manager_password_entry1.pack()
    Label(window3, text=" ", bg="white") .pack()
    Button(window3, text="Login", width=10, height=1, bg="white", command=manager_login_verify) .pack()

    global manager_verificationerror_label
    manager_verificationerror_label = Label(window3, text=" ", bg="white")
    manager_verificationerror_label.pack()

def manager_login_verify():
    global manager_username1
    manager_username1 = manager_username_verify.get()
    manager_password1 = manager_password_verify.get()
    manager_username_entry1.delete(0, END)
    manager_password_entry1.delete(0, END)

    manager_username_search = "SELECT password FROM managerinfo WHERE username = %s"
    manager_username_entered = (manager_username1,)
    cursor.execute(manager_username_search, manager_username_entered)

    password_returned = cursor.fetchall()

    if len(password_returned) == 0:
        manager_not_found()
    else:
         password_string = str(password_returned)
         password_replace1 = password_string.replace("'", "")
         password_replace2 = password_replace1.replace("(", "")
         password_replace3 = password_replace2.replace(")", "")
         password_replace4 = password_replace3.replace("[", "")
         password_replace5 = password_replace4.replace("]","")
         password_final = password_replace5.replace(",", "")
         if password_final == manager_password1:
             manager_session()
         else:
             manager_password_not_recognized()

def manager_password_not_recognized():
    manager_verificationerror_label.config(text="Password not recognized.", bg="white", fg="red", font="none 12 bold")

def manager_not_found():
    manager_verificationerror_label.config(text="Username not recognized.", bg="white", fg="red", font="none 12 bold")



def register_user():

    global firstname_info
    global lastname_info
    global email_info
    global username_info
    global password_info
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    email_info = email.get()
    username_info = username.get()
    password_info = password.get()

    sender_email = "timesheettestemail@gmail.com"
    rec_email = email_info
    email_password = "worldscapetest1"
    msg = MIMEText('Dear ' + firstname_info + """, \n \n
    You have successfully registered for the Worldscape Timesheet Application. \n
    This email will be updated with notifications from the application along with necessary information. \n
    If you would like to change the selected email to another one or would like to disable notifications, please do so in the settings tab of the application. \n
    Sincerely, \n
    The Worldscape Timesheet Application Development Team""")
    msg['Subject'] = 'Worldscape Timesheet Application Registration Success'
    msg['From'] = 'timesheettestemail@gmail.com'
    msg['To'] = email_info

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, email_password)
        print("Login Success")
        server.sendmail(sender_email, rec_email, msg.as_string())
        print("Email has been sent to " + rec_email)

        server.quit()

        #adding data to the worldscape_timesheet_database - userinfo table
        user_info_write = "INSERT INTO userinfo (name, email, username, password) VALUES (%s, %s, %s, %s)"

        user_registered_info = (firstname_info + " " + lastname_info, email_info, username_info, password_info)

        cursor.execute(user_info_write, user_registered_info)

        w_t_db.commit()

        print("Committed")
        #creating a user-specific table that all their timesheet data will be saved
        user_timesheet_table = "CREATE TABLE IF NOT EXISTS " + firstname_info + lastname_info + "_timesheetdata" + """ (timesheet VARCHAR(255), hourtype_selected VARCHAR(255), day1 INTEGER(10), day2 INTEGER(10), day3 INTEGER(10), day4 INTEGER(10), day5 INTEGER(10), day6 INTEGER(10), day7 INTEGER(10), notes VARCHAR(255), approval_status VARCHAR(255))"""

        cursor.execute(user_timesheet_table)

        w_t_db.commit()

        #creating a user-specific table that all of their saved draft timesheets will be saved

        user_saveddraft_timesheet_table = "CREATE TABLE IF NOT EXISTS " + firstname_info + lastname_info + "_saveddrafts" + """ (timesheet VARCHAR(255), hourtype_selected VARCHAR(255), day1 VARCHAR(255), day2 VARCHAR(255), day3 VARCHAR(255), day4 VARCHAR(255), day5 VARCHAR(255), day6 VARCHAR(255), day7 VARCHAR(255), notes VARCHAR(255), approval_status VARCHAR(255))"""

        cursor.execute(user_saveddraft_timesheet_table)

        w_t_db.commit()

        firstname_entry.delete(0, END)
        lastname_entry.delete(0, END)
        email_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)

        Label(window2, text = "Registration Success", fg="green", font="none 12 bold") .pack()
    except smtplib.SMTPRecipientsRefused:
        firstname_entry.delete(0, END)
        lastname_entry.delete(0, END)
        email_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)

        Label(window2, text = "Email Invalid", fg="red", font="none 12 bold") .pack()


def newuser():
    global window2
    window2 = Toplevel(window)
    window2.title("New User")
    window2.configure(background="white")

    global firstname
    global lastname
    global email
    global username
    global password
    global firstname_entry
    global lastname_entry
    global email_entry
    global username_entry
    global password_entry

    firstname = StringVar()
    lastname = StringVar()
    email = StringVar()
    username = StringVar()
    password = StringVar()


    Label(window2, text="Please enter details below to register.", bg="white", font="none 14 bold") .pack()
    Label(window2, text=" ", bg="white") .pack()
    Label(window2, text="First Name", bg="white", font="none 12") .pack()
    firstname_entry = Entry(window2, textvariable = firstname)
    firstname_entry.pack()
    Label(window2, text="Last Name", bg="white", font="none 12") .pack()
    lastname_entry = Entry(window2, textvariable = lastname)
    lastname_entry.pack()
    Label(window2, text="Email", bg="white", font="none 12") .pack()
    email_entry = Entry(window2, textvariable = email)
    email_entry.pack()
    Label(window2, text="Username", bg="white", font="none 12") .pack()
    username_entry = Entry(window2, textvariable = username)
    username_entry.pack()
    Label(window2, text="Password", bg="white", font="none 12") .pack()
    password_entry = Entry(window2, textvariable = password)
    password_entry.pack()
    Label(window2, text=" ", bg="white") .pack()
    Button(window2, text="Register", width=10, height=1, command=register_user) .pack()





global logo
logo = PhotoImage(file="worldscapeinc.png")
Label (window, image=logo, bg="white", justify="left") .pack()

Label (window, text="Worldscape Timesheet", bg="white", fg="black", font="none 20 bold") .pack()

Button(text="Login", width=20, command=login) .pack()
Label(window, text=" ", bg="white") .pack()
Button(text = "Manager Login", width=20, command=manager_login) .pack()
Label(window, text=" ", bg="white") .pack()
Button(window, text="New User?", width=20, command=newuser) .pack()
window.mainloop()
