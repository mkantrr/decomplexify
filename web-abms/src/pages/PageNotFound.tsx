import React from 'react';
import { Link } from 'react-router-dom';

const PageNotFound = () => {
    return (
        <div style={styles.container}>
            <h1 style={styles.heading}>404 - Page Not Found</h1>
            <p style={styles.text}>
                Sorry, the page you are looking for does not exist.
            </p>
            <Link to="/" style={styles.link}>
                Go Back to Home
            </Link>
        </div>
    );
};

const styles = {
    container: { textAlign: 'center' as const, marginTop: '50px' },
    heading: { fontSize: '2rem', marginBottom: '20px' },
    text: { fontSize: '1.2rem', marginBottom: '20px' },
    link: { fontSize: '1rem', color: '#007BFF', textDecoration: 'none' },
};

export default PageNotFound;