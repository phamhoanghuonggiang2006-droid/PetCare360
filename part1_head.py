# -*- coding: utf-8 -*-
HEAD_HTML = """<!DOCTYPE html>
<html lang="vi" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <title>PetCare360 - Hệ Sinh Thái Chăm Sóc Thú Cưng & Quản Trị Toàn Diện</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: '#f0fdfa',
                            100: '#ccfbf1',
                            200: '#99f6e4',
                            300: '#5eead4',
                            400: '#2dd4bf',
                            500: '#14b8a6',
                            600: '#0d9488',
                            700: '#0f766e',
                            800: '#115e59',
                            900: '#134e4a',
                            950: '#042f2e',
                        },
                        teal: {
                            50: '#f0fdfa',
                            100: '#ccfbf1',
                            200: '#99f6e4',
                            300: '#5eead4',
                            400: '#2dd4bf',
                            500: '#14b8a6',
                            600: '#0d9488',
                            700: '#0f766e',
                            800: '#115e59',
                            900: '#134e4a',
                            950: '#042f2e',
                        },
                        accent: {
                            400: '#fbbf24',
                            500: '#f59e0b',
                            600: '#d97706',
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <!-- FontAwesome 6 & Lucide Icons & Google Fonts -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <!-- Chart.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Alpine.js CDN -->
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <style>
        [x-cloak] { display: none !important; }
        .hide-scrollbar::-webkit-scrollbar, .no-scrollbar::-webkit-scrollbar { display: none; }
        .hide-scrollbar, .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 9999px; }
        .dark ::-webkit-scrollbar-thumb { background: #334155; }
        .drawer-slide { transition: transform 0.3s ease-in-out; }
    
        @media print {
            body * {
                visibility: hidden !important;
            }
            .print-invoice-area, .print-invoice-area * {
                visibility: visible !important;
            }
            .print-invoice-area {
                position: fixed !important;
                left: 0 !important;
                top: 0 !important;
                width: 100% !important;
                height: auto !important;
                background: white !important;
                color: #000 !important;
                padding: 24px !important;
                margin: 0 !important;
                box-shadow: none !important;
                border: none !important;
                z-index: 9999999 !important;
            }
            .no-print {
                display: none !important;
            }
        }
    </style>
</head>
<body class="h-full font-sans antialiased bg-slate-50 text-slate-800" x-data="superPetCareApp()" x-init="initApp()">
"""
