# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:37:55 2019

@author: orion.wille
"""

#create empty lists
todo_list = []
complete_list = []


def menu_screen():
    #display menu
    print("\n    :::Menu::: \n")
    print("Here are your options: \n")
    print("1) View Todo List")
    print("2) View Completed Tasks List")
    print("3) Add to Todo List")
    print("4) Mark Task as complete")
    print("5) Exit Program")
    
    #ask user where they would like to go
    print("\nEnter numbers between 1 and 5 to select an option")
    user_choice = int(input("What would you like to select?: "))
    
    if user_choice > 5 or user_choice < 1:
        print("\nPlease enter a valid number between 1 and 5")
        menu_screen()
    elif user_choice == 1:
        view_todo(todo_list)
    elif user_choice == 2:
        view_complete(complete_list)
    elif user_choice == 3:
        add_todo(todo_list)
    elif user_choice == 4:
        task_complete(todo_list, complete_list)
    elif user_choice == 5:
        print("\nExiting program")
    
    

#view todo list function
def view_todo(view_list):
    print("\nHere is your todo list:")
    #display todo list if not empty
    if view_list != []:
        for item in range(len(view_list)):
            print(str(item + 1) + ")", view_list[item])
    #if todo list empty display message
    else: 
        print("\nThere is nothing in your todo list!")
    
    #Go back to menu?
    back_to_menu = input("Press the 'enter' key to return to the menu: ")
    if back_to_menu == "":
        menu_screen()
    else:
        view_todo(view_list)

        
#view completed list function
def view_complete(view_list):
    print("\nHere is your list of completed tasks:")
    #display completed tasks if not empty
    if view_list != []:
        for item in range(len(view_list)):
            print(str(item + 1) + ")", view_list[item])
    #if complete list empty display message
    else:
        print("\nYou haven't completed any tasks yet!")
    #Go back to menu?
    back_to_menu = input("Press the 'enter' key to return to the menu: ")
    if back_to_menu == "":
        menu_screen()
    else:
        view_complete(view_list)
        
#Add to todo list function
def add_todo(add_list):
    #set initial add_more value to 'y'
    add_more = "y"
    #add to list while user continues to enter 'y'
    while add_more == "y":
    
        add_list.append(input("\nWhat would you like to add to your todo list?: "))
        add_more = input("Would you like to add another?('y' for yes, anything else for no): ")
        
     #Go back to menu?
    back_to_menu = input("Press the 'enter' key to return to the menu, or anything else to keep adding to your todo list: ")
    if back_to_menu == "":
        menu_screen()
    else:
        add_todo(add_list)
    #return modified todo list   
    return add_list


def task_complete(remove_item, add_complete):
       #set initial remove_more value to 'y'
       remove_more = "y"
       #remove items from to todo list and add to completed list while user continues to input 'y'
       while remove_more == "y":
           print("\nHere is your todo list:")
           #if todo list not empty print todo list for user reference
           if remove_item != []:
               for item in range(len(remove_item)):
                   print(str(item + 1) + ")", remove_item[item])
            #if todo list empty display message 
           else:
               print("\nThere is nothing in your todo list!")
           #ask which item user would like to remove from todo list    
           finished_item = input("What would you like to mark as complete from your todo list?: ")
           #if user input is in todo list remove the item and add to complete list
           if finished_item in remove_item:
               remove_item.remove(finished_item)
               add_complete.append(finished_item)
               #ask if they would like to remove another
               remove_more = input("Would you like to mark another as complete?('y' for yes, anything else for no): ")
            #if user input not in todo list display message 
           else:
               print("\nThe item is not in the list")
               #ask if they would like to remove another
               remove_more = input("Would you like to mark another as complete?('y' for yes, anything else for no): ")
       #back to menu?
       back_to_menu = input("Press the 'enter' key to return to the menu, or any other key to keep marking tasks as complete: ")
       if back_to_menu == "":
         menu_screen()
       else:
           task_complete(remove_item, add_complete)
       #return updated todo list and complete list
       return remove_item, add_complete

        
menu_screen()