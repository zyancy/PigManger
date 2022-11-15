# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 22:48:51 2022

@author: Admin
"""


import streamlit as st
import os
import sqlite3
from PIL import Image
import pandas
st.set_page_config(page_title="智能猪场数字化管理系统",layout="wide")

base_dir=os.path.dirname(os.path.abspath(__file__))
db_path=base_dir+'\PigManager.db'
con = sqlite3.connect(db_path)

c = con.cursor()

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS UserManager(User TEXT, Password TEXT)')

def add_userdata(username, password):

    if c.execute("SELECT User FROM UserManager WHERE User = :username",{"username":username}):
        st.warning("用户名已存在，请更换一个新的用户名。")
    else:
        c.execute("INSERT INTO userstable(username,password) VALUES(?,?)",(username,password))
        con.commit()
        st.success("恭喜，您已成功注册。")
        st.info("请在左侧选择“登录”选项进行登录。")

def login_user(username,password):
    if c.execute("SELECT User FROM UserManager WHERE User = :username",{"username":username}):
        c.execute("SELECT * FROM UserManager WHERE User = :username AND Password = :password",{"username":username,"password":password,})
        data=c.fetchall()
        
        return data
    else:
        st.warning("用户名不存在，请先选择注册按钮完成注册。")

def view_all_Pigs():
    c.execute("UPDATE PigManager SET 年龄（天数） =(SELECT julianday ('now') - julianday(出生时间) FROM PigManager)")
    c.execute('SELECT * FROM PigManager')
    data = c.fetchall()
    return data

def view_Check_Pigs(colum,value):
    c.execute("UPDATE PigManager SET 年龄（天数） =(SELECT julianday ('now') - julianday(出生时间) FROM PigManager)")
    c.execute('SELECT * FROM PigManager'+' where '+colum +'='+ value)
    data = c.fetchall()
    return data

def main():
    menu = ["首页","登录","注册", "注销"]
    ManagerSystem=["猪场看板","母猪管理","仔猪管理","猪只管理"]
    PigManger_columns=['编号','圈舍号','类别','出生时间','天数','进场时间','出场时间','当前状态']

    
    if 'count' not in st.session_state:
        st.session_state.count = 0

    choice = st.sidebar.selectbox("选项",menu)

    st.sidebar.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 250px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 250px;
        margin-left: -250px;
    }
    </style>
    """,
    unsafe_allow_html=True,)


    if choice =="首页":
        st.subheader("猪场看板系统")
        st.markdown('''Streamlit文档的地址是：https://docs.streamlit.io/''')
        c1, c2 = st.columns(2)
        with c1:
            image1 = Image.open(base_dir+'\pig1.png')
            st.success('This is a success message C1!')
            st.image(image1)
        with c2:
            image2 = Image.open(base_dir+'\pig2.png')
            st.success('This is a success message!')
            st.image(image2)
       
    elif choice =="登录":
        st.sidebar.subheader("登录区域")

        username = st.sidebar.text_input("用户名")
        password = st.sidebar.text_input("密码",type = "password")
        if st.sidebar.checkbox("开始登录"):
            logged_user = login_user(username,password)
            if logged_user:

                st.session_state.count += 1

                if st.session_state.count >= 1:

                    st.sidebar.success("您已登录成功，您的用户名是 {}".format(username))
                   
                    st.title("成功登录后可以看到的内容")
                    st.balloons()
                    
#                    c1, c2 = st.columns(2)
#                    with c1:
#                        image1 = Image.open(base_dir+'\pig1.png')
#                        st.success('This is a success message C1!')
#                        st.image(image1)
#                    with c2:
#                        image2 = Image.open(base_dir+'\pig2.png')
#                        st.success('This is a success message!')
#                        st.image(image2)

            else:
                st.sidebar.warning("用户名或者密码不正确，请检查后重试。")

    elif choice =="注册":
        st.subheader("注册")
        new_user = st.sidebar.text_input("用户名")
        new_password = st.sidebar.text_input("密码",type = "password")

        if st.sidebar.button("注册"):
            create_usertable()
            add_userdata(new_user,new_password)

    elif choice =="注销":
        st.session_state.count = 0
        if st.session_state.count == 0:
            st.info("您已成功注销，如果需要，请选择左侧的登录按钮继续登录。")
    if st.session_state.count>=1:
        st.sidebar.subheader("系统区域")
        choice = st.sidebar.radio("管理系统",ManagerSystem)
        if choice =="猪场看板":
            st.subheader("猪场看板")
            st.markdown('''Streamlit文档的地址是：https://docs.streamlit.io/''')
            with st.form("my_form"):
                st.write("Inside the form")
                slider_val = st.slider("Form slider")
                checkbox_val = st.checkbox("Form checkbox")
        
                # Every form must have a submit button.
                submitted = st.form_submit_button("Submit")
                if submitted:
                    st.write("slider", slider_val, "checkbox", checkbox_val)

            st.write("Outside the form")
        elif choice =="母猪管理":
            st.subheader("母猪管理")
            st.markdown('''Streamlit文档的地址是：https://docs.streamlit.io/''')

        elif choice =="仔猪管理":
            st.subheader("仔猪管理")
            st.markdown('''Streamlit文档的地址是：https://docs.streamlit.io/''')
                
        elif choice =="猪只管理":
            st.subheader("猪只管理")
            st.markdown('''Streamlit文档的地址是：https://docs.streamlit.io/''')
            choice = st.selectbox("按列查询",PigManger_columns)
            value = st.text_input("请输入参数")
            
            if st.checkbox("查询"):
                df = pandas.DataFrame( view_Check_Pigs(choice,value), columns=PigManger_columns)
            else:
                df = pandas.DataFrame( view_all_Pigs(), columns=PigManger_columns)
            st.dataframe(df)
            
    else:
        st.sidebar.warning("请登录！")     

if __name__=="__main__":
    main()