# import pickle
# import streamlit as st
# import numpy
# def recommend(movie):
#     movie_index = movie_list[movie_list['title'] == movie].index[0]  # it recomend movie on the basis of index position in data set
#     distances = similarity[movie_index]  # distances of each movie by their index number
#     movie_list1 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#     recommended=[]
#
#     for i in movie_list1:
#         recommended.append(movie_list.iloc[i[0]].title)
#     return  recommended
#
# movie_list=pickle.load(open('movies.pkl','rb'))
# movie_list=movie_list['title'].values
#
# similarity=pickle.load(open('similarity.pkl','rb'))
# st.title('Movie recomendation system')
#
# selected_movie_name = st.selectbox(
#     'Enter the movie Name',
#     (movie_list)
# )
#
# if st.button('recomend'):
#     recomendation = recommend(selected_movie_name)
#     for i in recomendation:
#         st.write(i)



import pickle
import streamlit as st
import requests
import time

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)#requested data of movie with thw movie id
#     data = data.json()#It provide the json data
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path #it get movies poster
#     return full_path
#
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]# provide movie_id index
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = movies.iloc[i[0]].movie_id# provide movie_id index
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)
#
#     return recommended_movie_names,recommended_movie_posters
#
#
# st.header('Movie Recommender System')
# movies = pickle.load(open('movies.pkl','rb'))
# similarity = pickle.load(open('similarity.pkl','rb'))
#
# movie_list = movies['title'].values
# selected_movie = st.selectbox(
#     "Type or select a movie from the dropdown",
#     movie_list
# )
#
# if st.button('Show Recommendation'):
#     recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])
#
#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])
#     with st.spinner('Wait for it...'):
#         time.sleep(2)
#     st.success('Done!')

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)#requested data of movie with thw movie id
    data = data.json()#It provide the json data
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path #it get movies poster
    return full_path


def getMovieDetails(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)  # requested data of movie with thw movie id
    data = data.json()  # It provide the json data
    movie_url = data['homepage']
    return movie_url


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]# provide movie_id index
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recomend_url=[]
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id# provide movie_id index
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recomend_url.append((getMovieDetails(movie_id)))

    return recommended_movie_names,recommended_movie_posters,recomend_url



st.header('Movie Recommender System')
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters,recomend_url = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
        st.markdown('**Homepage:** ' + recomend_url[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        st.markdown('**Homepage:** ' + recomend_url[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        st.markdown('**Homepage:** ' + recomend_url[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        st.markdown('**Homepage:** ' + recomend_url[3])

    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        st.markdown('**Homepage:** ' + recomend_url[3])
    with st.spinner('Wait for it...'):
        time.sleep(2)
    st.success('Done!')

