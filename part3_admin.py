# -*- coding: utf-8 -*-
ADMIN_HTML = """
    <!-- ======================================================== -->
    <!-- VIEW 2: GIAO DIỆN QUẢN TRỊ VIÊN CHUYÊN NGHIỆP (ADMIN VIEW) -->
    <!-- ======================================================== -->
    <div x-show="currentRole === 'admin'" class="min-h-screen flex flex-col bg-slate-50 text-slate-800 font-sans" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 scale-98" x-transition:enter-end="opacity-100 scale-100">
        
        <!-- TOP BAR ADMIN (SaaS Header) -->
        <header class="sticky top-0 z-40 bg-white border-b border-slate-200 h-16 flex items-center justify-between px-4 lg:px-6 shadow-sm">
            <div class="flex items-center gap-3 md:gap-5">
                <button @click="sidebarOpen = !sidebarOpen" class="p-2 rounded-xl hover:bg-slate-100 text-slate-600 transition" title="Mở/Đóng menu">
                    <i class="fa-solid fa-bars text-base"></i>
                </button>
                <div class="flex items-center gap-2.5">
                    <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-sky-600 to-teal-500 flex items-center justify-center text-white font-black text-lg shadow-sm shadow-sky-500/20">
                        <i class="fa-solid fa-shield-cat text-lg"></i>
                    </div>
                    <div>
                        <div class="flex items-center gap-1.5">
                            <span class="font-black text-slate-900 text-base tracking-tight leading-none">PetCare<span class="text-sky-600">360</span></span>
                            <span class="text-[10px] bg-sky-100 text-sky-800 font-extrabold px-2 py-0.5 rounded-full uppercase tracking-wider">Admin</span>
                        </div>
                        <span class="text-[10px] text-slate-400 font-medium">Hệ thống quản trị & điều hành</span>
                    </div>
                </div>

                <!-- Global Branch Select -->
                <div class="relative hidden md:block">
                    <div class="flex items-center bg-slate-100 border border-slate-200 rounded-xl px-2.5 py-1 text-xs">
                        <i class="fa-solid fa-location-dot text-sky-600 mr-2 text-xs"></i>
                        <select x-model="globalBranch" @change="showToast('Đã lọc cơ sở: ' + globalBranch)" class="bg-transparent text-xs font-semibold text-slate-800 focus:outline-none cursor-pointer pr-4">
                            <option value="ALL">Tất cả chi nhánh (3 cơ sở)</option>
                            <option value="Q1">Chi nhánh Quận 1 (TP.HCM)</option>
                            <option value="BT">Chi nhánh Bình Thạnh (TP.HCM)</option>
                            <option value="Q7">Chi nhánh Quận 7 (TP.HCM)</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- Header Right Actions -->
            <div class="flex items-center gap-3">
                <!-- Nút chuyển sang giao diện Khách Hàng (Customer View) -->
                <button @click="switchToCustomer()" class="px-3 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold transition flex items-center gap-1.5 border border-slate-200 shadow-2xs">
                    <i class="fa-solid fa-store text-sky-600"></i>
                    <span class="hidden sm:inline">Về Shop Khách Hàng</span>
                </button>

                <!-- Nút thông báo / Việc cần xử lý -->
                <button @click="switchAdminTab('dashboard')" class="relative p-2 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-700 border border-amber-200 text-xs font-bold transition flex items-center gap-1.5">
                    <i class="fa-solid fa-bell text-amber-600"></i>
                    <span class="hidden md:inline">Cần xử lý</span>
                    <span class="w-5 h-5 bg-rose-500 text-white rounded-full text-[10px] font-black flex items-center justify-center">3</span>
                </button>

                <div class="h-6 w-px bg-slate-200 mx-1"></div>

                <!-- Admin Profile Card -->
                <div class="flex items-center gap-2.5">
                    <div class="w-9 h-9 rounded-full bg-gradient-to-tr from-sky-600 to-indigo-600 text-white flex items-center justify-center font-black text-xs shadow-sm">
                        HL
                    </div>
                    <div class="hidden lg:block text-left">
                        <div class="text-xs font-bold text-slate-800 leading-tight">Hoàng Long</div>
                        <div class="text-[10px] text-sky-600 font-semibold">Quản Trị Viên Cấp Cao</div>
                    </div>
                    <button @click="logout()" class="text-xs bg-rose-50 text-rose-600 border border-rose-200 p-2 lg:px-2.5 lg:py-1.5 rounded-xl font-bold hover:bg-rose-100 transition flex items-center gap-1.5" title="Đăng xuất">
                        <i class="fa-solid fa-power-off text-xs"></i>
                        <span class="hidden xl:inline">Thoát</span>
                    </button>
                </div>
            </div>
        </header>

        <!-- MAIN LAYOUT: SIDEBAR + CONTENT -->
        <div class="flex-1 flex overflow-hidden">
            
            <!-- SIDEBAR ADMIN CHUYÊN NGHIỆP -->
            <aside x-show="sidebarOpen" class="w-64 bg-white border-r border-slate-200 flex flex-col shrink-0 transition-all duration-200 select-none">
                <div class="p-3 space-y-1 overflow-y-auto flex-1">
                    
                    <div class="px-3 pt-2 pb-1 text-[11px] font-bold text-slate-400 uppercase tracking-wider">Báo cáo & Giám sát</div>
                    
                    <!-- 1. DASHBOARD BÁO CÁO -->
                    <button @click="switchAdminTab('dashboard')" :class="activeAdminTab === 'dashboard' ? 'bg-sky-50 text-sky-700 font-bold border-r-4 border-sky-600 shadow-2xs' : 'text-slate-600 hover:bg-slate-50 font-medium'" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs transition text-left">
                        <i class="fa-solid fa-chart-line text-sm w-4 text-center text-sky-600"></i>
                        <span class="flex-1">Dashboard Tổng Quan</span>
                    </button>

                    <div class="px-3 pt-3 pb-1 text-[11px] font-bold text-slate-400 uppercase tracking-wider">Kinh Doanh & Dịch Vụ</div>

                    <!-- 2. QUẢN LÝ ĐƠN HÀNG -->
                    <button @click="switchAdminTab('orders')" :class="activeAdminTab === 'orders' ? 'bg-sky-50 text-sky-700 font-bold border-r-4 border-sky-600 shadow-2xs' : 'text-slate-600 hover:bg-slate-50 font-medium'" class="w-full flex items-center justify-between px-3 py-2.5 rounded-xl text-xs transition text-left">
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-bag-shopping text-sm w-4 text-center text-blue-600"></i>
                            <span>Quản lý Đơn hàng</span>
                        </div>
                        <span class="bg-blue-100 text-blue-800 text-[10px] font-bold px-1.5 py-0.5 rounded-full" x-text="adminRecentOrders.length"></span>
                    </button>

                    <!-- 3. QUẢN LÝ DỊCH VỤ -->
                    <button @click="switchAdminTab('services')" :class="activeAdminTab === 'services' ? 'bg-sky-50 text-sky-700 font-bold border-r-4 border-sky-600 shadow-2xs' : 'text-slate-600 hover:bg-slate-50 font-medium'" class="w-full flex items-center justify-between px-3 py-2.5 rounded-xl text-xs transition text-left">
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-scissors text-sm w-4 text-center text-teal-600"></i>
                            <span>Quản lý Dịch vụ</span>
                        </div>
                        <span class="bg-teal-100 text-teal-800 text-[10px] font-bold px-1.5 py-0.5 rounded-full" x-text="adminServicesList.length"></span>
                    </button>

                    <!-- 4. QUẢN LÝ TỒN KHO -->
                    <button @click="switchAdminTab('inventory')" :class="activeAdminTab === 'inventory' ? 'bg-sky-50 text-sky-700 font-bold border-r-4 border-sky-600 shadow-2xs' : 'text-slate-600 hover:bg-slate-50 font-medium'" class="w-full flex items-center justify-between px-3 py-2.5 rounded-xl text-xs transition text-left">
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-boxes-stacked text-sm w-4 text-center text-amber-600"></i>
                            <span>Quản lý Tồn Kho</span>
                        </div>
                        <span class="bg-amber-100 text-amber-800 text-[10px] font-bold px-1.5 py-0.5 rounded-full" x-text="inventoryItems.length"></span>
                    </button>

                    <!-- 5. QUẢN LÝ HOTEL -->
                    <button @click="switchAdminTab('hotel')" :class="activeAdminTab === 'hotel' ? 'bg-sky-50 text-sky-700 font-bold border-r-4 border-sky-600 shadow-2xs' : 'text-slate-600 hover:bg-slate-50 font-medium'" class="w-full flex items-center justify-between px-3 py-2.5 rounded-xl text-xs transition text-left">
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-hotel text-sm w-4 text-center text-indigo-600"></i>
                            <span>Quản lý Hotel</span>
                        </div>
                        <span class="bg-indigo-100 text-indigo-800 text-[10px] font-bold px-1.5 py-0.5 rounded-full">40 Phòng</span>
                    </button>

                    <!-- 9. FLOW PETSHIP (ĐIỀU PHỐI VẬN CHUYỂN) -->
                    <button @click="switchAdminTab('petship')" :class="activeAdminTab === 'petship' ? 'bg-sky-50 text-sky-700 font-bold border-r-4 border-sky-600 shadow-2xs' : 'text-slate-600 hover:bg-slate-50 font-medium'" class="w-full flex items-center justify-between px-3 py-2.5 rounded-xl text-xs transition text-left">
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-truck-fast text-sm w-4 text-center text-emerald-600"></i>
                            <span>Điều phối PetShip</span>
                        </div>
                        <span class="bg-emerald-100 text-emerald-800 text-[10px] font-bold px-1.5 py-0.5 rounded-full">Live</span>
                    </button>

                    <div class="px-3 pt-3 pb-1 text-[11px] font-bold text-slate-400 uppercase tracking-wider">Vận Hành & Khách Hàng</div>

                    <!-- 6. QUẢN LÝ NHÂN SỰ -->
                    <button @click="switchAdminTab('staff')" :class="activeAdminTab === 'staff' ? 'bg-sky-50 text-sky-700 font-bold border-r-4 border-sky-600 shadow-2xs' : 'text-slate-600 hover:bg-slate-50 font-medium'" class="w-full flex items-center justify-between px-3 py-2.5 rounded-xl text-xs transition text-left">
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-id-badge text-sm w-4 text-center text-purple-600"></i>
                            <span>Quản lý Nhân sự</span>
                        </div>
                        <span class="bg-purple-100 text-purple-800 text-[10px] font-bold px-1.5 py-0.5 rounded-full" x-text="staffList.length"></span>
                    </button>

                    <!-- 7. QUẢN LÝ KHÁCH HÀNG -->
                    <button @click="switchAdminTab('customers')" :class="activeAdminTab === 'customers' ? 'bg-sky-50 text-sky-700 font-bold border-r-4 border-sky-600 shadow-2xs' : 'text-slate-600 hover:bg-slate-50 font-medium'" class="w-full flex items-center justify-between px-3 py-2.5 rounded-xl text-xs transition text-left">
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-users text-sm w-4 text-center text-sky-600"></i>
                            <span>Quản lý Khách hàng</span>
                        </div>
                        <span class="bg-sky-100 text-sky-800 text-[10px] font-bold px-1.5 py-0.5 rounded-full" x-text="adminCustomersList.length"></span>
                    </button>

                    <!-- 8. HỒ SƠ THÚ CƯNG -->
                    <button @click="switchAdminTab('pets')" :class="activeAdminTab === 'pets' ? 'bg-sky-50 text-sky-700 font-bold border-r-4 border-sky-600 shadow-2xs' : 'text-slate-600 hover:bg-slate-50 font-medium'" class="w-full flex items-center justify-between px-3 py-2.5 rounded-xl text-xs transition text-left">
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-paw text-sm w-4 text-center text-rose-600"></i>
                            <span>Hồ sơ Thú cưng</span>
                        </div>
                        <span class="bg-rose-100 text-rose-800 text-[10px] font-bold px-1.5 py-0.5 rounded-full" x-text="adminPetProfilesList.length"></span>
                    </button>

                </div>

                <!-- Footer Sidebar -->
                <div class="p-3 border-t border-slate-100 bg-slate-50 text-center">
                    <div class="text-[11px] font-bold text-slate-600">PetCare360 Enterprise v4.2</div>
                    <div class="text-[10px] text-slate-400">Đồng bộ Cloud Realtime 24/7</div>
                </div>
            </aside>

            <!-- MAIN WORKSPACE CONTAINER (Desktop-first 1440px) -->
            <main class="flex-1 overflow-y-auto bg-slate-50/80 p-4 md:p-6 lg:p-8">
                <div class="max-w-[1440px] mx-auto space-y-6">

                    <!-- ======================================================== -->
                    <!-- MODULE 1: DASHBOARD BÁO CÁO, PHÂN TÍCH DOANH THU & WEB -->
                    <!-- ======================================================== -->
                    <section x-show="activeAdminTab === 'dashboard'" class="space-y-6 animate-fadeIn">
                        
                        <!-- Header & Filters (Mục 2) -->
                        <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4 bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs">
                            <div>
                                <h1 class="text-xl md:text-2xl font-black text-slate-900 tracking-tight flex items-center gap-2.5">
                                    <i class="fa-solid fa-chart-pie text-sky-600"></i>
                                    <span>Báo cáo & Phân tích tổng quan</span>
                                </h1>
                                <p class="text-xs text-slate-500 mt-1">
                                    Theo dõi các chỉ số doanh thu kinh doanh, lưu lượng truy cập website và hiệu quả bán hàng đa kênh PetCare360.
                                </p>
                            </div>

                            <!-- Bộ lọc thời gian nhanh & Nút hành động -->
                            <div class="flex flex-wrap items-center gap-2.5">
                                <!-- ButtonGroup Thời gian -->
                                <div class="inline-flex rounded-xl p-1 bg-slate-100 border border-slate-200 text-xs font-semibold">
                                    <button @click="applyAdminDashboardTimeFilter('today')" :class="adminDashboardTimeFilter === 'today' ? 'bg-sky-600 text-white font-bold shadow-xs' : 'text-slate-600 hover:text-slate-900'" class="px-2.5 py-1.5 rounded-lg transition">Hôm nay</button>
                                    <button @click="applyAdminDashboardTimeFilter('yesterday')" :class="adminDashboardTimeFilter === 'yesterday' ? 'bg-sky-600 text-white font-bold shadow-xs' : 'text-slate-600 hover:text-slate-900'" class="px-2.5 py-1.5 rounded-lg transition">Hôm qua</button>
                                    <button @click="applyAdminDashboardTimeFilter('7days')" :class="adminDashboardTimeFilter === '7days' ? 'bg-sky-600 text-white font-bold shadow-xs' : 'text-slate-600 hover:text-slate-900'" class="px-2.5 py-1.5 rounded-lg transition">7 ngày qua</button>
                                    <button @click="applyAdminDashboardTimeFilter('this_month')" :class="adminDashboardTimeFilter === 'this_month' ? 'bg-sky-600 text-white font-bold shadow-xs' : 'text-slate-600 hover:text-slate-900'" class="px-2.5 py-1.5 rounded-lg transition">Tháng này</button>
                                    <button @click="applyAdminDashboardTimeFilter('custom')" :class="adminDashboardTimeFilter === 'custom' ? 'bg-sky-600 text-white font-bold shadow-xs' : 'text-slate-600 hover:text-slate-900'" class="px-2.5 py-1.5 rounded-lg transition">Tùy chỉnh ngày</button>
                                </div>

                                <!-- Action buttons -->
                                <button @click="exportAdminReport()" class="px-3 py-2 rounded-xl border border-slate-300 hover:bg-slate-50 text-slate-700 font-bold text-xs transition flex items-center gap-1.5 shadow-2xs">
                                    <i class="fa-solid fa-file-arrow-down text-slate-500"></i>
                                    <span>Xuất báo cáo Excel/PDF</span>
                                </button>
                                <button @click="refreshAdminData()" class="px-3.5 py-2 rounded-xl bg-sky-600 hover:bg-sky-700 text-white font-bold text-xs transition flex items-center gap-1.5 shadow-sm shadow-sky-500/20">
                                    <i class="fa-solid fa-arrows-rotate"></i>
                                    <span>Làm mới dữ liệu</span>
                                </button>
                            </div>
                        </div>

                        <!-- 4 Thẻ Chỉ Số Nhanh (Metric Summary Cards - Mục 3) -->
                        <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-4">
                            <!-- Card 1: Tổng doanh thu -->
                            <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-md transition">
                                <div class="flex items-center justify-between mb-3">
                                    <span class="text-xs font-bold text-slate-500 uppercase tracking-wider">Tổng doanh thu</span>
                                    <div class="w-10 h-10 rounded-xl bg-sky-50 text-sky-600 flex items-center justify-center text-base">
                                        <i class="fa-solid fa-sack-dollar"></i>
                                    </div>
                                </div>
                                <div class="text-2xl font-black text-slate-900 tracking-tight" x-text="adminRevenueMetrics.totalRevenueFormatted"></div>
                                <div class="flex items-center gap-1.5 mt-2.5">
                                    <span class="inline-flex items-center gap-1 text-xs font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-md">
                                        <i class="fa-solid fa-arrow-trend-up"></i>
                                        <span x-text="adminRevenueMetrics.growthRevenue"></span>
                                    </span>
                                    <span class="text-[11px] text-slate-400">so với kỳ trước</span>
                                </div>
                            </div>

                            <!-- Card 2: Tổng số đơn hàng -->
                            <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-md transition">
                                <div class="flex items-center justify-between mb-3">
                                    <span class="text-xs font-bold text-slate-500 uppercase tracking-wider">Tổng số đơn hàng</span>
                                    <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center text-base">
                                        <i class="fa-solid fa-cart-shopping"></i>
                                    </div>
                                </div>
                                <div class="text-2xl font-black text-slate-900 tracking-tight" x-text="adminRevenueMetrics.totalOrders + ' đơn'"></div>
                                <div class="flex items-center justify-between text-[11px] text-slate-500 mt-2.5">
                                    <span class="inline-flex items-center gap-1 text-xs font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-md">
                                        <i class="fa-solid fa-arrow-trend-up"></i>
                                        <span x-text="adminRevenueMetrics.growthOrders"></span>
                                    </span>
                                    <span class="font-medium">Xong: <strong class="text-slate-800" x-text="adminRevenueMetrics.completedOrders"></strong> | Đang làm: <strong class="text-amber-600" x-text="adminRevenueMetrics.processingOrders"></strong></span>
                                </div>
                            </div>

                            <!-- Card 3: Giá trị trung bình mỗi đơn (AOV) -->
                            <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-md transition">
                                <div class="flex items-center justify-between mb-3">
                                    <span class="text-xs font-bold text-slate-500 uppercase tracking-wider">Giá trị TB mỗi đơn (AOV)</span>
                                    <div class="w-10 h-10 rounded-xl bg-indigo-50 text-indigo-600 flex items-center justify-center text-base">
                                        <i class="fa-solid fa-receipt"></i>
                                    </div>
                                </div>
                                <div class="text-2xl font-black text-slate-900 tracking-tight" x-text="adminRevenueMetrics.aovFormatted"></div>
                                <div class="flex items-center gap-1.5 mt-2.5">
                                    <span class="inline-flex items-center gap-1 text-xs font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-md">
                                        <i class="fa-solid fa-arrow-trend-up"></i>
                                        <span x-text="adminRevenueMetrics.growthAov"></span>
                                    </span>
                                    <span class="text-[11px] text-slate-400">so với kỳ trước</span>
                                </div>
                            </div>

                            <!-- Card 4: Lượng truy cập website -->
                            <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-md transition">
                                <div class="flex items-center justify-between mb-3">
                                    <span class="text-xs font-bold text-slate-500 uppercase tracking-wider">Lượng truy cập website</span>
                                    <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center text-base">
                                        <i class="fa-solid fa-globe"></i>
                                    </div>
                                </div>
                                <div class="text-2xl font-black text-slate-900 tracking-tight" x-text="adminRevenueMetrics.websiteTraffic.pageviews"></div>
                                <div class="flex items-center justify-between text-[11px] text-slate-500 mt-2.5">
                                    <span class="inline-flex items-center gap-1 text-xs font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-md">
                                        <i class="fa-solid fa-arrow-trend-up"></i>
                                        <span x-text="adminRevenueMetrics.growthTraffic"></span>
                                    </span>
                                    <span class="font-medium"><strong class="text-slate-800" x-text="adminRevenueMetrics.websiteTraffic.visitors"></strong> người truy cập</span>
                                </div>
                            </div>
                        </div>

                        <!-- Khu vực Biểu đồ Phân tích Doanh thu (Revenue Analytics Chart - Mục 4) -->
                        <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs space-y-4">
                            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 pb-3">
                                <div>
                                    <h3 class="text-base font-bold text-slate-900 flex items-center gap-2">
                                        <i class="fa-solid fa-chart-column text-sky-600"></i>
                                        <span>Xu Hướng Tăng Trưởng Doanh Thu & Đơn Hàng</span>
                                    </h3>
                                    <p class="text-xs text-slate-400">Biểu đồ đường biểu diễn dữ liệu thời gian thực theo từng mốc chu kỳ.</p>
                                </div>

                                <!-- Bộ lọc nhỏ góc trên biểu đồ: Doanh thu / Lợi nhuận / Số lượng đơn hàng -->
                                <div class="inline-flex rounded-xl p-1 bg-slate-100 border border-slate-200 text-xs font-bold">
                                    <button @click="setDashboardChartMetric('revenue')" :class="dashboardChartMetric === 'revenue' ? 'bg-sky-600 text-white shadow-2xs' : 'text-slate-600 hover:text-slate-900'" class="px-3 py-1.5 rounded-lg transition">Doanh thu</button>
                                    <button @click="setDashboardChartMetric('profit')" :class="dashboardChartMetric === 'profit' ? 'bg-sky-600 text-white shadow-2xs' : 'text-slate-600 hover:text-slate-900'" class="px-3 py-1.5 rounded-lg transition">Lợi nhuận</button>
                                    <button @click="setDashboardChartMetric('orders')" :class="dashboardChartMetric === 'orders' ? 'bg-sky-600 text-white shadow-2xs' : 'text-slate-600 hover:text-slate-900'" class="px-3 py-1.5 rounded-lg transition">Số lượng đơn hàng</button>
                                </div>
                            </div>

                            <!-- Canvas Chart.js -->
                            <div class="relative w-full h-80 pt-2">
                                <canvas id="adminRevenueMainChart" class="w-full h-full"></canvas>
                            </div>
                        </div>

                        <!-- Thống kê Hiệu suất Website (Traffic & Conversion - Mục 5) -->
                        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                            
                            <!-- Thẻ 1: Nguồn lưu lượng Traffic -->
                            <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs space-y-4">
                                <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                                    <h3 class="text-sm font-bold text-slate-900 flex items-center gap-2">
                                        <i class="fa-solid fa-chart-pie text-teal-600"></i>
                                        <span>Nguồn Lưu Lượng Truy Cập Website</span>
                                    </h3>
                                    <span class="text-xs text-slate-400">100% Tổng lượng</span>
                                </div>

                                <div class="space-y-3.5 pt-1">
                                    <template x-for="item in adminTrafficSources" :key="item.source">
                                        <div>
                                            <div class="flex justify-between items-center text-xs mb-1">
                                                <span class="font-bold text-slate-700 flex items-center gap-2">
                                                    <span class="w-2.5 h-2.5 rounded-full" :class="item.colorClass"></span>
                                                    <span x-text="item.source"></span>
                                                </span>
                                                <span class="font-black text-slate-900" x-text="item.percent + '%'"></span>
                                            </div>
                                            <div class="w-full h-2.5 bg-slate-100 rounded-full overflow-hidden">
                                                <div class="h-full rounded-full transition-all duration-500" :class="item.colorClass" :style="'width: ' + item.percent + '%'"></div>
                                            </div>
                                        </div>
                                    </template>
                                </div>
                            </div>

                            <!-- Thẻ 2: Phễu Tỷ Lệ Chuyển Đổi (Conversion Funnel) -->
                            <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs space-y-4">
                                <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                                    <h3 class="text-sm font-bold text-slate-900 flex items-center gap-2">
                                        <i class="fa-solid fa-filter text-indigo-600"></i>
                                        <span>Phễu Tỷ Lệ Chuyển Đổi (Conversion Rate)</span>
                                    </h3>
                                    <span class="text-xs font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-md">CR Trung bình 3.36%</span>
                                </div>

                                <div class="space-y-3 pt-1">
                                    <template x-for="(stage, idx) in adminConversionFunnel" :key="stage.step">
                                        <div class="p-3 rounded-xl bg-slate-50 border border-slate-100 flex items-center justify-between">
                                            <div class="flex items-center gap-3">
                                                <div class="w-7 h-7 rounded-lg bg-sky-100 text-sky-800 font-black text-xs flex items-center justify-center" x-text="idx + 1"></div>
                                                <div>
                                                    <div class="text-xs font-bold text-slate-800" x-text="stage.step"></div>
                                                    <div class="text-[11px] text-slate-400" x-text="stage.count + ' lượt'"></div>
                                                </div>
                                            </div>
                                            <div class="text-right">
                                                <div class="text-xs font-black text-sky-700" x-text="stage.percent + '%'"></div>
                                                <div class="w-24 h-1.5 bg-slate-200 rounded-full mt-1 overflow-hidden">
                                                    <div class="h-full bg-sky-600 rounded-full" :style="'width: ' + stage.percent + '%'"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </template>
                                </div>
                            </div>
                        </div>

                        <!-- Bảng Dữ Liệu Chi Tiết Bổ Sung (Split View Data Tables - Mục 6) -->
                        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                            
                            <!-- Bảng 1: Top Sản Phẩm Bán Chạy -->
                            <div class="bg-white rounded-2xl border border-slate-200/80 shadow-xs overflow-hidden">
                                <div class="p-4 border-b border-slate-100 flex items-center justify-between">
                                    <h3 class="text-sm font-bold text-slate-900 flex items-center gap-2">
                                        <i class="fa-solid fa-trophy text-amber-500"></i>
                                        <span>Top Sản Phẩm Bán Chạy</span>
                                    </h3>
                                    <button @click="switchAdminTab('inventory')" class="text-xs font-bold text-sky-600 hover:text-sky-700">Xem tất cả</button>
                                </div>
                                <div class="overflow-x-auto">
                                    <table class="w-full text-left text-xs">
                                        <thead class="bg-slate-50/70 text-slate-500 border-b border-slate-100 uppercase tracking-wider font-bold">
                                            <tr>
                                                <th class="py-2.5 px-3">Sản phẩm</th>
                                                <th class="py-2.5 px-3 text-center">Đã bán</th>
                                                <th class="py-2.5 px-3 text-right">Tổng doanh thu</th>
                                            </tr>
                                        </thead>
                                        <tbody class="divide-y divide-slate-100 font-medium text-slate-700">
                                            <template x-for="p in adminTopProducts" :key="p.sku">
                                                <tr class="hover:bg-slate-50/80 transition">
                                                    <td class="py-3 px-3 flex items-center gap-2.5">
                                                        <img :src="p.image" class="w-9 h-9 rounded-lg object-cover border border-slate-200 shrink-0">
                                                        <div>
                                                            <div class="font-bold text-slate-900 leading-tight" x-text="p.name"></div>
                                                            <div class="text-[10px] text-slate-400 font-mono" x-text="p.sku"></div>
                                                        </div>
                                                    </td>
                                                    <td class="py-3 px-3 text-center font-bold text-slate-800" x-text="p.sold + ' cái'"></td>
                                                    <td class="py-3 px-3 text-right font-black text-sky-700" x-text="formatCurrency(p.revenue)"></td>
                                                </tr>
                                            </template>
                                        </tbody>
                                    </table>
                                </div>
                            </div>

                            <!-- Bảng 2: Đơn Hàng Mới Nhất Cần Xử Lý -->
                            <div class="bg-white rounded-2xl border border-slate-200/80 shadow-xs overflow-hidden">
                                <div class="p-4 border-b border-slate-100 flex items-center justify-between">
                                    <h3 class="text-sm font-bold text-slate-900 flex items-center gap-2">
                                        <i class="fa-solid fa-clock text-blue-600"></i>
                                        <span>Đơn Hàng Mới Nhất Cần Xử Lý</span>
                                    </h3>
                                    <button @click="switchAdminTab('orders')" class="text-xs font-bold text-sky-600 hover:text-sky-700">Xem tất cả</button>
                                </div>
                                <div class="overflow-x-auto">
                                    <table class="w-full text-left text-xs">
                                        <thead class="bg-slate-50/70 text-slate-500 border-b border-slate-100 uppercase tracking-wider font-bold">
                                            <tr>
                                                <th class="py-2.5 px-3">Mã đơn</th>
                                                <th class="py-2.5 px-3">Khách hàng</th>
                                                <th class="py-2.5 px-3 text-right">Tổng tiền</th>
                                                <th class="py-2.5 px-3 text-center">Trạng thái</th>
                                                <th class="py-2.5 px-3 text-center">Hành động</th>
                                            </tr>
                                        </thead>
                                        <tbody class="divide-y divide-slate-100 font-medium text-slate-700">
                                            <template x-for="order in adminRecentOrders" :key="order.orderId">
                                                <tr class="hover:bg-slate-50/80 transition">
                                                    <td class="py-3 px-3 font-mono font-bold text-sky-700" x-text="order.orderId"></td>
                                                    <td class="py-3 px-3">
                                                        <div class="font-bold text-slate-900" x-text="order.customerName"></div>
                                                        <div class="text-[10px] text-slate-400" x-text="order.customerPhone"></div>
                                                    </td>
                                                    <td class="py-3 px-3 text-right font-black text-slate-900" x-text="formatCurrency(order.total)"></td>
                                                    <td class="py-3 px-3 text-center">
                                                        <span :class="getOrderStatusBadgeClass(order.status)" class="px-2 py-0.5 rounded-full text-[10px] font-bold" x-text="getOrderStatusLabel(order.status)"></span>
                                                    </td>
                                                    <td class="py-3 px-3 text-center">
                                                        <button @click="openAdminOrderDetail(order)" class="px-2.5 py-1 bg-sky-50 hover:bg-sky-100 text-sky-700 border border-sky-200 rounded-lg text-xs font-bold transition">
                                                            Chi tiết
                                                        </button>
                                                    </td>
                                                </tr>
                                            </template>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>

                    </section>

                    <!-- ======================================================== -->
                    <!-- MODULE 2: QUẢN LÝ ĐƠN HÀNG (ORDER MANAGEMENT) -->
                    <!-- ======================================================== -->
                    <section x-show="activeAdminTab === 'orders'" class="space-y-4 animate-fadeIn">
                        
                        <!-- Header & Search Toolbar -->
                        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-white p-4 rounded-2xl border border-slate-200/80 shadow-xs">
                            <div>
                                <h2 class="text-xl font-black text-slate-900 flex items-center gap-2">
                                    <i class="fa-solid fa-bag-shopping text-sky-600"></i>
                                    <span>Quản lý đơn hàng</span>
                                </h2>
                                <p class="text-xs text-slate-500">Tra cứu, cập nhật trạng thái và xuất hóa đơn bán hàng PetCare360.</p>
                            </div>

                            <div class="flex items-center gap-2">
                                <div class="relative w-64">
                                    <input type="text" placeholder="Tìm theo mã đơn, khách, SĐT..." class="w-full bg-slate-50 border border-slate-200 rounded-xl pl-8 pr-3 py-1.5 text-xs focus:outline-none focus:border-sky-500">
                                    <i class="fa-solid fa-magnifying-glass absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400 text-xs"></i>
                                </div>
                                <button class="px-3 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs font-bold border border-slate-200 transition flex items-center gap-1.5">
                                    <i class="fa-solid fa-filter text-xs"></i>
                                    <span>Bộ lọc</span>
                                </button>
                                <button @click="exportOrdersData()" class="px-3 py-1.5 bg-sky-600 hover:bg-sky-700 text-white rounded-xl text-xs font-bold shadow-xs transition flex items-center gap-1.5">
                                    <i class="fa-solid fa-download text-xs"></i>
                                    <span>Xuất dữ liệu</span>
                                </button>
                            </div>
                        </div>

                        <!-- Data Table 7 Cột Chuẩn Yêu Cầu -->
                        <div class="bg-white rounded-2xl border border-slate-200/80 shadow-xs overflow-hidden">
                            <div class="overflow-x-auto">
                                <table class="w-full text-left text-xs">
                                    <thead class="bg-slate-50 text-slate-500 border-b border-slate-200 uppercase tracking-wider font-bold">
                                        <tr>
                                            <th class="py-3 px-4">Mã đơn hàng</th>
                                            <th class="py-3 px-4">Khách hàng</th>
                                            <th class="py-3 px-4 text-right">Tổng tiền</th>
                                            <th class="py-3 px-4 text-center">Phương thức thanh toán</th>
                                            <th class="py-3 px-4">Ghi chú</th>
                                            <th class="py-3 px-4 text-center">Trạng thái</th>
                                            <th class="py-3 px-4 text-center">Thao tác</th>
                                        </tr>
                                    </thead>
                                    <tbody class="divide-y divide-slate-100 font-medium text-slate-700">
                                        <template x-for="order in adminRecentOrders" :key="order.orderId">
                                            <tr class="hover:bg-slate-50 transition">
                                                <!-- Cột 1: Mã đơn hàng -->
                                                <td class="py-3.5 px-4">
                                                    <button @click="openAdminOrderDetail(order)" class="font-mono font-bold text-sky-600 hover:text-sky-800 hover:underline" x-text="order.orderId"></button>
                                                </td>

                                                <!-- Cột 2: Khách hàng -->
                                                <td class="py-3.5 px-4">
                                                    <div class="font-bold text-slate-900" x-text="order.customerName"></div>
                                                    <div class="text-[11px] text-slate-400" x-text="order.customerEmail || order.customerPhone"></div>
                                                </td>

                                                <!-- Cột 3: Tổng tiền -->
                                                <td class="py-3.5 px-4 text-right font-black text-slate-900" x-text="formatCurrency(order.total)"></td>

                                                <!-- Cột 4: Phương thức thanh toán -->
                                                <td class="py-3.5 px-4 text-center">
                                                    <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-slate-100 font-bold text-slate-700">
                                                        <i :class="order.paymentMethod === 'momo' ? 'fa-solid fa-wallet text-pink-600' : (order.paymentMethod === 'vietqr' ? 'fa-solid fa-qrcode text-blue-600' : 'fa-solid fa-money-bill-1-wave text-emerald-600')"></i>
                                                        <span x-text="order.paymentMethod.toUpperCase()"></span>
                                                    </span>
                                                </td>

                                                <!-- Cột 5: Ghi chú (truncate & hover full) -->
                                                <td class="py-3.5 px-4 max-w-xs">
                                                    <div class="truncate text-slate-500 cursor-pointer" :title="order.notes" x-text="order.notes || 'Không có ghi chú'"></div>
                                                </td>

                                                <!-- Cột 6: Trạng thái (Badge màu chuẩn) -->
                                                <td class="py-3.5 px-4 text-center">
                                                    <span :class="getOrderStatusBadgeClass(order.status)" class="px-2.5 py-1 rounded-full text-[11px] font-bold" x-text="getOrderStatusLabel(order.status)"></span>
                                                </td>

                                                <!-- Cột 7: Thao tác -->
                                                <td class="py-3.5 px-4 text-center">
                                                    <button @click="openAdminOrderDetail(order)" class="px-3 py-1.5 bg-sky-50 hover:bg-sky-100 text-sky-700 border border-sky-200 rounded-xl font-bold transition flex items-center gap-1 mx-auto">
                                                        <i class="fa-solid fa-eye text-xs"></i>
                                                        <span>Chi tiết</span>
                                                    </button>
                                                </td>
                                            </tr>
                                        </template>
                                    </tbody>
                                </table>
                            </div>

                            <!-- Pagination -->
                            <div class="p-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
                                <span>Hiển thị 1 - 4 của 1,284 đơn hàng</span>
                                <div class="flex items-center gap-1">
                                    <button class="px-2.5 py-1 rounded-lg border border-slate-200 hover:bg-slate-50 disabled:opacity-50" disabled>Trang trước</button>
                                    <button class="px-2.5 py-1 rounded-lg bg-sky-600 text-white font-bold">1</button>
                                    <button class="px-2.5 py-1 rounded-lg border border-slate-200 hover:bg-slate-50">2</button>
                                    <button class="px-2.5 py-1 rounded-lg border border-slate-200 hover:bg-slate-50">3</button>
                                    <button class="px-2.5 py-1 rounded-lg border border-slate-200 hover:bg-slate-50">Trang sau</button>
                                </div>
                            </div>
                        </div>

                    </section>

                    <!-- ======================================================== -->
                    <!-- MODULE 3: QUẢN LÝ DỊCH VỤ (SERVICE MANAGEMENT) -->
                    <!-- ======================================================== -->
                    <section x-show="activeAdminTab === 'services'" class="space-y-4 animate-fadeIn">
                        
                        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-white p-4 rounded-2xl border border-slate-200/80 shadow-xs">
                            <div>
                                <h2 class="text-xl font-black text-slate-900 flex items-center gap-2">
                                    <i class="fa-solid fa-scissors text-teal-600"></i>
                                    <span>Quản lý Dịch vụ & Đặt chỗ</span>
                                </h2>
                                <p class="text-xs text-slate-500">Theo dõi lịch hẹn Spa, Hotel, Grooming và quản lý hồ sơ thú cưng đặt chỗ.</p>
                            </div>

                            <div class="flex items-center gap-2">
                                <div class="relative w-64">
                                    <input type="text" placeholder="Tìm theo mã DV, khách, thú cưng..." class="w-full bg-slate-50 border border-slate-200 rounded-xl pl-8 pr-3 py-1.5 text-xs focus:outline-none focus:border-teal-500">
                                    <i class="fa-solid fa-magnifying-glass absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400 text-xs"></i>
                                </div>
                                <select class="bg-slate-50 border border-slate-200 rounded-xl px-2.5 py-1.5 text-xs font-semibold text-slate-700">
                                    <option value="ALL">Tất cả gói</option>
                                    <option value="HOTEL">Hotel</option>
                                    <option value="SPA">Spa</option>
                                    <option value="GROOMING">Grooming</option>
                                </select>
                            </div>
                        </div>

                        <!-- Data Table 10 Cột Đúng Thứ Tự -->
                        <div class="bg-white rounded-2xl border border-slate-200/80 shadow-xs overflow-hidden">
                            <div class="overflow-x-auto">
                                <table class="w-full text-left text-xs">
                                    <thead class="bg-slate-50 text-slate-500 border-b border-slate-200 uppercase tracking-wider font-bold">
                                        <tr>
                                            <th class="py-3 px-3">Mã DV</th>
                                            <th class="py-3 px-3">Khách hàng</th>
                                            <th class="py-3 px-3">Thú cưng</th>
                                            <th class="py-3 px-3 text-center">Gói DV</th>
                                            <th class="py-3 px-3">Thời gian</th>
                                            <th class="py-3 px-3 text-right">Tổng tiền</th>
                                            <th class="py-3 px-3 text-center">Phương thức</th>
                                            <th class="py-3 px-3 text-center">PetShip</th>
                                            <th class="py-3 px-3 text-center">Trạng thái</th>
                                            <th class="py-3 px-3 text-center">Thao tác</th>
                                        </tr>
                                    </thead>
                                    <tbody class="divide-y divide-slate-100 font-medium text-slate-700">
                                        <template x-for="srv in adminServicesList" :key="srv.serviceId">
                                            <tr class="hover:bg-slate-50 transition">
                                                <!-- 1. Mã DV -->
                                                <td class="py-3.5 px-3">
                                                    <button @click="openAdminServiceDetail(srv)" class="font-mono font-bold text-teal-600 hover:underline" x-text="srv.serviceId"></button>
                                                </td>

                                                <!-- 2. Khách hàng -->
                                                <td class="py-3.5 px-3">
                                                    <div class="font-bold text-slate-900" x-text="srv.customerName"></div>
                                                    <div class="text-[10px] text-slate-400" x-text="srv.customerPhone"></div>
                                                </td>

                                                <!-- 3. Thú cưng -->
                                                <td class="py-3.5 px-3">
                                                    <div class="flex items-center gap-2">
                                                        <img :src="srv.petAvatar" class="w-8 h-8 rounded-full object-cover border border-slate-200">
                                                        <div>
                                                            <div class="font-bold text-slate-900" x-text="srv.petName"></div>
                                                            <div class="text-[10px] text-slate-400" x-text="srv.petBreed"></div>
                                                        </div>
                                                    </div>
                                                </td>

                                                <!-- 4. Gói DV -->
                                                <td class="py-3.5 px-3 text-center">
                                                    <span :class="srv.servicePackage === 'Hotel' ? 'bg-indigo-100 text-indigo-800' : (srv.servicePackage === 'Spa' ? 'bg-pink-100 text-pink-800' : 'bg-teal-100 text-teal-800')" class="px-2 py-0.5 rounded-full text-[10px] font-bold" x-text="srv.servicePackage"></span>
                                                </td>

                                                <!-- 5. Thời gian -->
                                                <td class="py-3.5 px-3">
                                                    <div class="text-slate-800 font-semibold" x-text="srv.checkInTime"></div>
                                                    <div class="text-[10px] text-slate-400" x-text="'Ra: ' + srv.checkOutTime"></div>
                                                </td>

                                                <!-- 6. Tổng tiền -->
                                                <td class="py-3.5 px-3 text-right font-black text-slate-900" x-text="formatCurrency(srv.total)"></td>

                                                <!-- 7. Phương thức TT -->
                                                <td class="py-3.5 px-3 text-center font-bold text-slate-600" x-text="srv.paymentMethod"></td>

                                                <!-- 8. PetShip -->
                                                <td class="py-3.5 px-3 text-center">
                                                    <span :class="srv.petShipShipper === 'Không có' ? 'text-slate-400' : 'text-emerald-700 font-bold bg-emerald-50 px-2 py-0.5 rounded-md'" x-text="srv.petShipShipper"></span>
                                                </td>

                                                <!-- 9. Trạng thái -->
                                                <td class="py-3.5 px-3 text-center">
                                                    <span :class="srv.depositStatus === 'Đã cọc' ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'" class="px-2 py-0.5 rounded-full text-[10px] font-bold" x-text="srv.depositStatus"></span>
                                                </td>

                                                <!-- 10. Thao tác -->
                                                <td class="py-3.5 px-3 text-center">
                                                    <button @click="openAdminServiceDetail(srv)" class="px-2.5 py-1 bg-teal-50 hover:bg-teal-100 text-teal-700 border border-teal-200 rounded-lg font-bold transition">
                                                        Chi tiết
                                                    </button>
                                                </td>
                                            </tr>
                                        </template>
                                    </tbody>
                                </table>
                            </div>
                        </div>

                    </section>

                    <!-- ======================================================== -->
                    <!-- MODULE 4: QUẢN LÝ TỒN KHO (INVENTORY MANAGEMENT) -->
                    <!-- ======================================================== -->
                    <section x-show="activeAdminTab === 'inventory'" class="space-y-4 animate-fadeIn">
                        
                        <!-- Toolbar -->
                        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-white p-4 rounded-2xl border border-slate-200/80 shadow-xs">
                            <div>
                                <h2 class="text-xl font-black text-slate-900 flex items-center gap-2">
                                    <i class="fa-solid fa-boxes-stacked text-amber-600"></i>
                                    <span>Quản lý Tồn Kho Hàng Hóa</span>
                                </h2>
                                <p class="text-xs text-slate-500">Kiểm soát định mức tồn, giá nhập trung bình và điều phối kho giữa các chi nhánh.</p>
                            </div>

                            <div class="flex flex-wrap items-center gap-2">
                                <div class="relative w-56">
                                    <input type="text" placeholder="Tìm theo SKU / tên SP..." class="w-full bg-slate-50 border border-slate-200 rounded-xl pl-8 pr-3 py-1.5 text-xs focus:outline-none focus:border-amber-500">
                                    <i class="fa-solid fa-magnifying-glass absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400 text-xs"></i>
                                </div>
                                <select class="bg-slate-50 border border-slate-200 rounded-xl px-2.5 py-1.5 text-xs font-semibold text-slate-700">
                                    <option value="ALL">Tất cả danh mục</option>
                                    <option value="SELL">Dùng để bán</option>
                                    <option value="FACILITY">Dùng cho cơ sở</option>
                                </select>
                                <button @click="openRestockModal()" class="px-3.5 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-bold shadow-xs transition flex items-center gap-1.5">
                                    <i class="fa-solid fa-plus text-xs"></i>
                                    <span>Nhập Thêm Kho</span>
                                </button>
                            </div>
                        </div>

                        <!-- Data Table 9 Cột Đúng Thứ Tự -->
                        <div class="bg-white rounded-2xl border border-slate-200/80 shadow-xs overflow-hidden">
                            <div class="overflow-x-auto">
                                <table class="w-full text-left text-xs">
                                    <thead class="bg-slate-50 text-slate-500 border-b border-slate-200 uppercase tracking-wider font-bold">
                                        <tr>
                                            <th class="py-3 px-3 text-center">
                                                <input type="checkbox" @change="toggleAllInventorySelection()" :checked="selectedInventorySKUs.length === inventoryItems.length && inventoryItems.length > 0" class="rounded text-sky-600 focus:ring-0">
                                            </th>
                                            <th class="py-3 px-3">SKU</th>
                                            <th class="py-3 px-3">Sản phẩm</th>
                                            <th class="py-3 px-3 text-center">Danh mục</th>
                                            <th class="py-3 px-3 text-right">Giá mua vào TB</th>
                                            <th class="py-3 px-3 text-right">Giá bán</th>
                                            <th class="py-3 px-3 text-center">Tổng tồn kho</th>
                                            <th class="py-3 px-3 text-center">Trạng thái</th>
                                            <th class="py-3 px-3 text-center">Thao tác</th>
                                        </tr>
                                    </thead>
                                    <tbody class="divide-y divide-slate-100 font-medium text-slate-700">
                                        <template x-for="item in inventoryItems" :key="item.sku">
                                            <tr class="hover:bg-slate-50 transition">
                                                <!-- Checkbox -->
                                                <td class="py-3.5 px-3 text-center">
                                                    <input type="checkbox" :checked="selectedInventorySKUs.includes(item.sku)" @change="toggleInventoryItemSelection(item.sku)" class="rounded text-sky-600 focus:ring-0">
                                                </td>

                                                <!-- SKU -->
                                                <td class="py-3.5 px-3 font-mono font-bold text-slate-800" x-text="item.sku"></td>

                                                <!-- Sản phẩm (Ảnh + Tên) -->
                                                <td class="py-3.5 px-3">
                                                    <div class="flex items-center gap-2.5">
                                                        <img :src="item.image" class="w-9 h-9 rounded-lg object-cover border border-slate-200 shrink-0">
                                                        <span class="font-bold text-slate-900" x-text="item.name"></span>
                                                    </div>
                                                </td>

                                                <!-- Danh mục -->
                                                <td class="py-3.5 px-3 text-center">
                                                    <span :class="item.category === 'Dùng để bán' ? 'bg-blue-100 text-blue-800' : 'bg-purple-100 text-purple-800'" class="px-2.5 py-0.5 rounded-full text-[10px] font-bold" x-text="item.category"></span>
                                                </td>

                                                <!-- Giá mua vào TB -->
                                                <td class="py-3.5 px-3 text-right font-medium text-slate-600" x-text="formatCurrency(item.buyPrice)"></td>

                                                <!-- Giá bán -->
                                                <td class="py-3.5 px-3 text-right font-bold text-slate-900" x-text="formatCurrency(item.sellPrice)"></td>

                                                <!-- Tổng tồn kho (Kèm logic note tự động trừ) -->
                                                <td class="py-3.5 px-3 text-center font-black text-slate-800">
                                                    <div x-text="item.stock + ' ' + item.unit"></div>
                                                    <div class="text-[9px] text-slate-400 font-normal">Tự động trừ khi bán</div>
                                                </td>

                                                <!-- Trạng thái -->
                                                <td class="py-3.5 px-3 text-center">
                                                    <span :class="item.status === 'Còn hàng' ? 'bg-emerald-100 text-emerald-800' : (item.status === 'Sắp hết' ? 'bg-amber-100 text-amber-800' : 'bg-rose-100 text-rose-800')" class="px-2.5 py-0.5 rounded-full text-[10px] font-bold" x-text="item.status"></span>
                                                </td>

                                                <!-- Thao tác -->
                                                <td class="py-3.5 px-3 text-center">
                                                    <div class="flex items-center justify-center gap-1.5">
                                                        <button @click="openRestockModal(item)" class="p-1.5 text-emerald-600 hover:bg-emerald-50 rounded-lg transition" title="Nhập kho">
                                                            <i class="fa-solid fa-truck-ramp-box text-sm"></i>
                                                        </button>
                                                        <button @click="showToast('Sửa sản phẩm: ' + item.sku)" class="p-1.5 text-sky-600 hover:bg-sky-50 rounded-lg transition" title="Sửa">
                                                            <i class="fa-solid fa-pen-to-square text-sm"></i>
                                                        </button>
                                                        <button @click="showToast('Xóa sản phẩm: ' + item.sku)" class="p-1.5 text-rose-600 hover:bg-rose-50 rounded-lg transition" title="Xóa">
                                                            <i class="fa-solid fa-trash-can text-sm"></i>
                                                        </button>
                                                    </div>
                                                </td>
                                            </tr>
                                        </template>
                                    </tbody>
                                </table>
                            </div>

                            <!-- Footer pagination -->
                            <div class="p-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
                                <span>Hiển thị 8 của 8 mặt hàng</span>
                                <span class="text-slate-400">Trang 1 / 1</span>
                            </div>
                        </div>

                    </section>

                    <!-- ======================================================== -->
                    <!-- MODULE 5: QUẢN LÝ HOTEL (HOTEL MANAGEMENT) -->
                    <!-- ======================================================== -->
                    <section x-show="activeAdminTab === 'hotel'" class="space-y-6 animate-fadeIn">
                        
                        <!-- Top Header & 2 Sub-Tabs -->
                        <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs space-y-4">
                            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                                <div>
                                    <h2 class="text-xl font-black text-slate-900 flex items-center gap-2">
                                        <i class="fa-solid fa-hotel text-indigo-600"></i>
                                        <span>Quản lý Khách sạn Thú cưng (Pet Hotel 5 Sao)</span>
                                    </h2>
                                    <p class="text-xs text-slate-500">Sơ đồ 40 phòng trực quan, đồng bộ trạng thái lưu trú và gán mã dịch vụ đã cọc.</p>
                                </div>

                                <!-- Sub-tabs: 20 Phòng Chó / 20 Phòng Mèo -->
                                <div class="inline-flex rounded-xl p-1 bg-slate-100 border border-slate-200 text-xs font-bold">
                                    <button @click="activeHotelSubTab = 'dog'" :class="activeHotelSubTab === 'dog' ? 'bg-indigo-600 text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'" class="px-4 py-2 rounded-lg transition flex items-center gap-2">
                                        <i class="fa-solid fa-dog"></i>
                                        <span>20 Phòng Hotel Chó</span>
                                    </button>
                                    <button @click="activeHotelSubTab = 'cat'" :class="activeHotelSubTab === 'cat' ? 'bg-indigo-600 text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'" class="px-4 py-2 rounded-lg transition flex items-center gap-2">
                                        <i class="fa-solid fa-cat"></i>
                                        <span>20 Phòng Hotel Mèo</span>
                                    </button>
                                </div>
                            </div>

                            <!-- Toolbar Filter nhanh trạng thái phòng -->
                            <div class="flex flex-wrap items-center justify-between gap-3 pt-2 border-t border-slate-100">
                                <div class="flex flex-wrap items-center gap-2 text-xs font-semibold">
                                    <span class="text-slate-400 mr-1">Lọc trạng thái:</span>
                                    <button @click="hotelStatusFilter = 'ALL'" :class="hotelStatusFilter === 'ALL' ? 'bg-slate-800 text-white font-bold' : 'bg-slate-100 text-slate-700'" class="px-3 py-1 rounded-lg transition">Tất cả (20)</button>
                                    <button @click="hotelStatusFilter = 'available'" :class="hotelStatusFilter === 'available' ? 'bg-emerald-600 text-white font-bold' : 'bg-emerald-50 text-emerald-800 border border-emerald-200'" class="px-3 py-1 rounded-lg transition">Phòng trống</button>
                                    <button @click="hotelStatusFilter = 'reserved'" :class="hotelStatusFilter === 'reserved' ? 'bg-amber-600 text-white font-bold' : 'bg-amber-50 text-amber-800 border border-amber-200'" class="px-3 py-1 rounded-lg transition">Đã cọc</button>
                                    <button @click="hotelStatusFilter = 'occupied'" :class="hotelStatusFilter === 'occupied' ? 'bg-sky-600 text-white font-bold' : 'bg-sky-50 text-sky-800 border border-sky-200'" class="px-3 py-1 rounded-lg transition">Đang sử dụng</button>
                                    <button @click="hotelStatusFilter = 'cleaning'" :class="hotelStatusFilter === 'cleaning' ? 'bg-purple-600 text-white font-bold' : 'bg-purple-50 text-purple-800 border border-purple-200'" class="px-3 py-1 rounded-lg transition">Đang dọn dẹp</button>
                                </div>

                                <div class="text-xs text-slate-500 font-medium">
                                    <i class="fa-solid fa-circle-info text-sky-600 mr-1"></i> Click vào phòng để đổi trạng thái hoặc gán đơn cọc.
                                </div>
                            </div>
                        </div>

                        <!-- Grid 5 cột × 4 hàng (20 Phòng) cho Sub-tab Chó -->
                        <div x-show="activeHotelSubTab === 'dog'" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
                            <template x-for="room in dogRooms" :key="room.id">
                                <div x-show="hotelStatusFilter === 'ALL' || hotelStatusFilter === room.status"
                                     @click="handleRoomClick(room)"
                                     class="p-4 rounded-2xl border-2 transition-all duration-200 cursor-pointer hover:shadow-md transform hover:-translate-y-0.5 select-none relative"
                                     :class="getRoomCardClass(room.status)">
                                    
                                    <div class="flex justify-between items-start">
                                        <div class="font-black text-lg" x-text="room.id"></div>
                                        <span class="text-[10px] font-black px-2 py-0.5 rounded-full uppercase" :class="getRoomBadgeClass(room.status)" x-text="getRoomStatusText(room.status)"></span>
                                    </div>

                                    <!-- Conditional Rendering: Mã DV nếu đang sử dụng -->
                                    <div class="mt-3">
                                        <template x-if="room.status === 'occupied'">
                                            <div class="bg-white/80 backdrop-blur rounded-xl p-2 border border-sky-200 space-y-0.5">
                                                <div class="text-[10px] text-sky-700 font-bold uppercase tracking-wider">Mã Dịch Vụ:</div>
                                                <div class="text-xs font-black text-sky-900 font-mono" x-text="room.serviceId"></div>
                                                <div class="text-[10px] text-slate-600 truncate" x-text="room.petName + ' (' + room.customerName + ')'"></div>
                                            </div>
                                        </template>

                                        <template x-if="room.status === 'reserved'">
                                            <div class="text-[11px] font-bold text-amber-800">
                                                Khách đã đặt trước
                                            </div>
                                        </template>

                                        <template x-if="room.status === 'available'">
                                            <div class="text-[11px] font-bold text-emerald-800">
                                                Sẵn sàng đón bé
                                            </div>
                                        </template>

                                        <template x-if="room.status === 'cleaning'">
                                            <div class="text-[11px] font-bold text-purple-800">
                                                Khử trùng ozone
                                            </div>
                                        </template>
                                    </div>
                                </div>
                            </template>
                        </div>

                        <!-- Grid 5 cột × 4 hàng (20 Phòng) cho Sub-tab Mèo -->
                        <div x-show="activeHotelSubTab === 'cat'" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
                            <template x-for="room in catRooms" :key="room.id">
                                <div x-show="hotelStatusFilter === 'ALL' || hotelStatusFilter === room.status"
                                     @click="handleRoomClick(room)"
                                     class="p-4 rounded-2xl border-2 transition-all duration-200 cursor-pointer hover:shadow-md transform hover:-translate-y-0.5 select-none relative"
                                     :class="getRoomCardClass(room.status)">
                                    
                                    <div class="flex justify-between items-start">
                                        <div class="font-black text-lg" x-text="room.id"></div>
                                        <span class="text-[10px] font-black px-2 py-0.5 rounded-full uppercase" :class="getRoomBadgeClass(room.status)" x-text="getRoomStatusText(room.status)"></span>
                                    </div>

                                    <!-- Conditional Rendering: Mã DV nếu đang sử dụng -->
                                    <div class="mt-3">
                                        <template x-if="room.status === 'occupied'">
                                            <div class="bg-white/80 backdrop-blur rounded-xl p-2 border border-sky-200 space-y-0.5">
                                                <div class="text-[10px] text-sky-700 font-bold uppercase tracking-wider">Mã Dịch Vụ:</div>
                                                <div class="text-xs font-black text-sky-900 font-mono" x-text="room.serviceId"></div>
                                                <div class="text-[10px] text-slate-600 truncate" x-text="room.petName + ' (' + room.customerName + ')'"></div>
                                            </div>
                                        </template>

                                        <template x-if="room.status === 'reserved'">
                                            <div class="text-[11px] font-bold text-amber-800">
                                                Khách đã đặt trước
                                            </div>
                                        </template>

                                        <template x-if="room.status === 'available'">
                                            <div class="text-[11px] font-bold text-emerald-800">
                                                Sẵn sàng đón bé
                                            </div>
                                        </template>

                                        <template x-if="room.status === 'cleaning'">
                                            <div class="text-[11px] font-bold text-purple-800">
                                                Khử trùng ozone
                                            </div>
                                        </template>
                                    </div>
                                </div>
                            </template>
                        </div>

                        <!-- Queue List: Danh sách mã dịch vụ đã cọc (Mục 4) -->
                        <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs space-y-3">
                            <div class="flex items-center justify-between">
                                <h3 class="text-sm font-bold text-slate-900 flex items-center gap-2">
                                    <i class="fa-solid fa-list-check text-amber-600"></i>
                                    <span>Những mã dịch vụ (đã cọc) đang chờ xếp phòng:</span>
                                </h3>
                                <span class="text-xs text-slate-500 font-medium">Click vào một mã dịch vụ bên dưới, sau đó click vào một "Phòng trống" ở trên để gán.</span>
                            </div>

                            <div class="flex flex-wrap gap-2.5 pt-1">
                                <template x-for="item in hotelDepositQueue" :key="item.serviceId">
                                    <button @click="selectQueueForAssignment(item)"
                                            :class="selectedQueueForAssignment && selectedQueueForAssignment.serviceId === item.serviceId ? 'bg-amber-600 text-white font-black ring-4 ring-amber-200' : 'bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-200 font-bold'"
                                            class="px-3.5 py-2 rounded-xl text-xs transition flex items-center gap-2 shadow-2xs">
                                        <i class="fa-solid fa-tag"></i>
                                        <span class="font-mono" x-text="item.serviceId"></span>
                                        <span>-</span>
                                        <span x-text="item.petName + ' (' + item.customerName + ')'"></span>
                                        <span class="text-[10px] bg-white/40 px-1.5 py-0.2 rounded" x-text="item.checkIn"></span>
                                    </button>
                                </template>

                                <div x-show="hotelDepositQueue.length === 0" class="text-xs text-slate-400 italic">
                                    Không có mã dịch vụ chờ xếp phòng.
                                </div>
                            </div>
                        </div>

                    </section>

                    <!-- ======================================================== -->
                    <!-- MODULE 6: QUẢN LÝ NHÂN SỰ (STAFF MANAGEMENT) -->
                    <!-- ======================================================== -->
                    <section x-show="activeAdminTab === 'staff'" class="space-y-4 animate-fadeIn">
                        
                        <!-- Top Actions (Mục 1) -->
                        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-white p-4 rounded-2xl border border-slate-200/80 shadow-xs">
                            <div>
                                <h2 class="text-xl font-black text-slate-900 flex items-center gap-2">
                                    <i class="fa-solid fa-id-badge text-purple-600"></i>
                                    <span>Quản lý Nhân sự</span>
                                </h2>
                                <p class="text-xs text-slate-500">Phân ca trực tuyến, toggle lịch làm tuần và quản lý bằng cấp bác sĩ.</p>
                            </div>

                            <div class="flex items-center gap-2">
                                <button @click="showToast('Thêm nhân sự mới')" class="px-3.5 py-2 bg-purple-600 hover:bg-purple-700 text-white rounded-xl text-xs font-bold shadow-xs transition flex items-center gap-1.5">
                                    <i class="fa-solid fa-user-plus text-xs"></i>
                                    <span>Thêm nhân sự</span>
                                </button>
                                <button @click="showToast('Chế độ sửa thông tin')" class="px-3 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs font-bold border border-slate-200 transition">
                                    Sửa thông tin
                                </button>
                                <button @click="showToast('Chọn nhân sự cần xóa')" class="px-3 py-2 bg-rose-50 hover:bg-rose-100 text-rose-600 rounded-xl text-xs font-bold border border-rose-300 transition">
                                    Xóa bỏ nhân sự
                                </button>
                            </div>
                        </div>

                        <!-- Bảng Dữ Liệu Nhân Sự (Inline Editable - Mục 2) -->
                        <div class="bg-white rounded-2xl border border-slate-200/80 shadow-xs overflow-hidden">
                            <div class="overflow-x-auto">
                                <table class="w-full text-left text-xs">
                                    <thead class="bg-slate-50 text-slate-500 border-b border-slate-200 uppercase tracking-wider font-bold">
                                        <tr>
                                            <th class="py-3 px-4">Mã nhân sự</th>
                                            <th class="py-3 px-4">Tên</th>
                                            <th class="py-3 px-4 text-center">Công việc</th>
                                            <th class="py-3 px-4">Ca làm (Chọn trực tiếp)</th>
                                            <th class="py-3 px-4">Lịch ca tuần (Bật/Tắt thứ)</th>
                                            <th class="py-3 px-4 text-center">Hồ sơ nhân sự</th>
                                        </tr>
                                    </thead>
                                    <tbody class="divide-y divide-slate-100 font-medium text-slate-700">
                                        <template x-for="st in staffList" :key="st.staffId">
                                            <tr class="hover:bg-slate-50 transition">
                                                <!-- Mã nhân sự -->
                                                <td class="py-4 px-4 font-mono font-bold text-slate-900" x-text="st.staffId"></td>

                                                <!-- Tên -->
                                                <td class="py-4 px-4">
                                                    <div class="font-bold text-slate-900" x-text="st.name"></div>
                                                    <div class="text-[10px] text-slate-400" x-text="st.phone"></div>
                                                </td>

                                                <!-- Công việc (Badge màu khác nhau) -->
                                                <td class="py-4 px-4 text-center">
                                                    <span :class="st.role === 'Chuyên gia chăm sóc' ? 'bg-rose-100 text-rose-800' : (st.role === 'PetShip' ? 'bg-emerald-100 text-emerald-800' : (st.role === 'Nhân viên chăm sóc' ? 'bg-teal-100 text-teal-800' : 'bg-slate-100 text-slate-700'))" class="px-2.5 py-1 rounded-full text-[11px] font-bold" x-text="st.role"></span>
                                                </td>

                                                <!-- Ca làm (Interactive Dropdown inline) -->
                                                <td class="py-4 px-4">
                                                    <select :value="st.shift" @change="updateStaffShift(st, $event.target.value)" class="bg-slate-50 border border-slate-300 rounded-xl px-2.5 py-1.5 text-xs font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-purple-200 cursor-pointer">
                                                        <option value="8h-12h">8h-12h (Sáng)</option>
                                                        <option value="12h-17h">12h-17h (Chiều)</option>
                                                        <option value="17h-21h">17h-21h (Tối)</option>
                                                        <option value="21h-8h">21h-8h (Đêm trực)</option>
                                                    </select>
                                                </td>

                                                <!-- Lịch ca tuần (Interactive Badges T2..CN click toggle) -->
                                                <td class="py-4 px-4">
                                                    <div class="flex items-center gap-1.5">
                                                        <template x-for="day in ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN']" :key="day">
                                                            <button @click="toggleStaffDay(st, day)"
                                                                    :class="isStaffWorkingDay(st, day) ? 'bg-purple-600 text-white font-black shadow-2xs' : 'bg-slate-100 text-slate-400 font-semibold hover:bg-slate-200'"
                                                                    class="w-7 h-7 rounded-lg text-[10px] flex items-center justify-center transition"
                                                                    x-text="day"></button>
                                                        </template>
                                                    </div>
                                                </td>

                                                <!-- Hồ sơ nhân sự -->
                                                <td class="py-4 px-4 text-center">
                                                    <button @click="openStaffProfile(st)" class="px-3 py-1.5 bg-sky-50 hover:bg-sky-100 text-sky-700 border border-sky-300 rounded-xl font-bold transition flex items-center gap-1 mx-auto">
                                                        <i class="fa-solid fa-address-card text-xs"></i>
                                                        <span>Hồ sơ</span>
                                                    </button>
                                                </td>
                                            </tr>
                                        </template>
                                    </tbody>
                                </table>
                            </div>
                        </div>

                    </section>

                    <!-- ======================================================== -->
                    <!-- MODULE 7: QUẢN LÝ KHÁCH HÀNG (CUSTOMER MANAGEMENT) -->
                    <!-- ======================================================== -->
                    <section x-show="activeAdminTab === 'customers'" class="space-y-4 animate-fadeIn">
                        
                        <!-- Header & Filters (Mục 1) -->
                        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-white p-4 rounded-2xl border border-slate-200/80 shadow-xs">
                            <div>
                                <h2 class="text-xl font-black text-slate-900 flex items-center gap-2">
                                    <i class="fa-solid fa-users text-sky-600"></i>
                                    <span>Quản lý Khách hàng</span>
                                </h2>
                                <p class="text-xs text-slate-500">Danh sách khách hàng, hạng thẻ thành viên, mức chi tiêu và lịch sử giao dịch.</p>
                            </div>

                            <div class="flex items-center gap-2">
                                <div class="relative w-64">
                                    <input type="text" placeholder="Tìm theo tên, SĐT..." class="w-full bg-slate-50 border border-slate-200 rounded-xl pl-8 pr-3 py-1.5 text-xs focus:outline-none focus:border-sky-500">
                                    <i class="fa-solid fa-magnifying-glass absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400 text-xs"></i>
                                </div>
                                <select class="bg-slate-50 border border-slate-200 rounded-xl px-2.5 py-1.5 text-xs font-semibold text-slate-700">
                                    <option value="ALL">Tất cả hạng</option>
                                    <option value="PLATINUM">Bạch Kim</option>
                                    <option value="GOLD">Vàng</option>
                                    <option value="SILVER">Bạc</option>
                                    <option value="BRONZE">Đồng</option>
                                </select>
                            </div>
                        </div>

                        <!-- Main Table (Mục 2) -->
                        <div class="bg-white rounded-2xl border border-slate-200/80 shadow-xs overflow-hidden">
                            <div class="overflow-x-auto">
                                <table class="w-full text-left text-xs">
                                    <thead class="bg-slate-50 text-slate-500 border-b border-slate-200 uppercase tracking-wider font-bold">
                                        <tr>
                                            <th class="py-3 px-4">Mã KH</th>
                                            <th class="py-3 px-4">Họ và tên</th>
                                            <th class="py-3 px-4">Liên hệ</th>
                                            <th class="py-3 px-4 text-center">Membership</th>
                                            <th class="py-3 px-4 text-center">Thú cưng</th>
                                            <th class="py-3 px-4 text-right">Tổng chi</th>
                                            <th class="py-3 px-4 text-center">Thao tác 1 (Lịch sử)</th>
                                            <th class="py-3 px-4 text-center">Thao tác 2 (Chat CSKH)</th>
                                        </tr>
                                    </thead>
                                    <tbody class="divide-y divide-slate-100 font-medium text-slate-700">
                                        <template x-for="cust in adminCustomersList" :key="cust.customerId">
                                            <tr class="hover:bg-slate-50 transition">
                                                <!-- Mã KH -->
                                                <td class="py-3.5 px-4">
                                                    <button @click="openCustomerHistory(cust)" class="font-mono font-bold text-sky-600 hover:underline" x-text="cust.customerId"></button>
                                                </td>

                                                <!-- Họ và tên + Avatar -->
                                                <td class="py-3.5 px-4">
                                                    <div class="flex items-center gap-2.5">
                                                        <img :src="cust.avatar" class="w-8 h-8 rounded-full object-cover border border-slate-200">
                                                        <span class="font-bold text-slate-900" x-text="cust.name"></span>
                                                    </div>
                                                </td>

                                                <!-- Liên hệ -->
                                                <td class="py-3.5 px-4 text-slate-600" x-text="cust.phone"></td>

                                                <!-- Membership (Huy hiệu phân cấp rõ ràng) -->
                                                <td class="py-3.5 px-4 text-center">
                                                    <span :class="cust.tier === 'Platinum' ? 'bg-slate-800 text-white' : (cust.tier === 'Gold' ? 'bg-amber-100 text-amber-900 border border-amber-300' : (cust.tier === 'Silver' ? 'bg-slate-200 text-slate-800' : 'bg-orange-100 text-orange-900'))" class="px-2.5 py-0.5 rounded-full text-[10px] font-black uppercase tracking-wider" x-text="cust.tier"></span>
                                                </td>

                                                <!-- Thú cưng -->
                                                <td class="py-3.5 px-4 text-center font-bold text-slate-800" x-text="cust.petsCount + ' (' + cust.petsDesc + ')'"></td>

                                                <!-- Tổng chi (In đậm) -->
                                                <td class="py-3.5 px-4 text-right font-black text-slate-900 text-sm" x-text="formatCurrency(cust.totalSpend)"></td>

                                                <!-- Thao tác 1: Lịch sử -->
                                                <td class="py-3.5 px-4 text-center">
                                                    <button @click="openCustomerHistory(cust)" class="px-3 py-1.5 bg-slate-50 hover:bg-slate-100 text-slate-700 border border-slate-300 rounded-xl font-bold transition">
                                                        Lịch sử
                                                    </button>
                                                </td>

                                                <!-- Thao tác 2: Chat CSKH -->
                                                <td class="py-3.5 px-4 text-center">
                                                    <button @click="openCustomerChat(cust)" class="w-8 h-8 rounded-xl bg-sky-50 hover:bg-sky-100 text-sky-600 border border-sky-200 flex items-center justify-center transition mx-auto" title="Nhắn tin trực tiếp">
                                                        <i class="fa-solid fa-message text-xs"></i>
                                                    </button>
                                                </td>
                                            </tr>
                                        </template>
                                    </tbody>
                                </table>
                            </div>
                        </div>

                    </section>

                    <!-- ======================================================== -->
                    <!-- MODULE 8: QUẢN LÝ HỒ SƠ THÚ CƯNG (PET PROFILES) -->
                    <!-- ======================================================== -->
                    <section x-show="activeAdminTab === 'pets'" class="space-y-4 animate-fadeIn">
                        
                        <!-- Top Actions (Mục 1) -->
                        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-white p-4 rounded-2xl border border-slate-200/80 shadow-xs">
                            <div>
                                <h2 class="text-xl font-black text-slate-900 flex items-center gap-2">
                                    <i class="fa-solid fa-paw text-rose-600"></i>
                                    <span>Hồ sơ Thú cưng</span>
                                </h2>
                                <p class="text-xs text-slate-500">Sổ theo dõi sức khỏe chuyên sâu, tiền sử tiêm chủng, dị ứng và khẩu phần ăn.</p>
                            </div>

                            <div class="flex items-center gap-2">
                                <button @click="showToast('Thêm hồ sơ thú cưng mới')" class="px-3.5 py-2 bg-rose-600 hover:bg-rose-700 text-white rounded-xl text-xs font-bold shadow-xs transition flex items-center gap-1.5">
                                    <i class="fa-solid fa-plus text-xs"></i>
                                    <span>Thêm hồ sơ</span>
                                </button>
                                <button @click="showToast('Chọn hồ sơ cần xóa')" class="px-3 py-2 bg-rose-50 hover:bg-rose-100 text-rose-600 rounded-xl text-xs font-bold border border-rose-300 transition flex items-center gap-1.5">
                                    <i class="fa-solid fa-trash-can text-xs"></i>
                                    <span>Xóa hồ sơ</span>
                                </button>
                            </div>
                        </div>

                        <!-- Main Table (Mục 2) -->
                        <div class="bg-white rounded-2xl border border-slate-200/80 shadow-xs overflow-hidden">
                            <div class="overflow-x-auto">
                                <table class="w-full text-left text-xs">
                                    <thead class="bg-slate-50 text-slate-500 border-b border-slate-200 uppercase tracking-wider font-bold">
                                        <tr>
                                            <th class="py-3 px-4">Mã Pet</th>
                                            <th class="py-3 px-4">Tên Thú Cưng</th>
                                            <th class="py-3 px-4">Loài & Giống</th>
                                            <th class="py-3 px-4">Tên Chủ</th>
                                            <th class="py-3 px-4 text-center">Cân nặng</th>
                                            <th class="py-3 px-4 text-center">Tình trạng hiện tại</th>
                                            <th class="py-3 px-4 text-center">Hành động</th>
                                        </tr>
                                    </thead>
                                    <tbody class="divide-y divide-slate-100 font-medium text-slate-700">
                                        <template x-for="pet in adminPetProfilesList" :key="pet.petId">
                                            <tr class="hover:bg-slate-50 transition">
                                                <!-- Mã Pet -->
                                                <td class="py-3.5 px-4 font-mono font-bold text-slate-900" x-text="pet.petId"></td>

                                                <!-- Tên Thú cưng -->
                                                <td class="py-3.5 px-4">
                                                    <div class="flex items-center gap-2.5">
                                                        <img :src="pet.avatar" class="w-8 h-8 rounded-full object-cover border border-slate-200">
                                                        <span class="font-black text-slate-900 text-sm" x-text="pet.name"></span>
                                                    </div>
                                                </td>

                                                <!-- Loài & Giống -->
                                                <td class="py-3.5 px-4 font-semibold text-slate-700" x-text="pet.species + ' - ' + pet.breed"></td>

                                                <!-- Tên Chủ (link click) -->
                                                <td class="py-3.5 px-4">
                                                    <button @click="showToast('Liên hệ chủ: ' + pet.ownerPhone)" class="font-bold text-sky-600 hover:underline" x-text="pet.ownerName"></button>
                                                </td>

                                                <!-- Cân nặng -->
                                                <td class="py-3.5 px-4 text-center font-black text-slate-800" x-text="pet.weight"></td>

                                                <!-- Tình trạng hiện tại -->
                                                <td class="py-3.5 px-4 text-center">
                                                    <span :class="pet.status === 'Khỏe mạnh' ? 'bg-emerald-100 text-emerald-800' : (pet.status === 'Đang ốm' ? 'bg-rose-100 text-rose-800' : 'bg-sky-100 text-sky-800')" class="px-2.5 py-0.5 rounded-full text-[10px] font-black" x-text="'[' + pet.status + ']'"></span>
                                                </td>

                                                <!-- Hành động: Sổ Sức Khỏe -->
                                                <td class="py-3.5 px-4 text-center">
                                                    <button @click="openPetHealthBook(pet)" class="px-3 py-1.5 bg-rose-50 hover:bg-rose-100 text-rose-700 border border-rose-300 rounded-xl font-bold transition flex items-center gap-1.5 mx-auto">
                                                        <i class="fa-solid fa-heart-pulse text-xs"></i>
                                                        <span>Sổ Sức Khỏe</span>
                                                    </button>
                                                </td>
                                            </tr>
                                        </template>
                                    </tbody>
                                </table>
                            </div>
                        </div>

                    </section>

                    <!-- ======================================================== -->
                    <!-- MODULE 9: FLOW PETSHIP (ĐIỀU PHỐI VẬN CHUYỂN) -->
                    <!-- ======================================================== -->
                    <section x-show="activeAdminTab === 'petship'" class="space-y-6 animate-fadeIn">
                        
                        <!-- Top Header & Sub-Tabs -->
                        <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs space-y-4">
                            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                                <div>
                                    <h2 class="text-xl font-black text-slate-900 flex items-center gap-2">
                                        <i class="fa-solid fa-truck-fast text-emerald-600"></i>
                                        <span>Điều phối Vận chuyển PetShip An Toàn</span>
                                    </h2>
                                    <p class="text-xs text-slate-500">Giám sát quy trình đưa đón thú cưng 3 Phase có OTP & ảnh POD xác thực.</p>
                                </div>

                                <!-- Sub-Tabs: Bảng 1 Đơn Hàng / Bảng 2 Đơn Dịch Vụ -->
                                <div class="inline-flex rounded-xl p-1 bg-slate-100 border border-slate-200 text-xs font-bold">
                                    <button @click="activePetShipSubTab = 'service'" :class="activePetShipSubTab === 'service' ? 'bg-emerald-600 text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'" class="px-4 py-2 rounded-lg transition flex items-center gap-2">
                                        <i class="fa-solid fa-paw"></i>
                                        <span>Bảng 2: Đơn Dịch Vụ (Đưa rước Pet)</span>
                                    </button>
                                    <button @click="activePetShipSubTab = 'physical'" :class="activePetShipSubTab === 'physical' ? 'bg-emerald-600 text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'" class="px-4 py-2 rounded-lg transition flex items-center gap-2">
                                        <i class="fa-solid fa-box"></i>
                                        <span>Bảng 1: Đơn Hàng (Sản phẩm vật lý)</span>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <!-- BẢNG 2: ĐƠN DỊCH VỤ (ĐƯA RƯỚC THÚ CƯNG) -->
                        <div x-show="activePetShipSubTab === 'service'" class="bg-white rounded-2xl border border-slate-200/80 shadow-xs overflow-hidden space-y-4">
                            <div class="p-4 border-b border-slate-100 flex items-center justify-between">
                                <h3 class="text-sm font-bold text-slate-900 flex items-center gap-2">
                                    <i class="fa-solid fa-route text-emerald-600"></i>
                                    <span>Danh Sách Đơn Đưa Rước Thú Cưng Đến Cơ Sở & Về Nhà</span>
                                </h3>
                                <span class="text-xs text-slate-400">Tự động gán OTP hai chiều</span>
                            </div>

                            <div class="overflow-x-auto">
                                <table class="w-full text-left text-xs">
                                    <thead class="bg-slate-50 text-slate-500 border-b border-slate-200 uppercase tracking-wider font-bold">
                                        <tr>
                                            <th class="py-3 px-3">Mã DV</th>
                                            <th class="py-3 px-3">Khách & Liên hệ</th>
                                            <th class="py-3 px-3">Thú cưng</th>
                                            <th class="py-3 px-3 text-center">Gói DV</th>
                                            <th class="py-3 px-3">Thời gian</th>
                                            <th class="py-3 px-3 text-right">Tổng tiền & TT</th>
                                            <th class="py-3 px-3 text-center">Trạng thái</th>
                                            <th class="py-3 px-3">PetShip (Điều phối)</th>
                                            <th class="py-3 px-3 text-center">Chi tiết</th>
                                        </tr>
                                    </thead>
                                    <tbody class="divide-y divide-slate-100 font-medium text-slate-700">
                                        <template x-for="srv in petShipServiceList" :key="srv.serviceId">
                                            <tr class="hover:bg-slate-50 transition">
                                                <!-- Mã DV -->
                                                <td class="py-3.5 px-3 font-mono font-bold text-teal-600" x-text="srv.serviceId"></td>

                                                <!-- Khách & Liên hệ -->
                                                <td class="py-3.5 px-3">
                                                    <div class="font-bold text-slate-900" x-text="srv.customerName"></div>
                                                    <div class="text-[10px] text-slate-400" x-text="srv.phone"></div>
                                                    <div class="text-[10px] text-slate-500 truncate max-w-xs" x-text="srv.address"></div>
                                                </td>

                                                <!-- Thú cưng -->
                                                <td class="py-3.5 px-3">
                                                    <div class="font-bold text-slate-800" x-text="srv.petName"></div>
                                                    <div class="text-[10px] text-slate-400" x-text="srv.petBreed"></div>
                                                </td>

                                                <!-- Gói DV -->
                                                <td class="py-3.5 px-3 text-center">
                                                    <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-pink-100 text-pink-800" x-text="srv.package"></span>
                                                </td>

                                                <!-- Thời gian -->
                                                <td class="py-3.5 px-3 font-semibold text-slate-800" x-text="srv.time"></td>

                                                <!-- Tổng tiền & TT -->
                                                <td class="py-3.5 px-3 text-right">
                                                    <div class="font-black text-slate-900" x-text="formatCurrency(srv.total)"></div>
                                                    <div class="text-[10px] text-slate-400" x-text="srv.payment"></div>
                                                </td>

                                                <!-- Trạng thái -->
                                                <td class="py-3.5 px-3 text-center">
                                                    <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-100 text-emerald-800" x-text="srv.status"></span>
                                                </td>

                                                <!-- PetShip Dropdown điều phối -->
                                                <td class="py-3.5 px-3">
                                                    <select :value="srv.shipper" @change="assignServiceShipper(srv, $event.target.value)"
                                                            :class="srv.shipper !== 'Không có' ? 'bg-emerald-50 text-emerald-800 border-emerald-300 font-bold' : 'bg-slate-50 text-slate-500 border-slate-200'"
                                                            class="border rounded-xl px-2.5 py-1.5 text-xs focus:outline-none cursor-pointer">
                                                        <template x-for="sp in availableShippers" :key="sp">
                                                            <option :value="sp" x-text="sp"></option>
                                                        </template>
                                                    </select>
                                                </td>

                                                <!-- Chi tiết: Nút Kiểm soát lộ trình -->
                                                <td class="py-3.5 px-3 text-center">
                                                    <button @click="openPetShipControl(srv)" class="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl font-bold transition flex items-center gap-1.5 shadow-2xs mx-auto">
                                                        <i class="fa-solid fa-shield-halved text-xs"></i>
                                                        <span>Kiểm soát lộ trình</span>
                                                    </button>
                                                </td>
                                            </tr>
                                        </template>
                                    </tbody>
                                </table>
                            </div>
                        </div>

                        <!-- BẢNG 1: ĐƠN HÀNG (GIAO SẢN PHẨM VẬT LÝ) -->
                        <div x-show="activePetShipSubTab === 'physical'" class="bg-white rounded-2xl border border-slate-200/80 shadow-xs overflow-hidden space-y-4">
                            <div class="p-4 border-b border-slate-100 flex items-center justify-between">
                                <h3 class="text-sm font-bold text-slate-900 flex items-center gap-2">
                                    <i class="fa-solid fa-box text-blue-600"></i>
                                    <span>Danh Sách Đơn Hàng Giao Sản Phẩm Vật Lý</span>
                                </h3>
                            </div>

                            <div class="overflow-x-auto">
                                <table class="w-full text-left text-xs">
                                    <thead class="bg-slate-50 text-slate-500 border-b border-slate-200 uppercase tracking-wider font-bold">
                                        <tr>
                                            <th class="py-3 px-3">Mã đơn hàng</th>
                                            <th class="py-3 px-3">Thông tin sản phẩm</th>
                                            <th class="py-3 px-3">Khách hàng</th>
                                            <th class="py-3 px-3">SĐT & Địa chỉ</th>
                                            <th class="py-3 px-3 text-right">Tổng tiền & TT</th>
                                            <th class="py-3 px-3">Ghi chú</th>
                                            <th class="py-3 px-3 text-center">Chi tiết</th>
                                        </tr>
                                    </thead>
                                    <tbody class="divide-y divide-slate-100 font-medium text-slate-700">
                                        <template x-for="ord in petShipPhysicalList" :key="ord.orderId">
                                            <tr class="hover:bg-slate-50 transition">
                                                <td class="py-3.5 px-3 font-mono font-bold text-sky-700" x-text="ord.orderId"></td>
                                                <td class="py-3.5 px-3 font-semibold text-slate-800" x-text="ord.products"></td>
                                                <td class="py-3.5 px-3 font-bold text-slate-900" x-text="ord.customerName"></td>
                                                <td class="py-3.5 px-3">
                                                    <div class="text-slate-800 font-semibold" x-text="ord.phone"></div>
                                                    <div class="text-[10px] text-slate-500 truncate max-w-xs" x-text="ord.address"></div>
                                                </td>
                                                <td class="py-3.5 px-3 text-right">
                                                    <div class="font-black text-slate-900" x-text="formatCurrency(ord.total)"></div>
                                                    <div class="text-[10px] text-slate-400" x-text="ord.payment"></div>
                                                </td>
                                                <td class="py-3.5 px-3 text-slate-500 max-w-xs truncate" x-text="ord.notes"></td>
                                                <td class="py-3.5 px-3 text-center">
                                                    <button @click="openAdminOrderDetail({ orderId: ord.orderId, customerName: ord.customerName, customerPhone: ord.phone, total: ord.total, paymentMethod: 'cod', notes: ord.notes, status: 'PROCESSING', address: ord.address })" class="px-3 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl font-bold transition">
                                                        Xem đơn
                                                    </button>
                                                </td>
                                            </tr>
                                        </template>
                                    </tbody>
                                </table>
                            </div>
                        </div>

                    </section>

                </div>
            </main>

        </div>

    </div>
"""
