import React, { createContext, useContext, useState, useEffect } from 'react';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';

type ThemeContextType = {
    darkMode: boolean;
    toggleDarkMode: () => void;
};

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

export const useThemeContext = () => {
    const context = useContext(ThemeContext);
    if (!context) {
        throw new Error('useThemeContext must be used within a ThemeProvider');
    }
    return context;
};

export const CustomThemeProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    // Load initial theme preference from localStorage
    const getInitialTheme = (): boolean => {
        const savedTheme = localStorage.getItem('darkMode');
        return savedTheme === 'true'; // Default to false if not set
    };

    const [darkMode, setDarkMode] = useState(getInitialTheme);

    const toggleDarkMode = () => {
        setDarkMode((prevMode) => {
            const newMode = !prevMode;
            localStorage.setItem('darkMode', JSON.stringify(newMode)); // Save to localStorage
            return newMode;
        });
    };

    // Themes for light and dark modes
    const lightTheme = createTheme({
        palette: {
            mode: 'light',
            primary: {
                main: '#1976d2',
            },
        },
    });

    const darkTheme = createTheme({
        palette: {
            mode: 'dark',
            primary: {
                main: '#90caf9',
            },
            background: {
                default: '#121212',
                paper: '#1e1e1e',
            },
        },
    });

    return (
        <ThemeContext.Provider value={{ darkMode, toggleDarkMode }}>
            <ThemeProvider theme={darkMode ? darkTheme : lightTheme}>
                <CssBaseline />
                {children}
            </ThemeProvider>
        </ThemeContext.Provider>
    );
};
