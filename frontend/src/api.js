import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/',
});

export const fetchQuizzes = () => apiClient.get('quizzes/');
export const fetchQuiz = (quizId) => apiClient.get(`quizzes/${quizId}/`);
// TODO: Add other API calls as needed
