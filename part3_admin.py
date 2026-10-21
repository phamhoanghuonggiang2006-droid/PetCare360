# -*- coding: utf-8 -*-
ADMIN_HTML = """
    <!-- ======================================================== -->
    <!-- VIEW 2: GIAO DIỆN QUẢN TRỊ VIÊN (ADMIN VIEW) -->
    <!-- ======================================================== -->
    <div x-show="currentRole === 'admin'" class="min-h-screen flex flex-col dark:bg-slate-900 dark:text-slate-100" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 scale-98" x-transition:enter-end="opacity-100 scale-100">
        
        <!-- TOP BAR ADMIN -->
        <header class="sticky top-0 z-30 bg-white dark:bg-slate-800 border-b border-slate-200 dark:border-slate-700 h-16 flex items-center justify-between px-4 lg:px-6 shadow-sm">
            <div class="flex items-center gap-3 md:gap-5">
                <button @click="sidebarOpen = !sidebarOpen" class="p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 focus:outline-none">
                    <i data-lucide="menu" class="w-5 h-5"></i>
                </button>
                <div class="flex items-center gap-2">
                    <div class="w-8 h-8 rounded-lg bg-teal-600 flex items-center justify-center text-white font-bold text-lg shadow-sm">
                        <i data-lucide="paw-print" class="w-5 h-5"></i>
                    </div>
                    <span class="font-bold text-slate-900 dark:text-white hidden sm:inline text-lg tracking-tight">PetCare<span class="text-teal-600 dark:text-teal-400">360</span> <span class="text-xs bg-teal-100 dark:bg-teal-950 text-teal-800 dark:text-teal-300 font-bold px-2 py-0.5 rounded-full ml-1">Admin</span></span>
                </div>

                <!-- Global Branch Select -->
                <div class="relative hidden sm:block">
                    <div class="flex items-center bg-slate-100 dark:bg-slate-700/70 border border-slate-200 dark:border-slate-600 rounded-lg p-1">
                        <i data-lucide="map-pin" class="w-4 h-4 text-teal-600 dark:text-teal-400 ml-2"></i>
                        <select x-model="globalBranch" @change="showToast('Đã lọc cơ sở: ' + globalBranch)" class="bg-transparent text-xs sm:text-sm font-medium text-slate-800 dark:text-slate-100 focus:outline-none px-2 py-1 pr-6 cursor-pointer">
                            <option value="ALL" class="dark:bg-slate-800">Tất cả cơ sở (3)</option>
                            <option value="Q1" class="dark:bg-slate-800">Chi nhánh Quận 1</option>
                            <option value="BT" class="dark:bg-slate-800">Chi nhánh Bình Thạnh</option>
                            <option value="Q7" class="dark:bg-slate-800">Chi nhánh Quận 7</option>
                        </select>
                    </div>
                </div>

                <!-- Time Filter Bar in Header -->
                <div class="relative hidden lg:flex items-center bg-slate-100 dark:bg-slate-700/70 border border-slate-200 dark:border-slate-600 rounded-lg p-1 text-xs">
                    <i data-lucide="calendar-range" class="w-4 h-4 text-amber-500 ml-2"></i>
                    <select x-model="adminTimeFilter" @change="applyTimeFilter()" class="bg-transparent text-xs font-semibold text-slate-800 dark:text-slate-100 focus:outline-none px-2 py-1 cursor-pointer">
                        <option value="ALL" class="dark:bg-slate-800">Toàn bộ thời gian</option>
                        <option value="TODAY" class="dark:bg-slate-800">Hôm nay</option>
                        <option value="7DAYS" class="dark:bg-slate-800">7 ngày gần nhất</option>
                        <option value="THIS_MONTH" class="dark:bg-slate-800">Tháng này</option>
                        <option value="THIS_QUARTER" class="dark:bg-slate-800">Quý này</option>
                    </select>
                </div>
            </div>

            <div class="flex items-center gap-2.5 sm:gap-3">
                <button @click="switchAdminTab('dashboard'); scrollToUrgentTasks()" class="relative p-2 rounded-lg bg-amber-50 dark:bg-amber-950/40 text-amber-700 dark:text-amber-400 border border-amber-200 dark:border-amber-800 text-xs font-semibold flex items-center gap-1.5 hover:bg-amber-100 transition-colors">
                    <i data-lucide="bell" class="w-4 h-4 text-amber-600 dark:text-amber-400"></i>
                    <span class="hidden md:inline">Việc cần xử lý</span>
                    <span class="bg-red-500 text-white text-[10px] px-1.5 py-0.5 rounded-full font-bold" x-text="urgentTasksCount"></span>
                </button>

                <!-- NÚT THÔNG BÁO CẬP NHẬT HỆ THỐNG MỚI NHẤT (THAY NÚT MẶT TRỜI - YÊU CẦU MỤC 6 & 7) -->
                <div class="relative">
                    <button @click="toggleAdminNotifications()" class="relative p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 transition" title="Thông báo cập nhật mới nhất">
                        <i class="fa-solid fa-bell text-lg"></i>
                        <span x-show="unreadNotificationsCount > 0" class="absolute top-1 right-1 w-4 h-4 bg-rose-500 text-white text-[9px] font-bold rounded-full flex items-center justify-center animate-pulse" x-text="unreadNotificationsCount"></span>
                    </button>

                    <!-- Dropdown danh sách những cập nhật mới nhất -->
                    <div x-show="showAdminNotifications" @click.away="showAdminNotifications = false" x-cloak class="absolute right-0 mt-2 w-80 sm:w-96 bg-white dark:bg-slate-800 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-700 z-50 overflow-hidden animate-fadeIn">
                        <div class="p-3.5 bg-gradient-to-r from-teal-600 to-teal-700 text-white flex items-center justify-between">
                            <div class="flex items-center gap-2">
                                <i class="fa-solid fa-bell"></i>
                                <span class="font-bold text-sm">Cập nhật hệ thống mới nhất</span>
                            </div>
                            <button @click="markAllNotificationsRead()" class="text-[11px] underline text-teal-100 hover:text-white font-medium">
                                Đã đọc tất cả
                            </button>
                        </div>
                        <div class="max-h-80 overflow-y-auto divide-y divide-slate-100 dark:divide-slate-700">
                            <template x-for="item in adminNotifications" :key="item.id">
                                <div @click="markNotificationRead(item.id)" class="p-3 hover:bg-slate-50 dark:hover:bg-slate-700/50 transition cursor-pointer flex gap-3 items-start" :class="item.read ? 'opacity-70' : 'bg-teal-50/40 dark:bg-teal-950/20'">
                                    <div class="w-8 h-8 rounded-xl flex items-center justify-center shrink-0 mt-0.5" :class="item.read ? 'bg-slate-100 dark:bg-slate-700 text-slate-500' : 'bg-teal-100 dark:bg-teal-900 text-teal-700 dark:text-teal-300'">
                                        <i :class="item.icon || 'fa-solid fa-bell'"></i>
                                    </div>
                                    <div class="flex-1">
                                        <div class="flex items-center justify-between">
                                            <h5 class="text-xs font-bold text-slate-800 dark:text-slate-100" x-text="item.title"></h5>
                                            <span class="text-[10px] text-slate-400" x-text="item.time"></span>
                                        </div>
                                        <p class="text-[11px] text-slate-600 dark:text-slate-300 mt-0.5 leading-snug" x-text="item.desc"></p>
                                    </div>
                                    <span x-show="!item.read" class="w-2 h-2 rounded-full bg-teal-500 shrink-0 mt-1.5"></span>
                                </div>
                            </template>
                        </div>
                        <div class="p-2.5 bg-slate-50 dark:bg-slate-700/50 text-center border-t border-slate-100 dark:border-slate-700">
                            <span class="text-[11px] text-slate-500 dark:text-slate-400 font-semibold">Tự động đồng bộ thời gian thực 24/7</span>
                        </div>
                    </div>
                </div>

                <div class="h-6 w-px bg-slate-200 dark:bg-slate-700 mx-1"></div>

                <!-- Admin Profile Card & Logout button -->
                <div class="flex items-center gap-2.5">
                    <div class="w-9 h-9 rounded-full bg-teal-700 text-white flex items-center justify-center font-bold text-sm shadow">
                        HL
                    </div>
                    <div class="hidden xl:block text-left">
                        <div class="text-sm font-bold text-slate-800 dark:text-slate-100 leading-tight">Hoàng Long</div>
                        <div class="text-xs text-teal-600 dark:text-teal-400 font-medium">Chủ doanh nghiệp</div>
                    </div>
                    <button @click="logout()" class="text-xs bg-rose-50 dark:bg-rose-950/40 text-rose-600 dark:text-rose-400 border border-rose-200 dark:border-rose-800 px-3 py-1.5 rounded-xl font-bold hover:bg-rose-100 dark:hover:bg-rose-900/60 transition flex items-center gap-1.5 shadow-xs" title="Đăng xuất khỏi hệ thống">
                        <i class="fa-solid fa-arrow-right-from-bracket text-xs"></i>
                        <span class="hidden sm:inline">Đăng xuất</span>
                    </button>
                </div>
            </div>
        </header>

        <div class="flex-1 flex overflow-hidden">
            <!-- SIDEBAR ADMIN -->
            <aside x-show="sidebarOpen" class="w-64 bg-white dark:bg-slate-800 border-r border-slate-200 dark:border-slate-700 flex flex-col transition-all duration-200 shrink-0">
                <div class="p-4 space-y-1 overflow-y-auto flex-1">
                    <div class="px-3 py-2 text-[11px] font-bold text-slate-400 uppercase tracking-wider">Tổng quan</div>
                    <button @click="switchAdminTab('dashboard')" :class="activeAdminTab === 'dashboard' ? 'text-teal-700 bg-teal-50 dark:bg-teal-950/50 dark:text-teal-300 font-bold' : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition">
                        <i data-lucide="layout-dashboard" class="w-4 h-4"></i> Dashboard Báo cáo
                    </button>
                    
                    <div class="px-3 py-2 text-[11px] font-bold text-slate-400 uppercase tracking-wider mt-4">Kinh doanh & Vận hành</div>
                    <button @click="switchAdminTab('orders')" :class="activeAdminTab === 'orders' ? 'text-teal-700 bg-teal-50 dark:bg-teal-950/50 dark:text-teal-300 font-bold' : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'" class="w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-sm font-medium transition">
                        <div class="flex items-center gap-3">
                            <i data-lucide="shopping-bag" class="w-4 h-4"></i> Quản lý Đơn hàng
                        </div>
                        <span x-show="pendingOrdersCount > 0" class="bg-amber-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full" x-text="pendingOrdersCount"></span>
                    </button>

                    <!-- LỊCH HẸN (ĐÃ ĐỔI TÊN THEO YÊU CẦU MỤC 1) -->
                    <button @click="switchAdminTab('appointments')" :class="activeAdminTab === 'appointments' ? 'text-teal-700 bg-teal-50 dark:bg-teal-950/50 dark:text-teal-300 font-bold' : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'" class="w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-sm font-medium transition">
                        <div class="flex items-center gap-3">
                            <i data-lucide="calendar" class="w-4 h-4"></i> Lịch hẹn
                        </div>
                        <span class="bg-teal-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full" x-text="appointments.length"></span>
                    </button>

                    <button @click="switchAdminTab('products')" :class="activeAdminTab === 'products' ? 'text-teal-700 bg-teal-50 dark:bg-teal-950/50 dark:text-teal-300 font-bold' : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition">
                        <i data-lucide="package" class="w-4 h-4"></i> Sản phẩm & Tồn kho
                    </button>
                    <button @click="switchAdminTab('customers')" :class="activeAdminTab === 'customers' ? 'text-teal-700 bg-teal-50 dark:bg-teal-950/50 dark:text-teal-300 font-bold' : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'" class="w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-sm font-medium transition">
                        <div class="flex items-center gap-3">
                            <i data-lucide="users" class="w-4 h-4"></i> Quản lý Khách hàng
                        </div>
                        <span class="text-[10px] text-teal-600 dark:text-teal-400 font-bold" x-text="customers.length"></span>
                    </button>
                    <button @click="switchAdminTab('pets')" :class="activeAdminTab === 'pets' ? 'text-teal-700 bg-teal-50 dark:bg-teal-950/50 dark:text-teal-300 font-bold' : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'" class="w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-sm font-medium transition">
                        <div class="flex items-center gap-3">
                            <i data-lucide="dog" class="w-4 h-4"></i> Hồ sơ Thú cưng
                        </div>
                        <span class="text-[10px] text-teal-600 dark:text-teal-400 font-bold" x-text="allPets.length"></span>
                    </button>

                    <div class="px-3 py-2 text-[11px] font-bold text-slate-400 uppercase tracking-wider mt-4">Hệ thống & Phân tích</div>
                    <button @click="switchAdminTab('analytics')" :class="activeAdminTab === 'analytics' ? 'text-teal-700 bg-teal-50 dark:bg-teal-950/50 dark:text-teal-300 font-bold' : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition">
                        <i data-lucide="bar-chart-3" class="w-4 h-4"></i> Phân tích Doanh thu & Web
                    </button>
                    <button @click="switchAdminTab('branches')" :class="activeAdminTab === 'branches' ? 'text-teal-700 bg-teal-50 dark:bg-teal-950/50 dark:text-teal-300 font-bold' : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition">
                        <i data-lucide="settings" class="w-4 h-4"></i> Cấu hình Chi nhánh
                    </button>

                    <div class="pt-4 mt-4 border-t border-slate-200 dark:border-slate-700">
                        <button @click="logout()" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-semibold text-rose-600 dark:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/40 transition">
                            <i data-lucide="log-out" class="w-4 h-4 text-rose-500"></i> Đăng xuất
                        </button>
                    </div>
                </div>
            </aside>

            <!-- MAIN CONTENT PANELS ADMIN -->
            <main class="flex-1 overflow-y-auto p-4 lg:p-6 space-y-6">

                <!-- MODULE 1: DASHBOARD -->
                <section x-show="activeAdminTab === 'dashboard'" class="space-y-6">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                        <div>
                            <h1 class="text-2xl font-bold text-slate-900 dark:text-white">Tổng quan Vận hành & Doanh thu</h1>
                            <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">
                                Đang xem: <strong class="text-teal-600 dark:text-teal-400" x-text="getBranchLabel()"></strong>
                                <span class="mx-2">•</span>
                                Thời gian: <span class="font-bold text-amber-600" x-text="getTimeFilterLabel()"></span>
                            </p>
                        </div>
                        <div class="flex items-center gap-2">
                            <!-- Bộ lọc thời gian nhanh -->
                            <div class="flex items-center bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl px-3 py-1.5 shadow-xs text-xs">
                                <span class="text-slate-400 mr-2"><i class="fa-solid fa-clock"></i> Thời gian:</span>
                                <select x-model="adminTimeFilter" @change="applyTimeFilter()" class="bg-transparent font-bold text-slate-800 dark:text-slate-200 focus:outline-none cursor-pointer">
                                    <option value="ALL">Toàn bộ</option>
                                    <option value="TODAY">Hôm nay</option>
                                    <option value="7DAYS">7 ngày qua</option>
                                    <option value="THIS_MONTH">Tháng này</option>
                                    <option value="THIS_QUARTER">Quý này</option>
                                </select>
                            </div>

                            <span class="text-xs bg-emerald-100 dark:bg-emerald-950/50 text-emerald-800 dark:text-emerald-300 font-semibold px-3 py-1.5 rounded-xl border border-emerald-300 flex items-center gap-1.5">
                                <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                                Real-time Sync
                            </span>
                        </div>
                    </div>

                    <!-- Metrics Grid -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                        <div class="bg-white dark:bg-slate-800 p-4 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm">
                            <div class="flex items-center justify-between text-xs text-slate-500">
                                <span>Doanh thu kỳ này</span>
                                <i data-lucide="dollar-sign" class="w-4 h-4 text-emerald-500"></i>
                            </div>
                            <div class="text-xl font-bold text-slate-900 dark:text-white mt-2" x-text="formatCurrency(totalRevenueFiltered)"></div>
                            <span class="text-[11px] text-emerald-600 font-medium">↑ +18.4% so với kỳ trước</span>
                        </div>
                        <div class="bg-white dark:bg-slate-800 p-4 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm">
                            <div class="flex items-center justify-between text-xs text-slate-500">
                                <span>Đơn hàng E-Commerce</span>
                                <i data-lucide="shopping-cart" class="w-4 h-4 text-teal-500"></i>
                            </div>
                            <div class="text-xl font-bold text-slate-900 dark:text-white mt-2" x-text="filteredOrdersByBranch.length + ' đơn'"></div>
                            <span class="text-[11px] text-amber-600 font-medium" x-text="pendingProductOrdersCount + ' đơn chờ xác nhận'"></span>
                        </div>
                        <div class="bg-white dark:bg-slate-800 p-4 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm">
                            <div class="flex items-center justify-between text-xs text-slate-500">
                                <span>Lịch hẹn Phòng khám & Spa</span>
                                <i data-lucide="calendar" class="w-4 h-4 text-indigo-500"></i>
                            </div>
                            <div class="text-xl font-bold text-slate-900 dark:text-white mt-2" x-text="filteredAppointmentsByBranch.length + ' ca'"></div>
                            <span class="text-[11px] text-teal-600 font-medium" x-text="inProgressAppointmentsCount + ' ca đang tiếp khách'"></span>
                        </div>
                        <div class="bg-white dark:bg-slate-800 p-4 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm">
                            <div class="flex items-center justify-between text-xs text-slate-500">
                                <span>Cảnh báo Tồn kho</span>
                                <i data-lucide="alert-triangle" class="w-4 h-4 text-red-500"></i>
                            </div>
                            <div class="text-xl font-bold text-slate-900 dark:text-white mt-2" x-text="lowStockCount + ' sản phẩm'"></div>
                            <span class="text-[11px] text-red-500 font-medium">Dưới ngưỡng an toàn</span>
                        </div>
                    </div>

                    <!-- Revenue Chart Section -->
                    <div class="bg-white dark:bg-slate-800 p-4 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm">
                        <div class="flex items-center justify-between mb-4">
                            <div>
                                <h3 class="text-base font-bold text-slate-900 dark:text-white">Biểu đồ Doanh thu (Triệu VNĐ)</h3>
                                <p class="text-xs text-slate-500">So sánh doanh thu Sản phẩm E-Commerce & Dịch vụ Y tế - Spa 6 tháng gần nhất</p>
                            </div>
                            <button @click="refreshChart()" class="text-xs text-teal-600 hover:underline flex items-center gap-1 font-semibold">
                                <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i> Cập nhật biểu đồ
                            </button>
                        </div>
                        <!-- FALLBACK UI VÀ CANVAS CHART (YÊU CẦU MỤC 1) -->
                        <div class="h-64 relative">
                            <canvas id="revenueChart" x-show="revenueMonthlyMock && revenueMonthlyMock.length > 0"></canvas>
                            <div x-show="!revenueMonthlyMock || revenueMonthlyMock.length === 0" class="absolute inset-0 flex flex-col items-center justify-center text-slate-400 bg-slate-50/50 dark:bg-slate-800 rounded-xl">
                                <i class="fa-solid fa-chart-column text-4xl mb-2 text-slate-300"></i>
                                <p class="text-xs font-semibold">Chưa có dữ liệu thống kê doanh thu</p>
                            </div>
                        </div>
                    </div>

                    <!-- Urgent Tasks Section -->
                    <div id="urgent-tasks-section" class="bg-white dark:bg-slate-800 p-4 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm space-y-3">
                        <h3 class="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
                            <i data-lucide="alert-circle" class="w-5 h-5 text-amber-500"></i> Việc cần xử lý ngay
                        </h3>
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                            <div class="p-3 bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/50 rounded-lg flex justify-between items-center">
                                <div>
                                    <div class="font-bold text-amber-900 dark:text-amber-300">Đơn hàng mới chờ duyệt</div>
                                    <div class="text-amber-700 dark:text-amber-400"><span x-text="pendingProductOrdersCount"></span> đơn hàng E-Commerce</div>
                                </div>
                                <button @click="switchAdminTab('orders'); setOrderTypeFilter('PRODUCT')" class="px-2.5 py-1 bg-amber-600 text-white font-bold rounded">Xem</button>
                            </div>
                            <div class="p-3 bg-teal-50 dark:bg-teal-950/30 border border-teal-200 dark:border-teal-800/50 rounded-lg flex justify-between items-center">
                                <div>
                                    <div class="font-bold text-teal-900 dark:text-teal-300">Lịch hẹn chờ tiếp đón</div>
                                    <div class="text-teal-700 dark:text-teal-400"><span x-text="pendingServiceAppointmentsCount"></span> ca hẹn phòng khám</div>
                                </div>
                                <button @click="switchAdminTab('appointments')" class="px-2.5 py-1 bg-teal-600 text-white font-bold rounded">Xem</button>
                            </div>
                            <div class="p-3 bg-red-50 dark:bg-red-950/30 border border-red-200 dark:border-red-800/50 rounded-lg flex justify-between items-center">
                                <div>
                                    <div class="font-bold text-red-900 dark:text-red-300">Thuốc/Vật tư sắp hết</div>
                                    <div class="text-red-700 dark:text-red-400"><span x-text="lowStockCount"></span> mặt hàng cần nhập</div>
                                </div>
                                <button @click="switchAdminTab('products'); showLowStockOnly = true" class="px-2.5 py-1 bg-red-600 text-white font-bold rounded">Kho</button>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- MODULE 2: QUẢN LÝ ĐƠN HÀNG -->
                <section x-show="activeAdminTab === 'orders'" class="space-y-4">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                        <div>
                            <h2 class="text-xl font-bold text-slate-900 dark:text-white">Quản lý Đơn hàng & Dịch vụ</h2>
                            <p class="text-xs text-slate-500 dark:text-slate-400">Đơn hàng khách đặt từ webapp được đồng bộ tức thì vào bảng điều khiển này</p>
                        </div>
                        <div class="flex gap-2">
                            <button @click="showToast('Đã xuất file Excel dữ liệu thành công!')" class="px-3 py-2 border border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 rounded-lg text-xs font-semibold hover:bg-slate-50 flex items-center gap-1">
                                <i data-lucide="download" class="w-4 h-4"></i> Xuất Excel
                            </button>
                        </div>
                    </div>

                    <!-- Type Filter Tabs -->
                    <div class="flex border-b border-slate-200 dark:border-slate-700 space-x-2">
                        <button @click="setOrderTypeFilter('PRODUCT')" :class="currentOrderTypeTab === 'PRODUCT' ? 'border-teal-600 text-teal-600 dark:text-teal-400 font-bold' : 'border-transparent text-slate-500 hover:text-slate-700'" class="pb-3 px-4 text-sm border-b-2 flex items-center gap-2 transition">
                            <i data-lucide="package" class="w-4 h-4"></i> Đơn hàng Sản phẩm E-Commerce (<span x-text="productOrdersCount"></span>)
                        </button>
                        <button @click="setOrderTypeFilter('SERVICE')" :class="currentOrderTypeTab === 'SERVICE' ? 'border-teal-600 text-teal-600 dark:text-teal-400 font-bold' : 'border-transparent text-slate-500 hover:text-slate-700'" class="pb-3 px-4 text-sm border-b-2 flex items-center gap-2 transition">
                            <i data-lucide="scissors" class="w-4 h-4"></i> Dịch vụ Spa & Phòng khám (<span x-text="serviceOrdersCount"></span>)
                        </button>
                    </div>

                    <div class="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 p-4 shadow-sm space-y-4">
                        <div class="flex flex-wrap items-center justify-between gap-3">
                            <div class="flex flex-wrap items-center gap-2 flex-1 min-w-[280px]">
                                <div class="relative flex-1 min-w-[200px]">
                                    <i data-lucide="search" class="w-4 h-4 absolute left-3 top-2.5 text-slate-400"></i>
                                    <input type="text" x-model="orderSearchQuery" placeholder="Tìm mã đơn, tên khách, SĐT..." class="w-full pl-9 pr-3 py-1.5 text-xs sm:text-sm bg-slate-50 dark:bg-slate-700/50 border border-slate-300 dark:border-slate-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500">
                                </div>
                                <select x-model="orderStatusFilter" class="bg-slate-50 dark:bg-slate-700/50 border border-slate-300 dark:border-slate-600 text-xs sm:text-sm rounded-lg px-3 py-1.5 text-slate-700 dark:text-slate-200">
                                    <option value="ALL">Tất cả trạng thái</option>
                                    <option value="PENDING">Chờ xác nhận</option>
                                    <option value="PREPARING">Đang chuẩn bị / Đã đặt</option>
                                    <option value="DELIVERING">Đang giao / Đang thực hiện</option>
                                    <option value="COMPLETED">Hoàn tất</option>
                                    <option value="CANCELLED">Đã hủy</option>
                                </select>
                            </div>
                            <div class="text-xs text-slate-500">
                                Hiển thị <span class="font-bold text-slate-800 dark:text-slate-200" x-text="filteredAdminOrders.length"></span> đơn
                            </div>
                        </div>

                        <!-- Orders Data Table -->
                        <div class="overflow-x-auto rounded-lg border border-slate-200 dark:border-slate-700">
                            <table class="w-full text-left border-collapse text-xs sm:text-sm">
                                <thead>
                                    <tr class="bg-slate-100 dark:bg-slate-700/50 text-slate-600 dark:text-slate-300 font-semibold border-b border-slate-200 dark:border-slate-700">
                                        <th class="p-3">Mã đơn</th>
                                        <th class="p-3">Khách hàng</th>
                                        <th class="p-3">Nội dung tóm tắt</th>
                                        <th class="p-3">Tổng tiền</th>
                                        <th class="p-3">Thanh toán</th>
                                        <th class="p-3">Chi nhánh</th>
                                        <th class="p-3">Trạng thái</th>
                                        <th class="p-3 text-right">Thao tác</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-200 dark:divide-slate-700">
                                    <template x-for="ord in filteredAdminOrders" :key="ord.id">
                                        <tr class="hover:bg-slate-50 dark:hover:bg-slate-700/30 transition-colors">
                                            <td class="p-3">
                                                <button @click="openOrderDetail(ord)" class="font-bold text-teal-600 dark:text-teal-400 hover:underline" x-text="'#' + ord.id"></button>
                                            </td>
                                            <td class="p-3">
                                                <div class="font-medium text-slate-800 dark:text-slate-200 flex items-center gap-1.5">
                                                    <span x-text="ord.customer"></span>
                                                    <span x-show="ord.customer === customerProfile.name" class="bg-teal-100 dark:bg-teal-900 text-teal-800 dark:text-teal-200 text-[9px] font-bold px-1.5 py-0.2 rounded">Tài khoản hiện tại</span>
                                                </div>
                                                <div class="text-[11px] text-slate-400" x-text="ord.phone"></div>
                                            </td>
                                            <td class="p-3 max-w-[220px] truncate text-xs" :title="ord.summary" x-text="ord.summary || getOrderSummary(ord)"></td>
                                            <td class="p-3 font-bold text-slate-900 dark:text-slate-100" x-text="formatCurrency(ord.total || ord.totalAmount)"></td>
                                            <td class="p-3 text-xs" x-text="ord.paymentMethodLabel || ord.payment"></td>
                                            <td class="p-3"><span class="px-2 py-0.5 rounded text-[10px] font-bold bg-teal-100 text-teal-800" x-text="ord.branch || 'Q1'"></span></td>
                                            <td class="p-3">
                                                <span class="px-2 py-0.5 rounded text-[10px] font-bold" 
                                                      :class="{
                                                          'bg-amber-100 text-amber-800': ord.status === 'PENDING' || ord.status === 'Chờ xác nhận',
                                                          'bg-emerald-100 text-emerald-800': ord.status === 'COMPLETED' || ord.status === 'Đã hoàn thành',
                                                          'bg-red-100 text-red-800': ord.status === 'CANCELLED' || ord.status === 'Đã hủy',
                                                          'bg-blue-100 text-blue-800': ord.status === 'PREPARING' || ord.status === 'DELIVERING' || ord.status === 'Đang xử lý'
                                                      }" 
                                                      x-text="formatOrderStatusLabel(ord.status)"></span>
                                            </td>
                                            <td class="p-3 text-right">
                                                <button @click="openOrderDetail(ord)" class="px-2 py-1 bg-teal-600 text-white text-xs rounded font-semibold hover:bg-teal-700">Chi tiết</button>
                                            </td>
                                        </tr>
                                    </template>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>

                <!-- MODULE 3: LỊCH HẸN (ĐÃ ĐỔI TÊN & THÊM CỘT GHI CHÚ, DROPDOWN THAO TÁC - YÊU CẦU MỤC 1, 2) -->
                <section x-show="activeAdminTab === 'appointments'" class="space-y-4">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                        <div>
                            <h2 class="text-xl font-bold text-slate-900 dark:text-white">Lịch hẹn Phòng khám & Spa</h2>
                            <p class="text-xs text-slate-500 dark:text-slate-400">Điều phối ca hẹn, xem ghi chú của khách và chọn trực tiếp trạng thái tiếp nhận</p>
                        </div>
                        <div class="flex gap-2">
                            <button @click="openNewAppointmentModal()" class="px-3 py-2 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold flex items-center gap-1.5 shadow-sm">
                                <i data-lucide="plus" class="w-4 h-4"></i> Tạo lịch hẹn mới
                            </button>
                        </div>
                    </div>

                    <div class="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 p-4 shadow-sm space-y-4">
                        <div class="flex flex-wrap items-center justify-between gap-3">
                            <div class="flex flex-wrap items-center gap-2 flex-1 min-w-[280px]">
                                <div class="relative flex-1 min-w-[200px]">
                                    <i data-lucide="search" class="w-4 h-4 absolute left-3 top-2.5 text-slate-400"></i>
                                    <input type="text" x-model="appointmentSearchQuery" placeholder="Tìm tên chủ, thú cưng, dịch vụ..." class="w-full pl-9 pr-3 py-1.5 text-xs sm:text-sm bg-slate-50 dark:bg-slate-700/50 border border-slate-300 dark:border-slate-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500">
                                </div>
                                <select x-model="appointmentServiceFilter" class="bg-slate-50 dark:bg-slate-700/50 border border-slate-300 dark:border-slate-600 text-xs sm:text-sm rounded-lg px-3 py-1.5 text-slate-700 dark:text-slate-200">
                                    <option value="ALL">Tất cả dịch vụ</option>
                                    <option value="Khám bệnh">Khám bệnh & Cấp cứu</option>
                                    <option value="Tiêm">Tiêm vắc xin</option>
                                    <option value="Spa">Spa & Cắt tỉa</option>
                                    <option value="Phẫu thuật">Phẫu thuật / Triệt sản</option>
                                    <option value="Răng">Lấy cao răng siêu âm</option>
                                </select>
                            </div>
                            <div class="text-xs text-slate-500">
                                Hiển thị <span class="font-bold text-slate-800 dark:text-slate-200" x-text="filteredAppointments.length"></span> ca hẹn
                            </div>
                        </div>

                        <!-- Appointments Table with Note Column & Selectable Status Action -->
                        <div class="overflow-x-auto rounded-lg border border-slate-200 dark:border-slate-700">
                            <table class="w-full text-left border-collapse text-xs sm:text-sm">
                                <thead>
                                    <tr class="bg-slate-100 dark:bg-slate-700/50 text-slate-600 dark:text-slate-300 font-semibold border-b border-slate-200 dark:border-slate-700">
                                        <th class="p-3">Mã hẹn</th>
                                        <th class="p-3">Khách hàng & Thú cưng</th>
                                        <th class="p-3">Dịch vụ & Bác sĩ</th>
                                        <th class="p-3">Thời gian</th>
                                        <th class="p-3">Chi nhánh</th>
                                        <!-- CỘT GHI CHÚ MỚI (YÊU CẦU MỤC 2) -->
                                        <th class="p-3 min-w-[150px]">Ghi chú khách hàng</th>
                                        <th class="p-3">Trạng thái</th>
                                        <!-- CỘT THAO TÁC CÓ THỂ LỰA CHỌN TRẠNG THÁI (YÊU CẦU MỤC 2) -->
                                        <th class="p-3 text-right min-w-[160px]">Thao tác (Đổi trạng thái)</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-200 dark:divide-slate-700">
                                    <template x-for="a in filteredAppointments" :key="a.id">
                                        <tr class="hover:bg-slate-50 dark:hover:bg-slate-700/30">
                                            <td class="p-3 font-bold text-teal-600" x-text="a.id"></td>
                                            <td class="p-3">
                                                <div class="font-bold text-slate-800 dark:text-slate-200" x-text="a.customer"></div>
                                                <div class="text-xs text-teal-600 font-medium" x-text="'Pet: ' + a.pet"></div>
                                            </td>
                                            <td class="p-3">
                                                <span class="font-semibold text-slate-700 dark:text-slate-200" x-text="a.service"></span>
                                                <div class="text-[11px] text-slate-400" x-text="a.doc"></div>
                                            </td>
                                            <td class="p-3 text-xs font-medium" x-text="a.time"></td>
                                            <td class="p-3"><span class="px-2 py-0.5 rounded text-[10px] font-bold bg-teal-100 text-teal-800" x-text="a.branch"></span></td>
                                            
                                            <!-- Hiển thị Ghi chú khách để lại (Yêu cầu mục 2) -->
                                            <td class="p-3">
                                                <span class="text-xs italic text-slate-600 dark:text-slate-300 bg-amber-50 dark:bg-amber-950/30 px-2 py-1 rounded-md border border-amber-200/50 block" 
                                                      x-text="a.note || 'Không có ghi chú thêm'"></span>
                                            </td>

                                            <td class="p-3">
                                                <span class="px-2.5 py-1 rounded-full text-[10px] font-bold"
                                                      :class="{
                                                          'bg-emerald-100 text-emerald-800': a.status === 'COMPLETED' || a.status === 'Hoàn thành',
                                                          'bg-blue-100 text-blue-800': a.status === 'IN_PROGRESS' || a.status === 'Đang tiếp khách',
                                                          'bg-amber-100 text-amber-800': a.status === 'CONFIRMED' || a.status === 'Đã đặt hẹn',
                                                          'bg-rose-100 text-rose-800': a.status === 'CANCELLED' || a.status === 'Hủy hẹn'
                                                      }"
                                                      x-text="formatAppointmentStatus(a.status)"></span>
                                            </td>

                                            <!-- Dropdown Thao tác có thể chọn trạng thái (Yêu cầu mục 2) -->
                                            <td class="p-3 text-right">
                                                <select :value="a.status" 
                                                        @change="updateAppointmentStatusDirect(a, $event.target.value)" 
                                                        class="bg-white dark:bg-slate-700 border border-slate-300 dark:border-slate-600 text-xs font-bold rounded-lg px-2.5 py-1.5 text-slate-800 dark:text-slate-100 focus:ring-2 focus:ring-teal-500 cursor-pointer shadow-xs">
                                                    <option value="CONFIRMED">Đã đặt hẹn</option>
                                                    <option value="IN_PROGRESS">Đang tiếp khách</option>
                                                    <option value="COMPLETED">Hoàn thành</option>
                                                    <option value="CANCELLED">Hủy hẹn</option>
                                                </select>
                                            </td>
                                        </tr>
                                    </template>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>

                <!-- MODULE 4: SẢN PHẨM & TỒN KHO (CÓ NÚT THÊM SẢN PHẨM & NHẬP THÊM - YÊU CẦU MỤC 4) -->
                <section x-show="activeAdminTab === 'products'" class="space-y-4">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                        <div>
                            <h2 class="text-xl font-bold text-slate-900 dark:text-white">Sản phẩm & Quản lý Tồn kho</h2>
                            <p class="text-xs text-slate-500 dark:text-slate-400">Quản lý danh mục sản phẩm, thêm mặt hàng mới và lập phiếu nhập kho đa cơ sở</p>
                        </div>
                        <div class="flex gap-2">
                            <!-- Nút Thêm sản phẩm mới mở Modal (Yêu cầu mục 4) -->
                            <button @click="openAddProductModal()" class="px-3.5 py-2 bg-teal-600 hover:bg-teal-700 text-white rounded-xl text-xs font-bold flex items-center gap-1.5 shadow-sm transition">
                                <i data-lucide="plus-circle" class="w-4 h-4"></i> Thêm sản phẩm mới
                            </button>
                        </div>
                    </div>

                    <div class="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 p-4 shadow-sm space-y-4">
                        <div class="flex flex-wrap items-center justify-between gap-3">
                            <div class="flex flex-wrap items-center gap-2 flex-1 min-w-[280px]">
                                <div class="relative flex-1 min-w-[200px]">
                                    <i data-lucide="search" class="w-4 h-4 absolute left-3 top-2.5 text-slate-400"></i>
                                    <input type="text" x-model="productSearchQuery" placeholder="Tìm tên sản phẩm, mã SKU, danh mục..." class="w-full pl-9 pr-3 py-1.5 text-xs sm:text-sm bg-slate-50 dark:bg-slate-700/50 border border-slate-300 dark:border-slate-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500">
                                </div>
                                <select x-model="productCategoryFilter" class="bg-slate-50 dark:bg-slate-700/50 border border-slate-300 dark:border-slate-600 text-xs sm:text-sm rounded-lg px-3 py-1.5 text-slate-700 dark:text-slate-200">
                                    <option value="ALL">Tất cả danh mục</option>
                                    <option value="Thức ăn">Thức ăn & Dinh dưỡng</option>
                                    <option value="Thuốc & Vaccine">Thuốc & Vaccine</option>
                                    <option value="Phụ kiện">Phụ kiện & Đồ chơi</option>
                                    <option value="Vệ sinh">Vệ sinh & Sữa tắm</option>
                                </select>
                                <button @click="showLowStockOnly = !showLowStockOnly" 
                                        :class="showLowStockOnly ? 'bg-red-600 text-white' : 'bg-red-50 dark:bg-red-950/40 border border-red-200 dark:border-red-800 text-red-700 dark:text-red-300'"
                                        class="px-3 py-1.5 rounded-lg text-xs font-bold flex items-center gap-1 transition">
                                    <i data-lucide="alert-circle" class="w-3.5 h-3.5"></i> Chỉ xem sắp hết hàng
                                </button>
                            </div>
                        </div>

                        <div class="overflow-x-auto rounded-lg border border-slate-200 dark:border-slate-700">
                            <table class="w-full text-left border-collapse text-xs sm:text-sm">
                                <thead>
                                    <tr class="bg-slate-100 dark:bg-slate-700/50 text-slate-600 dark:text-slate-300 font-semibold border-b border-slate-200 dark:border-slate-700">
                                        <th class="p-3">SKU / Sản phẩm</th>
                                        <th class="p-3">Danh mục</th>
                                        <th class="p-3 text-right">Giá bán</th>
                                        <th class="p-3 text-center">Tồn CN Q1</th>
                                        <th class="p-3 text-center">Tồn CN BT</th>
                                        <th class="p-3 text-center">Tồn CN Q7</th>
                                        <th class="p-3 text-center">Tổng tồn kho</th>
                                        <th class="p-3 text-right">Thao tác</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-200 dark:divide-slate-700">
                                    <template x-for="p in filteredProductsInventory" :key="p.sku">
                                        <tr class="hover:bg-slate-50 dark:hover:bg-slate-700/30">
                                            <td class="p-3">
                                                <div class="font-bold text-slate-800 dark:text-slate-200" x-text="p.name"></div>
                                                <span class="text-[10px] text-slate-400 font-mono" x-text="p.sku"></span>
                                            </td>
                                            <td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-700 text-xs" x-text="p.categoryAdmin || p.category"></span></td>
                                            <td class="p-3 text-right font-bold text-slate-900 dark:text-slate-100" x-text="formatCurrency(p.price)"></td>
                                            <td class="p-3 text-center font-semibold text-slate-700 dark:text-slate-300" x-text="(p.stockQ1 ?? p.q1 ?? 0)"></td>
                                            <td class="p-3 text-center font-semibold text-slate-700 dark:text-slate-300" x-text="(p.stockBT ?? p.bt ?? 0)"></td>
                                            <td class="p-3 text-center font-semibold text-slate-700 dark:text-slate-300" x-text="(p.stockQ7 ?? p.q7 ?? 0)"></td>
                                            <td class="p-3 text-center">
                                                <div class="flex items-center justify-center gap-1.5">
                                                    <span :class="getSafeTotalStock(p) === 0 ? 'text-red-600 font-extrabold' : (getSafeTotalStock(p) < 10 ? 'text-amber-600 font-bold' : 'text-teal-600 font-bold')" 
                                                          x-text="getSafeTotalStock(p)"></span>
                                                    <template x-if="getSafeTotalStock(p) === 0">
                                                        <span class="text-[10px] bg-red-100 text-red-700 px-1.5 py-0.5 rounded font-bold">Hết hàng</span>
                                                    </template>
                                                    <template x-if="getSafeTotalStock(p) > 0 && getSafeTotalStock(p) < 10">
                                                        <span class="text-[10px] bg-amber-100 text-amber-700 px-1.5 py-0.5 rounded font-bold">Sắp hết</span>
                                                    </template>
                                                </div>
                                            </td>
                                            
                                            <!-- Nút Nhập thêm mở Modal Phiếu Nhập Hàng (Yêu cầu mục 4) -->
                                            <td class="p-3 text-right">
                                                <button @click="openRestockModal(p)" class="px-2.5 py-1 bg-teal-50 hover:bg-teal-100 text-teal-800 border border-teal-200 dark:bg-slate-700 rounded-lg text-xs font-bold transition flex items-center gap-1 ml-auto shadow-xs">
                                                    <i class="fa-solid fa-plus-circle text-teal-600"></i> Nhập thêm
                                                </button>
                                            </td>
                                        </tr>
                                    </template>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>

                <!-- MODULE 5: QUẢN LÝ KHÁCH HÀNG -->
                <section x-show="activeAdminTab === 'customers'" class="space-y-4">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                        <div>
                            <h2 class="text-xl font-bold text-slate-900 dark:text-white">Quản lý Khách hàng B2C</h2>
                            <p class="text-xs text-slate-500 dark:text-slate-400">Danh sách chủ nuôi, điểm thưởng Loyalty và liên hệ CSKH trực tiếp</p>
                        </div>
                    </div>

                    <div class="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 p-4 shadow-sm space-y-4">
                        <div class="flex items-center gap-2 max-w-md">
                            <div class="relative flex-1">
                                <i data-lucide="search" class="w-4 h-4 absolute left-3 top-2.5 text-slate-400"></i>
                                <input type="text" x-model="customerSearchQuery" placeholder="Tìm tên khách hàng, SĐT, Email..." class="w-full pl-9 pr-3 py-1.5 text-xs sm:text-sm bg-slate-50 dark:bg-slate-700/50 border border-slate-300 dark:border-slate-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500">
                            </div>
                        </div>

                        <div class="overflow-x-auto rounded-lg border border-slate-200 dark:border-slate-700">
                            <table class="w-full text-left border-collapse text-xs sm:text-sm">
                                <thead>
                                    <tr class="bg-slate-100 dark:bg-slate-700/50 text-slate-600 dark:text-slate-300 font-semibold border-b border-slate-200 dark:border-slate-700">
                                        <th class="p-3">Mã KH</th>
                                        <th class="p-3">Họ và tên</th>
                                        <th class="p-3">Liên hệ</th>
                                        <th class="p-3">Hạng thẻ & Điểm</th>
                                        <th class="p-3">Thú cưng đang nuôi</th>
                                        <th class="p-3 font-semibold text-right">Tổng chi tiêu</th>
                                        <th class="p-3 text-right">Thao tác</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-200 dark:divide-slate-700">
                                    <template x-for="c in filteredAdminCustomers" :key="c.id">
                                        <tr class="hover:bg-slate-50 dark:hover:bg-slate-700/30">
                                            <td class="p-3 font-bold text-slate-500" x-text="c.id"></td>
                                            <td class="p-3">
                                                <div class="flex items-center gap-2">
                                                    <img :src="c.avatar" class="w-7 h-7 rounded-full object-cover">
                                                    <div class="font-bold text-slate-800 dark:text-slate-200" x-text="c.name"></div>
                                                </div>
                                            </td>
                                            <td class="p-3 text-xs">
                                                <div x-text="c.phone"></div>
                                                <div class="text-[11px] text-slate-400" x-text="c.email"></div>
                                            </td>
                                            <td class="p-3">
                                                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-100 text-amber-800" x-text="c.tier"></span>
                                                <div class="text-[10px] text-slate-400 mt-0.5" x-text="c.points + ' điểm'"></div>
                                            </td>
                                            <td class="p-3 text-xs">
                                                <div class="flex flex-wrap gap-1.5 items-center">
                                                    <template x-for="p in (c.petsList || [])" :key="p.name">
                                                        <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[11px] font-semibold bg-teal-50 dark:bg-slate-700 text-teal-800 dark:text-teal-300 border border-teal-200 dark:border-teal-800">
                                                            <i :class="p.type === 'Mèo' ? 'fa-solid fa-cat text-amber-500' : 'fa-solid fa-dog text-teal-600'"></i>
                                                            <span class="font-bold" x-text="p.name"></span>
                                                            <span class="text-[9px] text-slate-500 dark:text-slate-400" x-text="'(' + p.breed + ')'"></span>
                                                        </span>
                                                    </template>
                                                    <span x-show="!c.petsList || c.petsList.length === 0" class="text-slate-400 italic text-[11px]" x-text="c.pets || 'Chưa cập nhật'"></span>
                                                </div>
                                            </td>
                                            <td class="p-3 text-right font-bold text-teal-600" x-text="formatCurrency(c.spent)"></td>
                                            <td class="p-3 text-right">
                                                <button @click="openChatWithCustomer(c.name)" class="px-2.5 py-1 bg-slate-100 dark:bg-slate-700 hover:bg-slate-200 rounded text-xs font-semibold mr-1">
                                                    <i class="fa-solid fa-message mr-1 text-teal-600"></i>Chat
                                                </button>
                                            </td>
                                        </tr>
                                    </template>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>

                <!-- MODULE 6: HỒ SƠ THÚ CƯNG (CÓ NÚT SỔ SỨC KHỎE CHI TIẾT KÈM ẢNH - YÊU CẦU MỤC 3) -->
                <section x-show="activeAdminTab === 'pets'" class="space-y-4">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                        <div>
                            <h2 class="text-xl font-bold text-slate-900 dark:text-white">Hồ sơ Thú cưng Toàn Hệ Thống (Pets)</h2>
                            <p class="text-xs text-slate-500 dark:text-slate-400">Quản lý mã Microchip, giống loài, nhấn "Sổ sức khỏe" để xem chi tiết bệnh án và tiêm chủng</p>
                        </div>
                    </div>

                    <div class="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 p-4 shadow-sm space-y-4">
                        <div class="flex items-center gap-2 max-w-md">
                            <div class="relative flex-1">
                                <i data-lucide="search" class="w-4 h-4 absolute left-3 top-2.5 text-slate-400"></i>
                                <input type="text" x-model="petSearchQuery" placeholder="Tìm tên thú cưng, giống, mã Microchip, tên chủ..." class="w-full pl-9 pr-3 py-1.5 text-xs sm:text-sm bg-slate-50 dark:bg-slate-700/50 border border-slate-300 dark:border-slate-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500">
                            </div>
                        </div>

                        <div class="overflow-x-auto rounded-lg border border-slate-200 dark:border-slate-700">
                            <table class="w-full text-left border-collapse text-xs sm:text-sm">
                                <thead>
                                    <tr class="bg-slate-100 dark:bg-slate-700/50 text-slate-600 dark:text-slate-300 font-semibold border-b border-slate-200 dark:border-slate-700">
                                        <th class="p-3">Mã Pet / Microchip</th>
                                        <th class="p-3">Tên Thú cưng</th>
                                        <th class="p-3">Loài & Giống</th>
                                        <th class="p-3">Chủ sở hữu</th>
                                        <th class="p-3">Tuổi & Cân nặng</th>
                                        <th class="p-3">Tình trạng hiện tại</th>
                                        <th class="p-3 text-right">Thao tác</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-200 dark:divide-slate-700">
                                    <template x-for="p in filteredAdminPets" :key="p.id || p.chip">
                                        <tr class="hover:bg-slate-50 dark:hover:bg-slate-700/30">
                                            <td class="p-3 font-mono text-xs font-bold text-teal-600" x-text="p.chip"></td>
                                            <td class="p-3">
                                                <div class="flex items-center gap-2">
                                                    <img :src="p.image" class="w-8 h-8 rounded-lg object-cover bg-slate-100">
                                                    <div class="font-bold text-slate-800 dark:text-slate-200" x-text="p.name"></div>
                                                </div>
                                            </td>
                                            <td class="p-3 text-xs" x-text="p.species + ' - ' + p.breed"></td>
                                            <td class="p-3 text-xs">
                                                <span class="font-semibold text-slate-800 dark:text-slate-200" x-text="p.owner"></span>
                                            </td>
                                            <td class="p-3 text-xs" x-text="p.age + ' • ' + p.weight + ' kg'"></td>
                                            <td class="p-3 text-xs text-slate-500" x-text="p.health"></td>
                                            <!-- Nút Sổ sức khỏe mở Modal chi tiết (Yêu cầu mục 3) -->
                                            <td class="p-3 text-right">
                                                <button @click="openPetHealthModal(p)" class="px-2.5 py-1.5 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition flex items-center gap-1 ml-auto shadow-xs">
                                                    <i class="fa-solid fa-notes-medical text-xs"></i> Sổ sức khỏe
                                                </button>
                                            </td>
                                        </tr>
                                    </template>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>

                <!-- MODULE 7: PHÂN TÍCH DOANH THU & CHỈ SỐ WEBSITE (YÊU CẦU MỤC 6 & 7) -->
                <section x-show="activeAdminTab === 'analytics'" class="space-y-6">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                        <div>
                            <h2 class="text-xl font-bold text-slate-900 dark:text-white">Phân tích Doanh thu & Chỉ số Vận hành Website</h2>
                            <p class="text-xs text-slate-500 dark:text-slate-400">Báo cáo tài chính chi tiết kết hợp số liệu tương tác, chuyển đổi của Website</p>
                        </div>
                        <div class="flex items-center gap-2">
                            <!-- Bộ lọc thời gian phân tích -->
                            <div class="flex items-center bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl px-3 py-1.5 shadow-xs text-xs">
                                <span class="text-slate-400 mr-2"><i class="fa-solid fa-calendar-days"></i> Kỳ:</span>
                                <select x-model="adminTimeFilter" @change="applyTimeFilter()" class="bg-transparent font-bold text-slate-800 dark:text-slate-200 focus:outline-none cursor-pointer">
                                    <option value="ALL">Toàn bộ thời gian</option>
                                    <option value="TODAY">Hôm nay</option>
                                    <option value="7DAYS">7 ngày qua</option>
                                    <option value="THIS_MONTH">Tháng này</option>
                                    <option value="THIS_QUARTER">Quý này</option>
                                </select>
                            </div>
                            <button @click="showToast('Đang tạo báo cáo tổng hợp PDF chuyên sâu...')" class="px-3 py-2 border border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 rounded-lg text-xs font-semibold flex items-center gap-1.5">
                                <i data-lucide="download" class="w-4 h-4"></i> Xuất PDF
                            </button>
                        </div>
                    </div>

                    <!-- Financial KPI Summary Cards -->
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div class="bg-white dark:bg-slate-800 p-5 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm">
                            <span class="text-xs text-slate-500">Doanh thu E-Commerce Sản phẩm</span>
                            <div class="text-2xl font-bold text-teal-600 dark:text-teal-400 mt-1" x-text="formatCurrency(totalEcommerceRevenue)"></div>
                            <span class="text-xs text-emerald-600 font-semibold">↑ +21.5% so với cùng kỳ</span>
                        </div>
                        <div class="bg-white dark:bg-slate-800 p-5 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm">
                            <span class="text-xs text-slate-500">Doanh thu Dịch vụ Phòng khám & Spa</span>
                            <div class="text-2xl font-bold text-indigo-600 dark:text-indigo-400 mt-1" x-text="formatCurrency(totalServiceRevenue)"></div>
                            <span class="text-xs text-emerald-600 font-semibold">↑ +15.8% so với cùng kỳ</span>
                        </div>
                        <div class="bg-white dark:bg-slate-800 p-5 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm">
                            <span class="text-xs text-slate-500">Giá trị trung bình / Đơn hàng (AOV)</span>
                            <div class="text-2xl font-bold text-amber-600 dark:text-amber-400 mt-1">890.000 ₫</div>
                            <span class="text-xs text-slate-500">Mục tiêu: 850.000 ₫ (Đạt 104.7%)</span>
                        </div>
                    </div>

                    <!-- Category & Branch Breakdown -->
                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                        <div class="bg-white dark:bg-slate-800 p-5 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm">
                            <h3 class="font-bold text-slate-900 dark:text-white mb-3">Cơ cấu Doanh thu theo Danh mục</h3>
                            <div class="space-y-3">
                                <div>
                                    <div class="flex justify-between text-xs font-semibold mb-1">
                                        <span>Thức ăn & Dinh dưỡng</span>
                                        <span class="text-teal-600">44% (1.910 tr ₫)</span>
                                    </div>
                                    <div class="w-full bg-slate-100 dark:bg-slate-700 h-2 rounded-full overflow-hidden">
                                        <div class="bg-teal-500 h-full" style="width: 44%"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-xs font-semibold mb-1">
                                        <span>Khám bệnh & Phẫu thuật</span>
                                        <span class="text-indigo-600">26% (1.128 tr ₫)</span>
                                    </div>
                                    <div class="w-full bg-slate-100 dark:bg-slate-700 h-2 rounded-full overflow-hidden">
                                        <div class="bg-indigo-500 h-full" style="width: 26%"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-xs font-semibold mb-1">
                                        <span>Spa Grooming & Cắt tỉa</span>
                                        <span class="text-purple-600">17% (738 tr ₫)</span>
                                    </div>
                                    <div class="w-full bg-slate-100 dark:bg-slate-700 h-2 rounded-full overflow-hidden">
                                        <div class="bg-purple-500 h-full" style="width: 17%"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-xs font-semibold mb-1">
                                        <span>Thuốc & Phụ kiện</span>
                                        <span class="text-amber-600">13% (564 tr ₫)</span>
                                    </div>
                                    <div class="w-full bg-slate-100 dark:bg-slate-700 h-2 rounded-full overflow-hidden">
                                        <div class="bg-amber-500 h-full" style="width: 13%"></div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="bg-white dark:bg-slate-800 p-5 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm">
                            <h3 class="font-bold text-slate-900 dark:text-white mb-3">Tỷ trọng Đóng góp Doanh thu 3 Chi nhánh</h3>
                            <div class="space-y-4">
                                <div class="p-3 bg-slate-50 dark:bg-slate-700/40 rounded-lg flex items-center justify-between">
                                    <div>
                                        <div class="font-bold text-sm">Chi nhánh 1 - Quận 1</div>
                                        <div class="text-xs text-slate-500">1.909.600.000 ₫ (44%)</div>
                                    </div>
                                    <span class="px-2.5 py-1 bg-emerald-100 text-emerald-800 text-xs font-bold rounded-full">Dẫn đầu</span>
                                </div>
                                <div class="p-3 bg-slate-50 dark:bg-slate-700/40 rounded-lg flex items-center justify-between">
                                    <div>
                                        <div class="font-bold text-sm">Chi nhánh 2 - Bình Thạnh</div>
                                        <div class="text-xs text-slate-500">1.475.600.000 ₫ (34%)</div>
                                    </div>
                                    <span class="px-2.5 py-1 bg-blue-100 text-blue-800 text-xs font-bold rounded-full">Tăng trưởng nhanh</span>
                                </div>
                                <div class="p-3 bg-slate-50 dark:bg-slate-700/40 rounded-lg flex items-center justify-between">
                                    <div>
                                        <div class="font-bold text-sm">Chi nhánh 3 - Quận 7</div>
                                        <div class="text-xs text-slate-500">954.800.000 ₫ (22%)</div>
                                    </div>
                                    <span class="px-2.5 py-1 bg-slate-200 text-slate-700 text-xs font-bold rounded-full">Ổn định</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- MỤC PHÂN TÍCH CHI TIẾT ĐẦY ĐỦ CÁC CHỈ SỐ CỦA WEBSITE (YÊU CẦU MỤC 6 & 7) -->
                    <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-teal-200 dark:border-teal-900 shadow-sm space-y-6">
                        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 border-b border-slate-100 dark:border-slate-700 pb-4">
                            <div>
                                <span class="bg-teal-100 dark:bg-teal-900/60 text-teal-800 dark:text-teal-300 text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider inline-flex items-center gap-1.5">
                                    <i class="fa-solid fa-chart-line text-teal-600"></i> Báo cáo chuyên sâu
                                </span>
                                <h3 class="text-xl font-black text-slate-900 dark:text-white mt-2">Chỉ Số Vận Hành & Tương Tác Website (Web Analytics)</h3>
                                <p class="text-xs text-slate-500 dark:text-slate-400">Đo lường lưu lượng truy cập, tỷ lệ chuyển đổi đơn hàng và hành vi người dùng trên WebApp.</p>
                            </div>
                            <span class="text-xs font-mono bg-slate-100 dark:bg-slate-700 px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300">Google Analytics 4 • Connected</span>
                        </div>

                        <!-- 4 Web KPI Cards -->
                        <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
                            <div class="p-4 rounded-xl bg-slate-50 dark:bg-slate-700/30 border border-slate-100 dark:border-slate-700">
                                <span class="text-xs text-slate-500 block">Lượt truy cập (Sessions)</span>
                                <div class="text-xl font-black text-slate-900 dark:text-white mt-1">128.450</div>
                                <span class="text-[11px] text-emerald-600 font-bold">↑ +24.8% so với kỳ trước</span>
                            </div>
                            <div class="p-4 rounded-xl bg-slate-50 dark:bg-slate-700/30 border border-slate-100 dark:border-slate-700">
                                <span class="text-xs text-slate-500 block">Khách truy cập (Unique Users)</span>
                                <div class="text-xl font-black text-slate-900 dark:text-white mt-1">45.200</div>
                                <span class="text-[11px] text-emerald-600 font-bold">↑ +18.2% người dùng mới</span>
                            </div>
                            <div class="p-4 rounded-xl bg-slate-50 dark:bg-slate-700/30 border border-slate-100 dark:border-slate-700">
                                <span class="text-xs text-slate-500 block">Tỷ lệ chuyển đổi mua hàng</span>
                                <div class="text-xl font-black text-teal-600 dark:text-teal-400 mt-1">4.85%</div>
                                <span class="text-[11px] text-teal-700 dark:text-teal-300 font-medium">Mục tiêu: 4.50% (Vượt 7.8%)</span>
                            </div>
                            <div class="p-4 rounded-xl bg-slate-50 dark:bg-slate-700/30 border border-slate-100 dark:border-slate-700">
                                <span class="text-xs text-slate-500 block">Thời gian xem trang trung bình</span>
                                <div class="text-xl font-black text-amber-600 dark:text-amber-400 mt-1">4m 35s</div>
                                <span class="text-[11px] text-slate-400">Tỷ lệ thoát (Bounce): 28.5%</span>
                            </div>
                        </div>

                        <!-- Funnel and Traffic Sources Breakdown -->
                        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                            <!-- E-Commerce Funnel -->
                            <div class="lg:col-span-2 p-5 rounded-xl border border-slate-100 dark:border-slate-700 bg-slate-50/50 dark:bg-slate-800/50 space-y-3">
                                <h4 class="font-bold text-sm text-slate-800 dark:text-slate-200 flex items-center justify-between">
                                    <span>Phễu Hành Vi Khách Hàng (Conversion Funnel)</span>
                                    <span class="text-xs text-teal-600 font-semibold">Tỷ lệ hoàn tất đơn: 4.85%</span>
                                </h4>
                                <div class="space-y-3 text-xs pt-1">
                                    <div>
                                        <div class="flex justify-between mb-1 font-medium">
                                            <span>1. Truy cập xem Sản phẩm / Dịch vụ</span>
                                            <span class="font-bold">85.200 lượt (100%)</span>
                                        </div>
                                        <div class="w-full bg-slate-200 dark:bg-slate-700 h-2.5 rounded-full overflow-hidden">
                                            <div class="bg-teal-500 h-full rounded-full" style="width: 100%"></div>
                                        </div>
                                    </div>
                                    <div>
                                        <div class="flex justify-between mb-1 font-medium">
                                            <span>2. Thêm vào Giỏ hàng (Add to Cart)</span>
                                            <span class="font-bold">24.200 lượt (28.4%)</span>
                                        </div>
                                        <div class="w-full bg-slate-200 dark:bg-slate-700 h-2.5 rounded-full overflow-hidden">
                                            <div class="bg-indigo-500 h-full rounded-full" style="width: 28.4%"></div>
                                        </div>
                                    </div>
                                    <div>
                                        <div class="flex justify-between mb-1 font-medium">
                                            <span>3. Mở khung Thanh toán & Đặt lịch</span>
                                            <span class="font-bold">12.010 lượt (14.1%)</span>
                                        </div>
                                        <div class="w-full bg-slate-200 dark:bg-slate-700 h-2.5 rounded-full overflow-hidden">
                                            <div class="bg-amber-500 h-full rounded-full" style="width: 14.1%"></div>
                                        </div>
                                    </div>
                                    <div>
                                        <div class="flex justify-between mb-1 font-medium">
                                            <span>4. Hoàn tất đặt hàng thành công (Purchased)</span>
                                            <span class="font-bold text-emerald-600">4.132 đơn (4.85%)</span>
                                        </div>
                                        <div class="w-full bg-slate-200 dark:bg-slate-700 h-2.5 rounded-full overflow-hidden">
                                            <div class="bg-emerald-500 h-full rounded-full" style="width: 4.85%"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Device & Traffic Distribution -->
                            <div class="p-5 rounded-xl border border-slate-100 dark:border-slate-700 bg-slate-50/50 dark:bg-slate-800/50 space-y-4">
                                <h4 class="font-bold text-sm text-slate-800 dark:text-slate-200">Kênh Nguồn & Thiết Bị</h4>
                                <div class="space-y-3 text-xs">
                                    <div class="border-b border-slate-200 dark:border-slate-700 pb-2.5">
                                        <span class="text-slate-400 block mb-1">Nguồn truy cập chính:</span>
                                        <div class="flex justify-between py-0.5"><span>Tìm kiếm Google (Organic)</span><strong class="text-teal-600">42%</strong></div>
                                        <div class="flex justify-between py-0.5"><span>Cộng đồng PetShare360 & MXH</span><strong class="text-indigo-600">28%</strong></div>
                                        <div class="flex justify-between py-0.5"><span>Truy cập trực tiếp (Direct)</span><strong>18%</strong></div>
                                        <div class="flex justify-between py-0.5"><span>Quảng cáo & Đối tác</span><strong>12%</strong></div>
                                    </div>
                                    <div>
                                        <span class="text-slate-400 block mb-1">Thiết bị người dùng:</span>
                                        <div class="flex justify-between py-0.5"><span>📱 Smartphone Mobile</span><strong class="text-teal-600">68%</strong></div>
                                        <div class="flex justify-between py-0.5"><span>💻 Máy tính Desktop/Laptop</span><strong>26%</strong></div>
                                        <div class="flex justify-between py-0.5"><span>📟 Máy tính bảng Tablet</span><strong>6%</strong></div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Retention & CSAT metrics -->
                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-2 text-xs">
                            <div class="p-3.5 bg-emerald-50 dark:bg-emerald-950/20 border border-emerald-200 dark:border-emerald-800/50 rounded-xl">
                                <span class="text-emerald-700 dark:text-emerald-400 block font-medium">Tỷ lệ giữ chân khách hàng (Retention)</span>
                                <div class="text-xl font-bold text-emerald-900 dark:text-emerald-200 mt-0.5">72.4%</div>
                                <span class="text-[10px] text-emerald-600">Khách hàng đặt lại trên 2 lần/quý</span>
                            </div>
                            <div class="p-3.5 bg-blue-50 dark:bg-blue-950/20 border border-blue-200 dark:border-blue-800/50 rounded-xl">
                                <span class="text-blue-700 dark:text-blue-400 block font-medium">Chỉ số hài lòng dịch vụ (CSAT)</span>
                                <div class="text-xl font-bold text-blue-900 dark:text-blue-200 mt-0.5">4.92 / 5.0 ⭐</div>
                                <span class="text-[10px] text-blue-600">Dựa trên 2.450 lượt đánh giá 5 sao</span>
                            </div>
                            <div class="p-3.5 bg-purple-50 dark:bg-purple-950/20 border border-purple-200 dark:border-purple-800/50 rounded-xl">
                                <span class="text-purple-700 dark:text-purple-400 block font-medium">Thời gian phản hồi Chat CSKH</span>
                                <div class="text-xl font-bold text-purple-900 dark:text-purple-200 mt-0.5">&lt; 45 giây</div>
                                <span class="text-[10px] text-purple-600">Đội ngũ trực 24/7 giải quyết 99.2%</span>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- MODULE 8: CẤU HÌNH CHI NHÁNH -->
                <section x-show="activeAdminTab === 'branches'" class="space-y-6">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                        <div>
                            <h2 class="text-xl font-bold text-slate-900 dark:text-white">Cấu hình & Quản lý 3 Cơ sở Chi nhánh</h2>
                            <p class="text-xs text-slate-500 dark:text-slate-400">Cấu hình nhân sự, địa chỉ, hotline và giờ hoạt động từng cơ sở PetCare360</p>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                        <div class="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm overflow-hidden">
                            <div class="p-4 bg-teal-700 text-white flex justify-between items-center">
                                <div>
                                    <h3 class="font-bold text-base">PetCare360 - Quận 1</h3>
                                    <p class="text-xs text-teal-100">Mã: CN-Q1 | Trưởng CN: BS. Phạm Đức</p>
                                </div>
                                <span class="bg-teal-500 text-white text-[10px] font-bold px-2 py-0.5 rounded">Đang mở cửa</span>
                            </div>
                            <div class="p-4 space-y-3 text-xs">
                                <div><span class="text-slate-400">Địa chỉ:</span> <strong class="block text-slate-800 dark:text-slate-200">123 Nguyễn Thị Minh Khai, P.6, Quận 3, TP.HCM</strong></div>
                                <div><span class="text-slate-400">Hotline cấp cứu:</span> <strong class="block text-slate-800 dark:text-slate-200">028 3911 2233</strong></div>
                                <div><span class="text-slate-400">Nhân sự:</span> <span class="font-semibold text-slate-700 dark:text-slate-300">5 Bác sĩ, 8 Y tá, 4 KTV Spa</span></div>
                            </div>
                        </div>

                        <div class="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm overflow-hidden">
                            <div class="p-4 bg-slate-800 dark:bg-slate-700 text-white flex justify-between items-center">
                                <div>
                                    <h3 class="font-bold text-base">PetCare360 - Bình Thạnh</h3>
                                    <p class="text-xs text-slate-300">Mã: CN-BT | Trưởng CN: BS. Lê Thanh</p>
                                </div>
                                <span class="bg-teal-500 text-white text-[10px] font-bold px-2 py-0.5 rounded">Đang mở cửa</span>
                            </div>
                            <div class="p-4 space-y-3 text-xs">
                                <div><span class="text-slate-400">Địa chỉ:</span> <strong class="block text-slate-800 dark:text-slate-200">45/2 Bùi Đình Túy, Phường 24, Bình Thạnh, TP.HCM</strong></div>
                                <div><span class="text-slate-400">Hotline cấp cứu:</span> <strong class="block text-slate-800 dark:text-slate-200">028 3512 8899</strong></div>
                                <div><span class="text-slate-400">Nhân sự:</span> <span class="font-semibold text-slate-700 dark:text-slate-300">4 Bác sĩ, 6 Y tá, 3 KTV Spa</span></div>
                            </div>
                        </div>

                        <div class="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm overflow-hidden">
                            <div class="p-4 bg-slate-800 dark:bg-slate-700 text-white flex justify-between items-center">
                                <div>
                                    <h3 class="font-bold text-base">PetCare360 - Quận 7</h3>
                                    <p class="text-xs text-slate-300">Mã: CN-Q7 | Trưởng CN: BS. Hoàng Dung</p>
                                </div>
                                <span class="bg-teal-500 text-white text-[10px] font-bold px-2 py-0.5 rounded">Đang mở cửa</span>
                            </div>
                            <div class="p-4 space-y-3 text-xs">
                                <div><span class="text-slate-400">Địa chỉ:</span> <strong class="block text-slate-800 dark:text-slate-200">78 Nguyễn Đức Cảnh, Tân Phong, Quận 7, TP.HCM</strong></div>
                                <div><span class="text-slate-400">Hotline cấp cứu:</span> <strong class="block text-slate-800 dark:text-slate-200">028 5410 7788</strong></div>
                                <div><span class="text-slate-400">Nhân sự:</span> <span class="font-semibold text-slate-700 dark:text-slate-300">3 Bác sĩ, 5 Y tá, 3 KTV Spa</span></div>
                            </div>
                        </div>
                    </div>
                </section>

            </main>
        </div>

        <!-- CHI TIẾT ĐƠN HÀNG (DRAWER SIDE PANEL ADMIN) -->
        <div x-cloak x-show="orderDrawerOpen" @click="orderDrawerOpen = false" class="fixed inset-0 bg-slate-900/50 z-40 transition-opacity"></div>
        <aside x-cloak x-show="orderDrawerOpen" class="fixed top-0 right-0 z-50 w-full sm:w-[500px] lg:w-[580px] h-full bg-white dark:bg-slate-800 shadow-2xl flex flex-col drawer-slide"
               x-transition:enter="transition transform ease-out duration-300"
               x-transition:enter-start="translate-x-full"
               x-transition:enter-end="translate-x-0"
               x-transition:leave="transition transform ease-in duration-200"
               x-transition:leave-start="translate-x-0"
               x-transition:leave-end="translate-x-full">
            
            <div class="p-4 border-b border-slate-200 dark:border-slate-700 flex items-center justify-between bg-slate-50 dark:bg-slate-800/80">
                <div class="flex items-center gap-3">
                    <button @click="orderDrawerOpen = false" class="p-1 rounded-lg hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-500">
                        <i data-lucide="x" class="w-5 h-5"></i>
                    </button>
                    <div>
                        <div class="flex items-center gap-2">
                            <h3 class="text-base font-bold text-slate-900 dark:text-white" x-text="'#' + (selectedOrder ? selectedOrder.id : '')"></h3>
                            <span class="text-[10px] font-bold px-2 py-0.5 rounded"
                                  :class="selectedOrder?.type === 'SERVICE' ? 'bg-purple-100 text-purple-800' : 'bg-teal-100 text-teal-800'"
                                  x-text="selectedOrder?.type === 'SERVICE' ? 'Dịch vụ' : 'Sản phẩm'"></span>
                        </div>
                        <p class="text-xs text-slate-500">Khởi tạo: <span x-text="selectedOrder?.created || selectedOrder?.createdAt"></span></p>
                    </div>
                </div>

                <div class="flex items-center gap-2">
                    <button @click="showToast('Đã xuất file in hóa đơn PDF')" class="p-2 border border-slate-300 dark:border-slate-600 rounded-lg text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-700 text-xs font-semibold flex items-center gap-1" title="In phiếu giao / hóa đơn">
                        <i data-lucide="printer" class="w-4 h-4"></i> In
                    </button>
                </div>
            </div>

            <div class="flex-1 overflow-y-auto p-4 sm:p-5 space-y-5 text-xs sm:text-sm">
                <!-- Customer Info in Drawer -->
                <div class="bg-slate-50 dark:bg-slate-700/40 p-3.5 rounded-lg border border-slate-200 dark:border-slate-700 space-y-2">
                    <div class="flex items-center justify-between font-bold text-slate-800 dark:text-slate-200 border-b border-slate-200 dark:border-slate-600 pb-2">
                        <span class="flex items-center gap-1.5"><i data-lucide="user" class="w-4 h-4 text-teal-600"></i> Thông tin Khách hàng</span>
                        <button @click="openChatWithCustomer(selectedOrder?.customer)" class="text-xs text-teal-600 dark:text-teal-400 font-semibold hover:underline flex items-center gap-1">
                            <i data-lucide="message-square" class="w-3.5 h-3.5"></i> Chat với khách
                        </button>
                    </div>
                    <div class="grid grid-cols-2 gap-2 text-xs">
                        <div><span class="text-slate-400">Tên khách:</span> <strong class="block text-slate-700 dark:text-slate-200" x-text="selectedOrder?.customer"></strong></div>
                        <div><span class="text-slate-400">Số điện thoại:</span> <strong class="block text-slate-700 dark:text-slate-200" x-text="selectedOrder?.phone"></strong></div>
                    </div>
                    <div class="text-xs"><span class="text-slate-400">Địa chỉ giao / Chi nhánh:</span> <p class="font-medium text-slate-700 dark:text-slate-200" x-text="selectedOrder?.address"></p></div>
                </div>

                <!-- Update Status Buttons -->
                <div class="bg-amber-50/60 dark:bg-amber-950/30 p-3 rounded-xl border border-amber-200 dark:border-amber-800/60 space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="font-bold text-xs text-amber-900 dark:text-amber-300">Trạng thái đơn:</span>
                        <span class="font-bold text-xs uppercase px-2.5 py-0.5 rounded-full" 
                              :class="{
                                  'bg-amber-200 text-amber-900': selectedOrder?.status === 'PENDING' || selectedOrder?.status === 'Chờ xác nhận',
                                  'bg-blue-200 text-blue-900': selectedOrder?.status === 'PREPARING' || selectedOrder?.status === 'DELIVERING',
                                  'bg-emerald-200 text-emerald-900': selectedOrder?.status === 'COMPLETED',
                                  'bg-rose-200 text-rose-900': selectedOrder?.status === 'CANCELLED'
                              }"
                              x-text="formatOrderStatusLabel(selectedOrder?.status)"></span>
                    </div>
                    <div class="flex flex-wrap gap-1.5 pt-1">
                        <button @click="updateOrderStatus(selectedOrder, 'PREPARING')" class="px-2.5 py-1 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-lg text-xs">Duyệt & Chuẩn bị</button>
                        <button @click="updateOrderStatus(selectedOrder, 'DELIVERING')" class="px-2.5 py-1 bg-indigo-600 hover:bg-indigo-700 text-white font-bold rounded-lg text-xs">Đang giao / Thực hiện</button>
                        <button @click="updateOrderStatus(selectedOrder, 'COMPLETED')" class="px-2.5 py-1 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-lg text-xs">Hoàn thành</button>
                        <button @click="updateOrderStatus(selectedOrder, 'CANCELLED')" class="px-2.5 py-1 bg-rose-600 hover:bg-rose-700 text-white font-bold rounded-lg text-xs">Hủy đơn</button>
                    </div>
                </div>

                <!-- Items Table -->
                <div>
                    <h4 class="font-bold text-slate-800 dark:text-slate-200 mb-2 flex items-center gap-1.5">
                        <i data-lucide="shopping-bag" class="w-4 h-4 text-teal-600"></i> Danh sách Chi tiết Đơn
                    </h4>
                    <div class="border border-slate-200 dark:border-slate-700 rounded-lg overflow-hidden">
                        <table class="w-full text-left text-xs">
                            <thead class="bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 font-semibold">
                                <tr>
                                    <th class="p-2.5">Sản phẩm / Dịch vụ</th>
                                    <th class="p-2.5 text-center">SL</th>
                                    <th class="p-2.5 text-right">Đơn giá</th>
                                    <th class="p-2.5 text-right">Thành tiền</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-100 dark:divide-slate-700">
                                <template x-for="item in (selectedOrder ? selectedOrder.items : [])" :key="item.name">
                                    <tr>
                                        <td class="p-2.5">
                                            <div class="font-semibold text-slate-800 dark:text-slate-200" x-text="item.name"></div>
                                            <template x-if="item.bookingDate || item.selectedPet">
                                                <div class="text-[10px] text-teal-600 font-medium" x-text="(item.bookingDate ? 'Lịch: ' + item.bookingDate : '') + (item.selectedPet ? ' • Pet: ' + item.selectedPet : '')"></div>
                                            </template>
                                        </td>
                                        <td class="p-2.5 text-center" x-text="item.quantity || item.qty || 1"></td>
                                        <td class="p-2.5 text-right" x-text="formatCurrency(item.price)"></td>
                                        <td class="p-2.5 text-right font-bold" x-text="formatCurrency((item.quantity || item.qty || 1) * item.price)"></td>
                                    </tr>
                                </template>
                            </tbody>
                        </table>
                        <div class="p-3 bg-slate-50 dark:bg-slate-700/30 border-t border-slate-200 dark:border-slate-700 space-y-1 text-xs">
                            <div class="flex justify-between font-bold text-slate-900 dark:text-white text-sm pt-1">
                                <span>Tổng thanh toán:</span>
                                <span class="text-teal-600 dark:text-teal-400" x-text="formatCurrency(selectedOrder?.total || selectedOrder?.totalAmount || 0)"></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="p-4 border-t border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800/90 flex justify-end">
                <button @click="orderDrawerOpen = false" class="px-4 py-2 bg-slate-200 dark:bg-slate-700 text-slate-800 dark:text-slate-200 rounded-lg text-xs font-bold">Đóng</button>
            </div>
        </aside>

    </div>
"""
