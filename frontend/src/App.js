import { useState, useEffect } from 'react';
import { fetchQuizzes } from './api';

function App() {
  const [quizzes, setQuizzes] = useState([]);

  useEffect(() => {
    const fetchAllQuizzes = async () => {
      const response = await fetchQuizzes();
      setQuizzes(response.data.quizzes);
    };

    fetchAllQuizzes();
  }, []);

  return (
    <div className="App">
      {/* TODO: Add quiz listing and navigation to quiz detail */}
      {quizzes.map((quiz) => (
        <div key={quiz._id}>
          <h3>{quiz.title}</h3>
        </div>
      ))}
      {/* TODO: Implement quiz creation form */}
      {/* TODO: Implement quiz detail and quiz-taking components */}
      {/* TODO: Implement quiz submission and score display */}
    </div>
  );
}

export default App;
