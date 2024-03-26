import pickle
import streamlit as st
import numpy as np

pickle_sc=open('scaling.pkl', 'rb')
scaling=pickle.load(pickle_sc)

pickle_in=open('LRmodel.pkl', 'rb')
LRmodel=pickle.load(pickle_in)

st.set_page_config(page_title='Airline Passenger Satisfaction', initial_sidebar_state = 'auto')

def main():
    st.title('Airline Passenger Satisfaction Prediction Machine Learning')

    col1, col2,col3 = st.columns(3)
    with col1:
        Gender = st.radio("Gender",
                         ["Male", "Female"],
                         index=None,
                         horizontal=True)
    with col2:
        CustomerType = st.radio("Passanger is Regular",
                         ["Yes", "No"],
                         index=None,
                         horizontal=True)
    with col3:
        TravelType = st.radio("Type of Travel",
                         ["Personal", "Business"],
                         index=None,
                         horizontal=True)
        
    col1, col2,col3, col4 = st.columns(4)
    with col2:
        Classt = st.selectbox("Class",
                              ("Eco", "Eco Plus", "Business"),
                              index=None,
                              placeholder="Select Class",)
    with col1:
        Age = st.number_input('Age')
    with col3:
        FlightDistance = st.number_input('Flight Distance')
    with col4:
        ArrivalDelay=st.number_input('Arrival Delay in Minutes')
    
    st.divider() 
    st.subheader("Please rate your experience (from 1 to 5 stars)")
    col1, col2, col3, col4=st.columns(4)
    with col1:
        wifi = st.radio("Wifi Service",
                         [1, 2, 3, 4, 5],
                         index=None,
                         horizontal=True)
    with col2:
        OnlineBook = st.radio("Online Booking",
                         [1, 2, 3, 4, 5],
                         index=None,
                         horizontal=True)
    with col3:
        timeconvenient = st.radio("Time convenient",
                         [1, 2, 3, 4, 5],
                         index=None,
                         horizontal=True)
    with col4:
        Food = st.radio("Food and Drink",
                         [1, 2, 3, 4, 5],
                         index=None,
                         horizontal=True)
    with col1:
        Onlineboarding = st.radio("Online Boarding",
                         [1, 2, 3, 4, 5],
                         index=None,
                         horizontal=True)
    with col2:
        Seatcomfort = st.radio("Seat Comfort",
                         [1, 2, 3, 4, 5],
                         index=None,
                         horizontal=True)
    with col3:
        Inflightentertainment = st.radio("Inflight Entertainment",
                         [1, 2, 3, 4, 5],
                         index=None,
                         horizontal=True)
    with col4:
        Onboardservice = st.radio("On-board Service",
                         [1, 2, 3, 4, 5],
                         index=None,
                         horizontal=True)
    with col1:
        Legroomservice = st.radio("Leg Room Service",
                         [1, 2, 3, 4, 5],
                         index=None,
                         horizontal=True)
    with col2:
        Baggagehandling = st.radio("Baggage Handling",
                         [1, 2, 3, 4, 5],
                         index=None,
                         horizontal=True)
    with col3:
        Checkinservice = st.radio("Checkin Service",
                         [1, 2, 3, 4, 5],
                         index=None,
                         horizontal=True)
    with col4:
        Inflightservice = st.radio("Inflight Service",
                         [1, 2, 3, 4, 5],
                         index=None,
                         horizontal=True)
    with col1:
        Cleanliness = st.radio("Cleanliness",
                         [1, 2, 3, 4, 5],
                         index=None,
                         horizontal=True)
    with col2:
        Gatelocation = st.radio("Gate location",
                         [1, 2, 3, 4, 5],
                         index=None,
                         horizontal=True)
   
    st.divider() 
    btn = st.columns(2)
    with btn[1]:
       Button= st.button("Button")
    
    sum=0
    count=0
    if Button:

        for i in [wifi, Classt, CustomerType, Gender, ArrivalDelay, timeconvenient, OnlineBook, 
                  Onlineboarding, Food, Seatcomfort, Inflightentertainment, Onboardservice, 
                  Legroomservice, Gatelocation, Inflightservice, Baggagehandling, Checkinservice, Cleanliness, TravelType]:
            if i is None:
                count=count+1
            else:
                sum=sum+1
        if count!=0:
            st.error("Please select all fields")
    
        if FlightDistance<30:
            st.error("Enter Distance more than 30")
        else:
            sum=sum+1
        if Age<7:
            st.error("Enter Age more than 7")
        else:
            sum=sum+1
        
        # encoding
        classencode=None
        if Classt=="Business":
            classencode=0
        elif Classt=="Eco":
            classencode=1
        elif Classt=="Eco Plus":
            classencode=2

        genderencode=None
        if Gender=="Male":
            genderencode=1
        elif Gender=="Female":
            genderencode=0

        CustomerTypeEncode=None
        if CustomerType=="Yes":
            CustomerTypeEncode=0
        elif CustomerType=="No":
            CustomerTypeEncode=1

        TravalTypeEncode=None
        if TravelType=="Personal":
            TravalTypeEncode=1
        elif TravelType=="Business":
            TravalTypeEncode=0
        
        # normalize
        fdist=np.sqrt(FlightDistance)

        data=np.array([[Age,classencode,fdist,wifi,timeconvenient,OnlineBook,Gatelocation,Food,Onlineboarding,Seatcomfort,Inflightentertainment,Onboardservice,Legroomservice,Baggagehandling,Checkinservice,Inflightservice,Cleanliness,ArrivalDelay,genderencode,CustomerTypeEncode,TravalTypeEncode]])
        # scaling
        scalingdata=scaling.transform(data)

        if sum==21:
            # prediction
            report=LRmodel.predict(scalingdata)
            if report==1:
                st.success("Passenger is Satisfied with Airline")
            elif report==0:
                st.warning("The passenger's opinion of the airline is either neutral or dissatisfied")


if __name__=='__main__':
    main()

        # l1=[wifi, Classt, CustomerType, Gender, ArrivalDelay, Age, timeconvenient, OnlineBook,
        #     Onlineboarding, Food, Seatcomfort, Inflightentertainment, Onboardservice, FlightDistance, 
        #     Legroomservice, Gatelocation, Inflightservice, Baggagehandling, Checkinservice, Cleanliness,TravelType]
        # l2=["wifi", "Class", "CustomerType", "Gender", "ArrivalDelay", "Age", "timeconvenient", "OnlineBook", 
        #  "Onlineboarding", "Food", "Seatcomfort", "Inflightentertainment", "Onboardservice", "FlightDistance", 
        #  "Legroomservice", "Gatelocation", "Inflightservice", "Baggagehandling", "Checkinservice", "Cleanliness","TravelType"]
        # for j,k in zip(l1,l2):
        #     st.write(k," : ",j)

        # st.write(Age,Classt,FlightDistance,wifi,timeconvenient,OnlineBook,Gatelocation,Food,Onlineboarding,Seatcomfort,Inflightentertainment,Onboardservice,Legroomservice,Baggagehandling,Checkinservice,Inflightservice,Cleanliness,ArrivalDelay,Gender,CustomerType,TravelType)
        # st.write(Age,classencode,fdist,wifi,timeconvenient,OnlineBook,Gatelocation,Food,Onlineboarding,Seatcomfort,Inflightentertainment,Onboardservice,Legroomservice,Baggagehandling,Checkinservice,Inflightservice,Cleanliness,ArrivalDelay,genderencode,CustomerTypeEncode,TravalTypeEncode)
        
        # #python -m streamlit run app.py