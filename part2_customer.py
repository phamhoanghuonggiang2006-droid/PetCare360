# -*- coding: utf-8 -*-
CUSTOMER_HTML = """
    <!-- ======================================================== -->
    <!-- VIEW 1: GIAO DIỆN KHÁCH HÀNG (CUSTOMER VIEW - MẶC ĐỊNH) -->
    <!-- ======================================================== -->
    <div x-show="currentRole === 'customer'" class="min-h-screen flex flex-col pb-16 md:pb-0" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 scale-98" x-transition:enter-end="opacity-100 scale-100">
        
        <!-- Header Navigation Customer -->
        <header class="sticky top-0 z-30 bg-white/95 backdrop-blur border-b border-slate-200 shadow-sm">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex items-center justify-between h-16">
                    <!-- Logo & New Slogan -->
                    <div class="flex items-center gap-3 cursor-pointer" @click="activeCustomerTab = 'home'">
                        <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-brand-600 to-teal-400 flex items-center justify-center text-white shadow-md shadow-brand-500/20">
                            <i class="fa-solid font-bold fa-paw text-xl"></i>
                        </div>
                        <div>
                            <span class="text-xl font-bold bg-gradient-to-r from-brand-700 to-teal-500 bg-clip-text text-transparent">PetCare<span class="text-accent-500">360</span></span>
                            <span class="block text-[9px] text-brand-600 font-bold tracking-wider uppercase -mt-0.5">ĐỒNG HÀNH TRỌN ĐỜI CÙNG THÚ CƯNG</span>
                        </div>
                    </div>

                    <!-- Desktop Navigation Menu -->
                    <nav class="hidden md:flex items-center gap-1 lg:gap-1.5">
                        <button @click="activeCustomerTab = 'home'" :class="activeCustomerTab === 'home' ? 'text-brand-700 bg-brand-50 font-bold' : 'text-slate-600 hover:text-brand-600 hover:bg-slate-50'" class="px-3 py-2 rounded-xl text-xs lg:text-sm transition flex items-center gap-1.5">
                            <i class="fa-solid fa-house"></i>Trang Chủ
                        </button>
                        <button @click="activeCustomerTab = 'petshare'" :class="activeCustomerTab === 'petshare' ? 'text-brand-700 bg-brand-50 font-bold' : 'text-slate-600 hover:text-brand-600 hover:bg-slate-50'" class="px-3 py-2 rounded-xl text-xs lg:text-sm transition flex items-center gap-1.5 relative">
                            <i class="fa-solid fa-newspaper text-amber-500"></i>PetShare360
                            <span class="text-[9px] bg-rose-500 text-white font-bold px-1.5 py-0.2 rounded-full">Hot</span>
                        </button>
                        <button @click="activeCustomerTab = 'shop'" :class="activeCustomerTab === 'shop' ? 'text-brand-700 bg-brand-50 font-bold' : 'text-slate-600 hover:text-brand-600 hover:bg-slate-50'" class="px-3 py-2 rounded-xl text-xs lg:text-sm transition flex items-center gap-1.5">
                            <i class="fa-solid fa-box-open"></i>Sản Phẩm
                        </button>
                        <button @click="activeCustomerTab = 'booking'" :class="activeCustomerTab === 'booking' ? 'text-brand-700 bg-brand-50 font-bold' : 'text-slate-600 hover:text-brand-600 hover:bg-slate-50'" class="px-3 py-2 rounded-xl text-xs lg:text-sm transition flex items-center gap-1.5">
                            <i class="fa-solid fa-scissors"></i>Dịch Vụ
                        </button>
                        <button @click="activeCustomerTab = 'orders'" :class="activeCustomerTab === 'orders' ? 'text-brand-700 bg-brand-50 font-bold' : 'text-slate-600 hover:text-brand-600 hover:bg-slate-50'" class="px-3 py-2 rounded-xl text-xs lg:text-sm transition flex items-center gap-1.5 relative">
                            <i class="fa-solid fa-receipt"></i>Đơn Hàng
                            <span x-show="customerOrders.length > 0" class="ml-1 px-1.5 py-0.2 text-[10px] bg-amber-500 text-white font-bold rounded-full" x-text="customerOrders.length"></span>
                        </button>
                        <button @click="activeCustomerTab = 'profile'" :class="activeCustomerTab === 'profile' ? 'text-brand-700 bg-brand-50 font-bold' : 'text-slate-600 hover:text-brand-600 hover:bg-slate-50'" class="px-3 py-2 rounded-xl text-xs lg:text-sm transition flex items-center gap-1.5">
                            <i class="fa-solid fa-user-gear"></i>Hồ Sơ & Pets
                        </button>
                    </nav>

                    <!-- Actions: Chat CSKH, Cart & Account (Login / Profile) -->
                    <div class="flex items-center gap-2 sm:gap-3">
                        <!-- Nút Chat CSKH trực tiếp (Bên trái giỏ hàng) -->
                        <button @click="openCustomerSupportChat()" class="relative p-2.5 rounded-xl text-slate-700 hover:text-brand-600 hover:bg-brand-50 transition border border-slate-200 flex items-center gap-1.5 group" title="Chat hỗ trợ CSKH 24/7">
                            <i class="fa-solid fa-headset text-base text-brand-600 group-hover:scale-110 transition"></i>
                            <span class="hidden xl:inline text-xs font-bold text-slate-700">Chat CSKH</span>
                            <span class="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                        </button>

                        <!-- Nút Giỏ hàng -->
                        <button @click="cartOpen = true" class="relative p-2.5 rounded-xl text-slate-700 hover:text-brand-600 hover:bg-brand-50 transition border border-slate-200">
                            <i class="fa-solid fa-cart-shopping text-base"></i>
                            <span x-show="cartItemsCount > 0" x-text="cartItemsCount" class="absolute -top-1.5 -right-1.5 bg-accent-500 text-white font-bold text-[10px] w-5 h-5 rounded-full flex items-center justify-center shadow-sm animate-pulse"></span>
                        </button>

                        <!-- Khối Tài Khoản: Nếu chưa đăng nhập hiện Đăng nhập, nếu đã đăng nhập hiện thông tin và nút Đăng xuất -->
                        <div class="pl-2 border-l border-slate-200">
                            <template x-if="!isLoggedIn">
                                <button @click="openLoginModal()" class="flex items-center gap-2 bg-gradient-to-r from-brand-600 to-teal-500 hover:from-brand-700 hover:to-teal-600 text-white font-bold text-xs sm:text-sm px-3.5 py-2 rounded-xl shadow-md transition transform active:scale-95">
                                    <i class="fa-solid fa-right-to-bracket text-xs"></i>
                                    <span>Đăng nhập</span>
                                </button>
                            </template>

                            <template x-if="isLoggedIn">
                                <div class="flex items-center gap-2">
                                    <div @click="activeCustomerTab = 'profile'" class="flex items-center gap-2 cursor-pointer hover:opacity-85 transition">
                                        <img :src="customerProfile.avatar" :alt="customerProfile.name" class="w-9 h-9 rounded-full object-cover border-2 border-brand-500 shadow-sm">
                                        <div class="hidden lg:block text-left">
                                            <p class="text-xs font-bold text-slate-800 leading-none truncate max-w-[110px]" x-text="customerProfile.name"></p>
                                            <p class="text-[10px] text-brand-600 font-medium" x-text="customerProfile.rank"></p>
                                        </div>
                                    </div>
                                    <!-- Nút Đăng xuất Khách hàng -->
                                    <button @click="logout()" class="p-2 rounded-xl text-slate-400 hover:text-rose-600 hover:bg-rose-50 transition border border-slate-200 ml-1" title="Đăng xuất tài khoản">
                                        <i class="fa-solid fa-arrow-right-from-bracket text-xs"></i>
                                    </button>
                                </div>
                            </template>
                        </div>
                    </div>
                </div>
            </div>
        </header>

        <!-- Main Content Area Customer -->
        <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">

            <!-- Banner Announcement -->
            <div class="mb-6 bg-gradient-to-r from-brand-600 via-teal-600 to-emerald-600 rounded-2xl p-4 sm:p-6 text-white shadow-lg relative overflow-hidden">
                <div class="absolute -right-10 -bottom-10 opacity-20 text-9xl pointer-events-none">
                    <i class="fa-solid fa-bone"></i>
                </div>
                <div class="relative z-10 max-w-full overflow-hidden">
                    <div class="flex items-center gap-2 mb-2">
                        <span class="bg-amber-400 text-slate-900 text-xs font-bold px-2.5 py-1 rounded-md uppercase tracking-wider inline-block">Khuyến mãi hỏa tốc</span>
                        <span class="bg-white/20 text-white text-[10px] font-semibold px-2 py-0.5 rounded-full">Ưu đãi tuần lễ Pet Care</span>
                    </div>
                    <h2 class="text-sm sm:text-lg md:text-xl font-extrabold mb-1 whitespace-nowrap truncate leading-tight">Ưu đãi spa & chăm sóc răng miệng cho thú cưng 30%</h2>
                    <p class="text-brand-100 text-xs sm:text-sm mb-4">Nhập mã <span class="font-bold underline text-white">PETCARE30</span> để giảm ngay cho mọi đơn hàng từ 300.000đ.</p>
                    <div class="flex gap-2">
                        <button @click="activeCustomerTab = 'shop'" class="bg-white text-brand-700 hover:bg-brand-50 text-xs sm:text-sm font-bold px-4 py-2 rounded-xl transition shadow">Khám Phá Sản Phẩm</button>
                        <button @click="activeCustomerTab = 'booking'" class="bg-amber-500 hover:bg-amber-600 text-white text-xs sm:text-sm font-bold px-4 py-2 rounded-xl transition shadow">Đặt Lịch Spa</button>
                    </div>
                </div>
            </div>

            <!-- TAB 1: TRANG CHỦ (HOME) -->
            <div x-show="activeCustomerTab === 'home'" class="space-y-8" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                <!-- Quick Categories -->
                <div>
                    <h3 class="text-lg font-bold text-slate-800 mb-4 flex items-center gap-2">
                        <i class="fa-solid fa-shapes text-brand-600"></i> Dịch Vụ & Danh Mục Hot
                    </h3>
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
                        <div @click="activeCustomerTab = 'shop'; filterCategory = 'food'" class="bg-white p-4 rounded-2xl shadow-sm border border-slate-100 hover:shadow-md hover:border-brand-300 transition cursor-pointer text-center group">
                            <div class="w-12 h-12 rounded-xl bg-orange-100 text-orange-600 flex items-center justify-center mx-auto mb-2 text-xl group-hover:scale-110 transition">
                                <i class="fa-solid fa-bowl-food"></i>
                            </div>
                            <h4 class="font-semibold text-slate-800 text-sm">Thức Ăn Thú Cưng</h4>
                            <p class="text-xs text-slate-500">Hạt, Pate, Bánh thưởng</p>
                        </div>
                        <div @click="activeCustomerTab = 'shop'; filterCategory = 'supplies'" class="bg-white p-4 rounded-2xl shadow-sm border border-slate-100 hover:shadow-md hover:border-brand-300 transition cursor-pointer text-center group">
                            <div class="w-12 h-12 rounded-xl bg-teal-100 text-teal-600 flex items-center justify-center mx-auto mb-2 text-xl group-hover:scale-110 transition">
                                <i class="fa-solid fa-shield-cat"></i>
                            </div>
                            <h4 class="font-semibold text-slate-800 text-sm">Phụ Kiện & Đồ Chơi</h4>
                            <p class="text-xs text-slate-500">Vòng cổ, chuồng, cát cún</p>
                        </div>
                        <div @click="activeCustomerTab = 'booking'" class="bg-white p-4 rounded-2xl shadow-sm border border-slate-100 hover:shadow-md hover:border-brand-300 transition cursor-pointer text-center group">
                            <div class="w-12 h-12 rounded-xl bg-amber-100 text-amber-600 flex items-center justify-center mx-auto mb-2 text-xl group-hover:scale-110 transition">
                                <i class="fa-solid fa-scissors"></i>
                            </div>
                            <h4 class="font-semibold text-slate-800 text-sm">Grooming & Spa</h4>
                            <p class="text-xs text-slate-500">Cắt tỉa, tắm sấy tận tình</p>
                        </div>
                        <div @click="activeCustomerTab = 'booking'" class="bg-white p-4 rounded-2xl shadow-sm border border-slate-100 hover:shadow-md hover:border-brand-300 transition cursor-pointer text-center group">
                            <div class="w-12 h-12 rounded-xl bg-rose-100 text-rose-600 flex items-center justify-center mx-auto mb-2 text-xl group-hover:scale-110 transition">
                                <i class="fa-solid fa-user-doctor"></i>
                            </div>
                            <h4 class="font-semibold text-slate-800 text-sm">Thú Y & Home Visit</h4>
                            <p class="text-xs text-slate-500">Tiêm phòng, khám tại nhà</p>
                        </div>
                    </div>
                </div>

                <!-- Stores & Service Providers Section -->
                <div>
                    <div class="flex items-center justify-between mb-4">
                        <h3 class="text-lg font-bold text-slate-800 flex items-center gap-2">
                            <i class="fa-solid fa-store text-brand-600"></i> Cơ Sở & Cửa Hàng Gần Bạn
                        </h3>
                        <button @click="activeCustomerTab = 'booking'" class="text-brand-600 font-semibold text-sm hover:underline flex items-center gap-1">
                            Xem danh sách <i class="fa-solid fa-arrow-right text-xs"></i>
                        </button>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
                        <template x-for="store in storeProviders" :key="store.id">
                            <div class="bg-white rounded-2xl border border-slate-100 shadow-sm overflow-hidden hover:shadow-md transition flex flex-col justify-between">
                                <div class="p-4">
                                    <div class="flex items-start justify-between gap-2 mb-2">
                                        <h4 class="font-bold text-slate-800 text-base" x-text="store.name"></h4>
                                        <span class="bg-slate-100 text-slate-600 text-[10px] font-semibold px-2 py-0.5 rounded-full flex items-center gap-1 shrink-0">
                                            <i class="fa-solid fa-location-dot text-brand-600"></i> <span x-text="store.distance"></span>
                                        </span>
                                    </div>
                                    <p class="text-xs text-slate-500 mb-3 flex items-center gap-1">
                                        <i class="fa-regular fa-map text-slate-400"></i> <span x-text="store.address"></span>
                                    </p>
                                    <div class="flex items-center gap-2 mb-3">
                                        <div class="flex items-center text-amber-400 text-xs">
                                            <i class="fa-solid fa-star"></i>
                                            <span class="font-bold text-slate-800 ml-1" x-text="store.rating"></span>
                                        </div>
                                        <span class="text-xs text-slate-400" x-text="'(' + store.reviewsCount + ' đánh giá)'"></span>
                                    </div>
                                    <div class="flex flex-wrap gap-1.5 mb-3">
                                        <template x-for="tag in store.tags" :key="tag">
                                            <span class="bg-brand-50 text-brand-700 text-[10px] font-semibold px-2 py-0.5 rounded-md" x-text="tag"></span>
                                        </template>
                                    </div>
                                </div>
                                <div class="px-4 py-3 bg-slate-50 border-t border-slate-100 flex justify-between items-center">
                                    <span class="text-xs font-semibold text-emerald-600"><i class="fa-solid fa-clock mr-1"></i>Đang mở cửa</span>
                                    <button @click="activeCustomerTab = 'booking'" class="bg-brand-600 hover:bg-brand-700 text-white font-bold text-xs px-3 py-1.5 rounded-xl transition">
                                        Đặt lịch
                                    </button>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>

                <!-- Featured Products -->
                <div>
                    <div class="flex items-center justify-between mb-4">
                        <h3 class="text-lg font-bold text-slate-800 flex items-center gap-2">
                            <i class="fa-solid fa-fire text-amber-500"></i> Sản Phẩm Bán Chạy
                        </h3>
                        <button @click="activeCustomerTab = 'shop'" class="text-brand-600 font-semibold text-sm hover:underline flex items-center gap-1">
                            Xem tất cả 12 sản phẩm <i class="fa-solid fa-arrow-right text-xs"></i>
                        </button>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-5">
                        <template x-for="item in products.slice(0, 4)" :key="item.id">
                            <div class="bg-white rounded-2xl border border-slate-100 shadow-sm overflow-hidden flex flex-col hover:shadow-md transition relative group">
                                <span x-show="item.discount" class="absolute top-3 right-3 bg-rose-500 text-white font-extrabold text-[10px] px-2 py-0.5 rounded-lg z-10" x-text="'-' + item.discount + '%'"></span>

                                <div class="relative aspect-square overflow-hidden bg-slate-100 cursor-pointer" @click="openProductDetail(item)">
                                    <img :src="item.image" :alt="item.name" class="w-full h-full object-cover group-hover:scale-105 transition duration-300">
                                    <span class="absolute top-3 left-3 bg-brand-600 text-white text-[10px] font-bold px-2 py-1 rounded-lg uppercase tracking-wide" x-text="item.categoryName"></span>
                                </div>
                                <div class="p-4 flex-1 flex flex-col justify-between">
                                    <div>
                                        <h4 @click="openProductDetail(item)" class="font-bold text-slate-800 line-clamp-1 mb-1 text-base hover:text-brand-600 cursor-pointer transition" x-text="item.name"></h4>
                                        <div class="flex items-center gap-1.5 mb-2 text-xs">
                                            <div class="flex text-amber-400">
                                                <i class="fa-solid fa-star"></i>
                                            </div>
                                            <span class="font-bold text-slate-800 text-[11px]" x-text="item.rating"></span>
                                            <span class="text-slate-400 text-[10px]" x-text="'(' + item.sold + ' đã bán)'"></span>
                                        </div>
                                        <p class="text-xs text-slate-500 line-clamp-1 mb-3" x-text="item.description"></p>
                                    </div>
                                    <div class="flex items-center justify-between pt-2 border-t border-slate-100">
                                        <span class="text-brand-700 font-extrabold text-base" x-text="formatCurrency(item.price)"></span>
                                        <div class="flex gap-1.5">
                                            <button @click="openProductDetail(item)" class="p-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs" title="Xem chi tiết">
                                                <i class="fa-solid fa-eye"></i>
                                            </button>
                                            <button @click="addToCart(item)" class="bg-brand-600 hover:bg-brand-700 text-white px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1 transition active:scale-95">
                                                <i class="fa-solid fa-plus"></i> Thêm
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>

                <!-- BÀI VIẾT PETSHARE360 ĐƯỢC NHIỀU NGƯỜI QUAN TÂM (YÊU CẦU MỤC 12) -->
                <div class="bg-gradient-to-br from-teal-50/70 via-white to-amber-50/50 rounded-3xl p-6 sm:p-8 border border-teal-100 shadow-sm space-y-6">
                    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3">
                        <div>
                            <span class="bg-amber-100 text-amber-800 text-[11px] font-bold px-3 py-1 rounded-full uppercase tracking-wider inline-flex items-center gap-1.5">
                                <i class="fa-solid fa-fire text-amber-500"></i> Xu hướng cẩm nang
                            </span>
                            <h3 class="text-xl font-extrabold text-slate-800 mt-2">🔥 PetShare360 - Góc Chia Sẻ Được Quan Tâm Nhất</h3>
                            <p class="text-xs text-slate-500">Tổng hợp các bài viết kinh nghiệm nuôi dưỡng, mẹo vặt chăm sóc và cẩm nang y tế từ đội ngũ Bác sĩ Thú y PetCare360.</p>
                        </div>
                        <button @click="activeCustomerTab = 'petshare'" class="bg-white hover:bg-teal-50 text-brand-700 font-bold text-xs sm:text-sm px-4 py-2.5 rounded-xl border border-teal-200 shadow-xs transition flex items-center gap-1.5 shrink-0">
                            Xem tất cả PetShare360 <i class="fa-solid fa-arrow-right text-xs"></i>
                        </button>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                        <template x-for="art in articles.slice(0, 3)" :key="art.id">
                            <div @click="openArticleDetail(art)" class="bg-white rounded-2xl border border-slate-100 shadow-xs hover:shadow-md transition overflow-hidden cursor-pointer flex flex-col justify-between group">
                                <div>
                                    <div class="relative aspect-video overflow-hidden bg-slate-100">
                                        <img :src="art.image" :alt="art.title" class="w-full h-full object-cover group-hover:scale-105 transition duration-300">
                                        <span class="absolute top-3 left-3 bg-slate-900/80 backdrop-blur-sm text-white text-[10px] font-bold px-2.5 py-1 rounded-lg" x-text="art.category"></span>
                                        <span class="absolute bottom-3 right-3 bg-white/90 text-slate-700 text-[10px] font-medium px-2 py-0.5 rounded-md flex items-center gap-1">
                                            <i class="fa-solid fa-eye text-teal-600"></i> <span x-text="art.views"></span>
                                        </span>
                                    </div>
                                    <div class="p-4 space-y-2">
                                        <div class="text-[11px] text-slate-400 flex items-center gap-2">
                                            <span><i class="fa-solid fa-user-pen mr-1 text-brand-600"></i><span x-text="art.author"></span></span>
                                            <span>•</span>
                                            <span><i class="fa-regular fa-clock mr-1"></i><span x-text="art.date"></span></span>
                                        </div>
                                        <h4 class="font-bold text-slate-800 text-sm leading-snug line-clamp-2 group-hover:text-brand-600 transition" x-text="art.title"></h4>
                                        <p class="text-xs text-slate-500 line-clamp-2" x-text="art.summary"></p>
                                    </div>
                                </div>
                                <div class="p-4 pt-0 flex justify-between items-center text-xs font-bold text-brand-600">
                                    <span>Đọc chi tiết</span>
                                    <i class="fa-solid fa-arrow-right group-hover:translate-x-1 transition"></i>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>
            </div>

            <!-- TAB 2: PETSHARE360 (CỘNG ĐỒNG & CẨM NANG - YÊU CẦU MỤC 3) -->
            <div x-show="activeCustomerTab === 'petshare'" class="space-y-6" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                <!-- Header PetShare360 -->
                <div class="bg-gradient-to-r from-teal-600 via-brand-600 to-emerald-600 rounded-3xl p-6 sm:p-8 text-white relative overflow-hidden shadow-lg">
                    <div class="absolute -right-8 -bottom-8 opacity-15 text-9xl pointer-events-none">
                        <i class="fa-solid fa-newspaper"></i>
                    </div>
                    <div class="relative z-10 max-w-2xl space-y-2">
                        <span class="bg-amber-400 text-slate-900 text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider inline-block">Cộng Đồng PetCare360</span>
                        <h2 class="text-2xl sm:text-3xl font-black">PetShare360 - Cẩm Nang & Kinh Nghiệm Nuôi Thú Cưng</h2>
                        <p class="text-brand-100 text-xs sm:text-sm">Tổng hợp các bài viết hướng dẫn chuyên sâu từ Đội ngũ Bác sĩ Thú y và Chuyên viên Grooming hàng đầu.</p>
                    </div>
                </div>

                <!-- Search & Category Filters -->
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 bg-white p-4 rounded-2xl border border-slate-100 shadow-sm">
                    <div class="flex gap-2 overflow-x-auto w-full sm:w-auto pb-2 sm:pb-0 hide-scrollbar">
                        <button @click="filterArticleCat = 'all'" :class="filterArticleCat === 'all' ? 'bg-brand-600 text-white font-bold' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="px-4 py-2 rounded-xl text-xs whitespace-nowrap transition">Tất cả bài viết (<span x-text="articles.length"></span>)</button>
                        <button @click="filterArticleCat = 'Dinh dưỡng'" :class="filterArticleCat === 'Dinh dưỡng' ? 'bg-brand-600 text-white font-bold' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="px-4 py-2 rounded-xl text-xs whitespace-nowrap transition">Dinh dưỡng</button>
                        <button @click="filterArticleCat = 'Y tế & Sức khỏe'" :class="filterArticleCat === 'Y tế & Sức khỏe' ? 'bg-brand-600 text-white font-bold' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="px-4 py-2 rounded-xl text-xs whitespace-nowrap transition">Y tế & Sức khỏe</button>
                        <button @click="filterArticleCat = 'Chăm sóc & Vệ sinh'" :class="filterArticleCat === 'Chăm sóc & Vệ sinh' ? 'bg-brand-600 text-white font-bold' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="px-4 py-2 rounded-xl text-xs whitespace-nowrap transition">Spa & Vệ sinh</button>
                        <button @click="filterArticleCat = 'Huấn luyện'" :class="filterArticleCat === 'Huấn luyện' ? 'bg-brand-600 text-white font-bold' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="px-4 py-2 rounded-xl text-xs whitespace-nowrap transition">Huấn luyện</button>
                    </div>
                    <div class="relative w-full sm:w-72">
                        <input type="text" x-model="searchArticleQuery" placeholder="Tìm kiếm bài viết hướng dẫn..." class="w-full pl-9 pr-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs focus:outline-none focus:ring-2 focus:ring-brand-500">
                        <i class="fa-solid fa-magnifying-glass absolute left-3 top-3 text-slate-400 text-xs"></i>
                    </div>
                </div>

                <!-- Articles Grid (6 bài viết) -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                    <template x-for="art in filteredArticles" :key="art.id">
                        <div @click="openArticleDetail(art)" class="bg-white rounded-3xl border border-slate-100 shadow-sm hover:shadow-lg transition duration-200 overflow-hidden cursor-pointer flex flex-col justify-between group">
                            <div>
                                <div class="relative aspect-video overflow-hidden bg-slate-100">
                                    <img :src="art.image" :alt="art.title" class="w-full h-full object-cover group-hover:scale-105 transition duration-300">
                                    <span class="absolute top-3 left-3 bg-brand-600 text-white text-[10px] font-bold px-3 py-1 rounded-lg uppercase tracking-wide" x-text="art.category"></span>
                                    <span class="absolute bottom-3 right-3 bg-slate-900/70 backdrop-blur text-white text-[10px] font-medium px-2 py-0.5 rounded-md flex items-center gap-1">
                                        <i class="fa-solid fa-eye text-teal-300"></i> <span x-text="art.views"></span>
                                    </span>
                                </div>
                                <div class="p-5 space-y-2.5">
                                    <div class="text-[11px] text-slate-400 flex items-center gap-2">
                                        <span class="font-bold text-slate-700"><i class="fa-solid fa-user-doctor mr-1 text-teal-600"></i><span x-text="art.author"></span></span>
                                        <span>•</span>
                                        <span><i class="fa-regular fa-clock mr-1"></i><span x-text="art.date"></span></span>
                                    </div>
                                    <h4 class="font-bold text-slate-800 text-base leading-snug group-hover:text-brand-600 transition" x-text="art.title"></h4>
                                    <p class="text-xs text-slate-500 line-clamp-3 leading-relaxed" x-text="art.summary"></p>
                                </div>
                            </div>
                            <div class="p-5 pt-0 flex justify-between items-center text-xs font-bold text-brand-600 border-t border-slate-50 pt-3">
                                <span>Đọc toàn văn bài viết</span>
                                <i class="fa-solid fa-arrow-right group-hover:translate-x-1.5 transition"></i>
                            </div>
                        </div>
                    </template>
                </div>
            </div>

            <!-- TAB 3: SẢN PHẨM (ĐỔI TÊN TỪ CỬA HÀNG - YÊU CẦU MỤC 9 & 10) -->
            <div x-show="activeCustomerTab === 'shop'" class="space-y-6" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 bg-white p-4 rounded-2xl border border-slate-100 shadow-sm">
                    <div class="flex gap-2 overflow-x-auto w-full sm:w-auto pb-2 sm:pb-0 hide-scrollbar">
                        <button @click="filterCategory = 'all'" :class="filterCategory === 'all' ? 'bg-brand-600 text-white font-bold' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="px-4 py-2 rounded-xl text-xs whitespace-nowrap transition">Tất cả (<span x-text="products.length"></span>)</button>
                        <button @click="filterCategory = 'food'" :class="filterCategory === 'food' ? 'bg-brand-600 text-white font-bold' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="px-4 py-2 rounded-xl text-xs whitespace-nowrap transition">Thức ăn & Dinh dưỡng</button>
                        <button @click="filterCategory = 'supplies'" :class="filterCategory === 'supplies' ? 'bg-brand-600 text-white font-bold' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="px-4 py-2 rounded-xl text-xs whitespace-nowrap transition">Phụ kiện & Vệ sinh</button>
                        <button @click="filterCategory = 'medical'" :class="filterCategory === 'medical' ? 'bg-brand-600 text-white font-bold' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'" class="px-4 py-2 rounded-xl text-xs whitespace-nowrap transition">Thuốc & Y tế</button>
                    </div>
                    <div class="relative w-full sm:w-64">
                        <input type="text" x-model="searchQuery" placeholder="Tìm kiếm trong 12 sản phẩm..." class="w-full pl-9 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-xl text-xs focus:outline-none focus:ring-2 focus:ring-brand-500">
                        <i class="fa-solid fa-magnifying-glass absolute left-3 top-2.5 text-slate-400 text-xs"></i>
                    </div>
                </div>

                <!-- Product Grid (12 sản phẩm) -->
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-5">
                    <template x-for="item in filteredProducts" :key="item.id">
                        <div class="bg-white rounded-2xl border border-slate-100 shadow-sm overflow-hidden flex flex-col hover:shadow-md transition relative group">
                            <span x-show="item.discount" class="absolute top-3 right-3 bg-rose-500 text-white font-extrabold text-[10px] px-2 py-0.5 rounded-lg z-10" x-text="'-' + item.discount + '%'"></span>

                            <div class="relative aspect-square overflow-hidden bg-slate-100 cursor-pointer" @click="openProductDetail(item)">
                                <img :src="item.image" :alt="item.name" class="w-full h-full object-cover group-hover:scale-105 transition duration-300">
                                <span class="absolute top-3 left-3 bg-brand-600 text-white text-[10px] font-bold px-2 py-1 rounded-lg uppercase" x-text="item.categoryName"></span>
                            </div>
                            <div class="p-4 flex-1 flex flex-col justify-between">
                                <div>
                                    <h4 @click="openProductDetail(item)" class="font-bold text-slate-800 line-clamp-1 mb-1 text-base hover:text-brand-600 cursor-pointer transition" x-text="item.name"></h4>
                                    <div class="flex items-center gap-1.5 mb-2 text-xs">
                                        <div class="flex text-amber-400">
                                            <i class="fa-solid fa-star"></i>
                                        </div>
                                        <span class="font-bold text-slate-800 text-[11px]" x-text="item.rating"></span>
                                        <span class="text-slate-400 text-[10px]" x-text="'(' + item.sold + ' đã bán)'"></span>
                                    </div>
                                    <p class="text-xs text-slate-500 line-clamp-2 mb-3" x-text="item.description"></p>
                                </div>
                                <div class="flex items-center justify-between pt-2 border-t border-slate-100">
                                    <span class="text-brand-700 font-extrabold text-base" x-text="formatCurrency(item.price)"></span>
                                    <div class="flex gap-1.5">
                                        <button @click="openProductDetail(item)" class="p-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs" title="Xem chi tiết sản phẩm">
                                            <i class="fa-solid fa-eye"></i>
                                        </button>
                                        <button @click="addToCart(item)" class="bg-brand-600 hover:bg-brand-700 text-white px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1 transition active:scale-95">
                                            <i class="fa-solid fa-cart-plus"></i> Thêm giỏ
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </template>
                </div>
            </div>

            <!-- TAB 4: DỊCH VỤ (12 DỊCH VỤ - YÊU CẦU MỤC 8) -->
            <div x-show="activeCustomerTab === 'booking'" class="space-y-6" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                <div class="bg-white p-6 rounded-3xl border border-slate-100 shadow-sm space-y-4">
                    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
                        <div>
                            <h3 class="text-xl font-black text-slate-800">Dịch Vụ Chăm Sóc & Y Tế Thú Cưng Chuyên Nghiệp (12 Gói)</h3>
                            <p class="text-xs text-slate-500">Mỗi dịch vụ được thực hiện bởi đội ngũ Bác sĩ Thú y & KTV Spa chứng chỉ quốc tế. Nhấn vào dịch vụ để xem quy trình chi tiết.</p>
                        </div>
                        <span class="bg-emerald-100 text-emerald-800 text-xs font-bold px-3 py-1.5 rounded-full flex items-center gap-1.5 shrink-0">
                            <i class="fa-solid fa-circle-check"></i> Tiêu chuẩn Thú Y 5 Sao
                        </span>
                    </div>

                    <!-- 12 Services Grid -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 pt-2">
                        <template x-for="service in servicesList" :key="service.id">
                            <div class="border border-slate-200 rounded-2xl overflow-hidden hover:border-brand-500 hover:shadow-md transition bg-white flex flex-col justify-between group">
                                <div>
                                    <div class="relative aspect-video overflow-hidden bg-slate-100 cursor-pointer" @click="openServiceDetail(service)">
                                        <img :src="service.image" :alt="service.name" class="w-full h-full object-cover group-hover:scale-105 transition duration-300">
                                        <div class="absolute top-3 left-3 w-9 h-9 rounded-xl bg-brand-600/90 backdrop-blur text-white flex items-center justify-center text-sm shadow">
                                            <i :class="service.icon"></i>
                                        </div>
                                        <div class="absolute bottom-3 right-3 bg-white/90 backdrop-blur px-2 py-0.5 rounded-md text-[11px] font-bold text-slate-800 flex items-center gap-1 shadow-sm">
                                            <i class="fa-solid fa-star text-amber-400"></i>
                                            <span x-text="service.rating"></span>
                                            <span class="text-slate-400 font-normal" x-text="'(' + service.reviewsCount + ')'"></span>
                                        </div>
                                    </div>

                                    <div class="p-4 space-y-2">
                                        <h4 @click="openServiceDetail(service)" class="font-bold text-slate-800 text-base leading-snug hover:text-brand-600 cursor-pointer transition line-clamp-1" x-text="service.name"></h4>
                                        <p class="text-xs text-slate-500 line-clamp-2" x-text="service.description"></p>
                                        
                                        <div class="flex flex-wrap gap-1 pt-1">
                                            <template x-for="tag in service.tags" :key="tag">
                                                <span class="bg-slate-100 text-slate-600 text-[10px] font-semibold px-2 py-0.5 rounded-md" x-text="tag"></span>
                                            </template>
                                        </div>
                                    </div>
                                </div>

                                <div class="p-4 pt-0 border-t border-slate-100 flex items-center justify-between mt-2 pt-3">
                                    <div>
                                        <span class="text-[10px] text-slate-400 block">Giá trọn gói:</span>
                                        <span class="text-brand-700 font-black text-base" x-text="formatCurrency(service.price)"></span>
                                    </div>
                                    <div class="flex gap-2">
                                        <button @click="openServiceDetail(service)" class="px-3 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs rounded-xl transition" title="Xem quy trình">
                                            Chi tiết
                                        </button>
                                        <button @click="addToCart(service)" class="px-3.5 py-2 bg-brand-600 hover:bg-brand-700 text-white font-bold text-xs rounded-xl shadow transition flex items-center gap-1 active:scale-95">
                                            <i class="fa-solid fa-plus"></i> Đặt
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>
            </div>

            <!-- TAB 5: ĐƠN HÀNG (ORDERS) -->
            <div x-show="activeCustomerTab === 'orders'" class="space-y-6" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                <div class="bg-white p-6 rounded-2xl border border-slate-100 shadow-sm">
                    <div class="flex items-center justify-between mb-6">
                        <div>
                            <h3 class="text-xl font-bold text-slate-800">Lịch Sử Đơn Hàng & Dịch Vụ Của Bạn</h3>
                            <p class="text-xs text-slate-500">Mọi tương tác trạng thái từ Admin sẽ được đồng bộ tức thì tại đây.</p>
                        </div>
                        <span class="text-xs bg-brand-100 text-brand-800 font-semibold px-3 py-1 rounded-full" x-text="customerOrders.length + ' Đơn hàng'"></span>
                    </div>

                    <template x-if="customerOrders.length === 0">
                        <div class="text-center py-12">
                            <div class="w-16 h-16 bg-slate-100 text-slate-400 rounded-full flex items-center justify-center mx-auto mb-3 text-2xl">
                                <i class="fa-solid fa-box-open"></i>
                            </div>
                            <p class="text-slate-500 font-medium text-sm">Bạn chưa có đơn hàng nào.</p>
                            <button @click="activeCustomerTab = 'shop'" class="mt-3 text-brand-600 text-xs font-bold hover:underline">Khám phá sản phẩm ngay</button>
                        </div>
                    </template>

                    <div class="space-y-4">
                        <template x-for="order in customerOrders" :key="order.id">
                            <div class="border border-slate-200 rounded-2xl p-4 hover:shadow-sm transition">
                                <div class="flex flex-wrap items-center justify-between gap-2 pb-3 border-b border-slate-100 text-xs">
                                    <div>
                                        <span class="font-bold text-slate-800" x-text="'Mã đơn: #' + order.id"></span>
                                        <span class="text-slate-400 ml-2" x-text="order.created || order.createdAt"></span>
                                        <span class="ml-2 px-2 py-0.5 rounded bg-slate-100 text-slate-600 text-[10px]" x-text="'CN: ' + (order.branch || 'Q1')"></span>
                                    </div>
                                    <div class="flex items-center gap-2">
                                        <span class="px-2.5 py-1 rounded-full font-bold text-[10px] uppercase" 
                                            :class="{
                                                'bg-amber-100 text-amber-700': order.status === 'PENDING' || order.status === 'Chờ xác nhận',
                                                'bg-blue-100 text-blue-700': order.status === 'PREPARING' || order.status === 'DELIVERING' || order.status === 'Đang xử lý',
                                                'bg-emerald-100 text-emerald-700': order.status === 'COMPLETED' || order.status === 'Đã hoàn thành',
                                                'bg-rose-100 text-rose-700': order.status === 'CANCELLED' || order.status === 'Đã hủy'
                                            }" 
                                            x-text="formatOrderStatusLabel(order.status)"></span>
                                    </div>
                                </div>

                                <div class="py-3 divide-y divide-slate-100">
                                    <template x-for="item in order.items" :key="item.id || item.name">
                                        <div class="flex items-center justify-between py-2 text-xs">
                                            <div class="flex items-center gap-3">
                                                <img :src="item.image || 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400&auto=format&fit=crop&q=80'" :alt="item.name" class="w-10 h-10 rounded-lg object-cover bg-slate-100">
                                                <div>
                                                    <p class="font-semibold text-slate-800" x-text="item.name"></p>
                                                    <p class="text-slate-400" x-text="formatCurrency(item.price) + ' x ' + (item.quantity || item.qty || 1)"></p>
                                                    <template x-if="item.bookingDate || item.selectedPet">
                                                        <p class="text-[11px] text-brand-600 font-medium">
                                                            <i class="fa-regular fa-calendar-check mr-1"></i>
                                                            <span x-text="item.bookingDate ? 'Lịch: ' + item.bookingDate : ''"></span>
                                                            <span x-text="item.selectedPet ? ' • Pet: ' + item.selectedPet : ''"></span>
                                                        </p>
                                                    </template>
                                                </div>
                                            </div>
                                            <span class="font-bold text-slate-700" x-text="formatCurrency(item.price * (item.quantity || item.qty || 1))"></span>
                                        </div>
                                    </template>
                                </div>

                                <div class="pt-3 border-t border-slate-100 flex flex-wrap items-center justify-between text-xs gap-2">
                                    <div>
                                        <span class="text-slate-500">Thanh toán: </span>
                                        <span class="font-semibold text-slate-700" x-text="order.paymentMethodLabel || order.payment"></span>
                                    </div>
                                    <div class="text-right">
                                        <span class="text-slate-500 mr-2">Tổng tiền:</span>
                                        <span class="text-brand-700 font-extrabold text-sm" x-text="formatCurrency(order.total || order.totalAmount)"></span>
                                    </div>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>
            </div>

            <!-- TAB 6: HỒ SƠ TÀI KHOẢN & QUYỀN LỢI TÍCH ĐIỂM (BỎ Ô TỔNG CHI - YÊU CẦU MỤC 5, 6, 7) -->
            <div x-show="activeCustomerTab === 'profile'" class="space-y-8" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                
                <!-- Personal Information Header Card (ĐÃ BỎ Ô TỔNG CHI) -->
                <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm relative overflow-hidden">
                    <div class="absolute -right-12 -top-12 w-48 h-48 bg-brand-50 rounded-full blur-2xl pointer-events-none"></div>
                    <div class="flex flex-col sm:flex-row items-center sm:items-start justify-between gap-6 relative z-10">
                        <div class="flex flex-col sm:flex-row items-center gap-5 text-center sm:text-left">
                            <div class="relative">
                                <img :src="customerProfile.avatar" :alt="customerProfile.name" class="w-24 h-24 rounded-full object-cover border-4 border-white shadow-md">
                                <span class="absolute bottom-1 right-1 bg-amber-500 text-white text-xs w-6 h-6 rounded-full flex items-center justify-center border-2 border-white shadow">
                                    <i class="fa-solid fa-crown text-[10px]"></i>
                                </span>
                            </div>
                            <div class="space-y-1">
                                <div class="flex items-center justify-center sm:justify-start gap-2">
                                    <h2 class="text-2xl font-extrabold text-slate-800" x-text="customerProfile.name"></h2>
                                    <span class="bg-amber-100 text-amber-800 text-[11px] font-bold px-2.5 py-0.5 rounded-full border border-amber-200" x-text="customerProfile.rank"></span>
                                </div>
                                <p class="text-xs text-slate-500 flex items-center justify-center sm:justify-start gap-3">
                                    <span><i class="fa-solid fa-phone mr-1 text-slate-400"></i><span x-text="customerProfile.phone"></span></span>
                                    <span>•</span>
                                    <span><i class="fa-solid fa-envelope mr-1 text-slate-400"></i><span x-text="customerProfile.email"></span></span>
                                </p>
                                <!-- Reward Points Widget (ĐÃ BỎ Ô TỔNG CHI THEO YÊU CẦU MỤC 5) -->
                                <div class="pt-2 flex items-center justify-center sm:justify-start gap-2">
                                    <div class="bg-gradient-to-r from-amber-500 to-orange-500 text-white font-bold text-xs px-3.5 py-2 rounded-xl shadow-xs flex items-center gap-1.5">
                                        <i class="fa-solid fa-coins text-yellow-200"></i>
                                        <span>Tích điểm: <span x-text="customerProfile.points.toLocaleString('vi-VN') + ' điểm'"></span></span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <button @click="editProfileModalOpen = true" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs px-4 py-2.5 rounded-xl transition flex items-center gap-2 shrink-0">
                            <i class="fa-solid fa-pen-to-square"></i> Chỉnh Sửa Thông Tin
                        </button>
                    </div>
                </div>

                <!-- BẢNG TÍCH ĐIỂM QUYỀN LỢI KHÁCH HÀNG (CÓ NÚT THÔNG TIN CHI TIẾT - YÊU CẦU MỤC 6) -->
                <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                        <div>
                            <h3 class="text-lg font-bold text-slate-800 flex items-center gap-2">
                                <i class="fa-solid fa-award text-amber-500"></i> Bảng Quyền Lợi Thành Viên Theo Mức Tích Điểm
                            </h3>
                            <p class="text-xs text-slate-500">Tích lũy điểm từ mỗi đơn hàng (10.000đ = 1 điểm). Điểm tính lại từ đầu theo chu kỳ mỗi 6 tháng.</p>
                        </div>
                        <!-- Nút Thông Tin Chi Tiết (Yêu cầu mục 6) -->
                        <button @click="loyaltyDetailModalOpen = true" class="bg-amber-50 hover:bg-amber-100 text-amber-800 border border-amber-300 font-bold text-xs px-4 py-2 rounded-xl transition flex items-center gap-1.5 shrink-0 shadow-xs">
                            <i class="fa-solid fa-circle-info text-amber-600"></i> Thông Tin Chi Tiết
                        </button>
                    </div>

                    <div class="overflow-x-auto">
                        <table class="w-full text-left border-collapse text-xs">
                            <thead>
                                <tr class="bg-slate-50 border-b border-slate-200 text-slate-700">
                                    <th class="p-3 font-bold">Hạng Thành Viên</th>
                                    <th class="p-3 font-bold">Mức Điểm Tích Lũy</th>
                                    <th class="p-3 font-bold">Tỷ Lệ Tích Điểm</th>
                                    <th class="p-3 font-bold">Đặc Quyền Cụ Thể</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-100 text-slate-600">
                                <tr class="hover:bg-slate-50/80 transition">
                                    <td class="p-3 font-bold text-amber-700 flex items-center gap-2">
                                        <span class="w-6 h-6 rounded-full bg-amber-100 flex items-center justify-center text-amber-800 font-bold text-[10px]">Cu</span>
                                        Đồng (Bronze)
                                    </td>
                                    <td class="p-3">0 - 499 điểm</td>
                                    <td class="p-3 font-medium">1% giá trị đơn hàng</td>
                                    <td class="p-3">Voucher mừng sinh nhật pet (50.000đ), Miễn phí tư vấn thú y online.</td>
                                </tr>
                                <tr class="hover:bg-slate-50/80 transition">
                                    <td class="p-3 font-bold text-slate-500 flex items-center gap-2">
                                        <span class="w-6 h-6 rounded-full bg-slate-200 flex items-center justify-center text-slate-700 font-bold text-[10px]">Ag</span>
                                        Bạc (Silver)
                                    </td>
                                    <td class="p-3">500 - 999 điểm</td>
                                    <td class="p-3 font-medium">2% giá trị đơn hàng</td>
                                    <td class="p-3">Giảm 5% mọi gói Spa/Grooming, Freeship đơn từ 300k, Quà tặng sinh nhật.</td>
                                </tr>
                                <tr class="hover:bg-slate-50/80 transition bg-amber-50/30">
                                    <td class="p-3 font-bold text-amber-600 flex items-center gap-2">
                                        <span class="w-6 h-6 rounded-full bg-amber-400 text-white flex items-center justify-center font-bold text-[10px]">Au</span>
                                        Vàng (Gold) <span class="text-[9px] bg-amber-500 text-white px-1.5 py-0.2 rounded-full">Hiện tại</span>
                                    </td>
                                    <td class="p-3">1.000 - 2.499 điểm</td>
                                    <td class="p-3 font-medium text-amber-700 font-bold">3% giá trị đơn hàng</td>
                                    <td class="p-3 font-medium text-slate-800">Giảm 10% gói Spa, Ưu tiên đặt lịch khung giờ Vàng, Miễn phí xe đưa đón Pet dưới 5km.</td>
                                </tr>
                                <tr class="hover:bg-slate-50/80 transition">
                                    <td class="p-3 font-bold text-cyan-600 flex items-center gap-2">
                                        <span class="w-6 h-6 rounded-full bg-cyan-100 text-cyan-600 flex items-center justify-center font-bold text-[10px]">Di</span>
                                        Kim Cương (Diamond)
                                    </td>
                                    <td class="p-3">Từ 2.500 điểm trở lên</td>
                                    <td class="p-3 font-medium">5% giá trị đơn hàng</td>
                                    <td class="p-3">Giảm 15% tất cả sản phẩm & dịch vụ, Hotline bác sĩ VIP riêng 24/7, Tặng 1 đêm Khách sạn Pet miễn phí/tháng.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Pet Profiles Management Section (CÓ CHỖ THÊM HÌNH ẢNH - YÊU CẦU MỤC 7) -->
                <div class="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-6">
                    <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
                        <div>
                            <h3 class="text-lg font-bold text-slate-800 flex items-center gap-2">
                                <i class="fa-solid fa-paw text-brand-600"></i> Hồ Sơ Thú Cưng Của Bạn (<span x-text="myPets.length"></span> bé)
                            </h3>
                            <p class="text-xs text-slate-500">Thêm hoặc cập nhật thú cưng tại đây sẽ tự động đồng bộ sang hồ sơ Microchip bên Admin.</p>
                        </div>
                        <button @click="addPetModalOpen = true" class="bg-brand-600 hover:bg-brand-700 text-white text-xs font-bold px-4 py-2.5 rounded-xl shadow-xs transition flex items-center gap-1.5 shrink-0">
                            <i class="fa-solid fa-plus"></i> Thêm Thú Cưng Mới
                        </button>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
                        <template x-for="pet in myPets" :key="pet.id">
                            <div class="border rounded-2xl p-4 transition relative flex flex-col justify-between bg-white shadow-xs hover:border-brand-300"
                                 :class="pet.isDefault ? 'border-brand-500 ring-2 ring-brand-500/10' : 'border-slate-200'">
                                <div>
                                    <div class="flex items-center justify-between mb-3">
                                        <span class="bg-amber-100 text-amber-800 text-[10px] font-extrabold px-2.5 py-0.5 rounded-md uppercase tracking-wider" x-text="pet.species + ' • ' + pet.breed"></span>
                                        <span x-show="pet.isDefault" class="bg-brand-600 text-white text-[10px] font-bold px-2 py-0.5 rounded-full flex items-center gap-1">
                                            <i class="fa-solid fa-check text-[9px]"></i> Mặc định
                                        </span>
                                    </div>

                                    <div class="flex items-center gap-4 mb-3">
                                        <img :src="pet.image" :alt="pet.name" class="w-16 h-16 rounded-2xl object-cover bg-slate-100 border border-slate-100 shrink-0 shadow-xs">
                                        <div>
                                            <h4 class="font-extrabold text-slate-800 text-lg leading-tight" x-text="pet.name"></h4>
                                            <p class="text-xs text-slate-500 mt-1" x-text="pet.age + ' • ' + pet.weight + ' kg'"></p>
                                            <p class="text-[10px] text-teal-600 font-mono mt-0.5" x-text="'Chip: ' + (pet.chip || 'Chờ gắn')"></p>
                                        </div>
                                    </div>

                                    <div class="bg-slate-50 p-2.5 rounded-xl text-xs text-slate-600 mb-4 border border-slate-100">
                                        <span class="font-bold text-slate-700">Tình trạng:</span> <span x-text="pet.health"></span>
                                    </div>
                                </div>

                                <div class="pt-2 border-t border-slate-100 flex items-center justify-between">
                                    <button x-show="!pet.isDefault" @click="setDefaultPet(pet.id)" class="text-xs text-brand-600 hover:text-brand-800 font-bold">
                                        Đặt làm mặc định
                                    </button>
                                    <span x-show="pet.isDefault" class="text-[11px] text-slate-400 font-medium">Bé đang chọn</span>

                                    <button @click="deletePet(pet.id)" class="text-xs text-slate-300 hover:text-rose-500 p-1">
                                        <i class="fa-solid fa-trash-can"></i>
                                    </button>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>

                <!-- Address Book Section -->
                <div class="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-6">
                    <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
                        <div>
                            <h3 class="text-lg font-bold text-slate-800 flex items-center gap-2">
                                <i class="fa-solid fa-location-dot text-brand-600"></i> Sổ Địa Chỉ Giao Hàng & Nhận Thú Cưng
                            </h3>
                            <p class="text-xs text-slate-500">Lưu địa chỉ giúp giao sản phẩm và dịch vụ đón tận nơi nhanh chóng hơn.</p>
                        </div>
                        <button @click="addAddressModalOpen = true" class="bg-slate-800 hover:bg-slate-900 text-white text-xs font-bold px-4 py-2.5 rounded-xl shadow-xs transition flex items-center gap-1.5 shrink-0">
                            <i class="fa-solid fa-plus"></i> Thêm Địa Chỉ Mới
                        </button>
                    </div>

                    <div class="space-y-3">
                        <template x-for="addr in addresses" :key="addr.id">
                            <div class="p-4 rounded-2xl border flex flex-col sm:flex-row sm:items-center justify-between gap-3 transition"
                                 :class="addr.isDefault ? 'border-brand-500 bg-brand-50/30' : 'border-slate-200 bg-white'">
                                <div class="flex items-start gap-3">
                                    <div class="w-9 h-9 rounded-xl bg-slate-100 text-slate-600 flex items-center justify-center text-sm shrink-0 mt-0.5">
                                        <i class="fa-solid fa-house-chimney"></i>
                                    </div>
                                    <div>
                                        <div class="flex items-center gap-2">
                                            <span class="font-bold text-slate-800 text-sm" x-text="addr.label"></span>
                                            <span x-show="addr.isDefault" class="bg-brand-600 text-white text-[10px] font-bold px-2 py-0.2 rounded-md">Mặc định</span>
                                        </div>
                                        <p class="text-xs text-slate-600 mt-0.5" x-text="addr.fullAddress"></p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-3 justify-end">
                                    <button x-show="!addr.isDefault" @click="setDefaultAddress(addr.id)" class="text-xs text-brand-600 hover:underline font-semibold">
                                        Đặt mặc định
                                    </button>
                                    <button @click="deleteAddress(addr.id)" class="text-xs text-slate-300 hover:text-rose-500 p-1">
                                        <i class="fa-solid fa-trash-can"></i>
                                    </button>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>
            </div>

            <!-- FAQ ACCORDION SECTION (5 CÂU HỎI CHI TIẾT ĐẦY ĐỦ - YÊU CẦU MỤC 11) -->
            <div class="mt-12 bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-6">
                <div class="text-center max-w-xl mx-auto space-y-2">
                    <span class="bg-brand-100 text-brand-800 text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider">Hỗ trợ khách hàng</span>
                    <h3 class="text-2xl font-extrabold text-slate-800">Các Câu Hỏi Thường Gặp (FAQ - 5 Chủ Đề Quan Trọng)</h3>
                    <p class="text-xs text-slate-500">Mọi thông tin thắc mắc về quy trình dịch vụ, giao hàng và hỗ trợ chăm sóc thú cưng được giải đáp chi tiết nhất.</p>
                </div>

                <div class="max-w-3xl mx-auto divide-y divide-slate-200">
                    <template x-for="(faq, index) in faqList" :key="index">
                        <div class="py-4">
                            <button @click="faqActive = faqActive === index ? null : index" class="w-full flex justify-between items-center text-left focus:outline-none group">
                                <span class="font-bold text-slate-800 text-sm sm:text-base group-hover:text-brand-600 transition" x-text="faq.question"></span>
                                <div class="w-7 h-7 rounded-full bg-slate-100 group-hover:bg-brand-100 text-slate-500 group-hover:text-brand-700 flex items-center justify-center transition shrink-0 ml-2">
                                    <i class="fa-solid text-xs" :class="faqActive === index ? 'fa-minus' : 'fa-plus'"></i>
                                </div>
                            </button>
                            <div x-show="faqActive === index" 
                                 x-transition:enter="transition ease-out duration-200"
                                 x-transition:enter-start="opacity-0 -translate-y-1"
                                 x-transition:enter-end="opacity-100 translate-y-0"
                                 class="mt-3 text-xs sm:text-sm text-slate-600 leading-relaxed bg-slate-50 p-4 rounded-2xl border border-slate-100" 
                                 x-html="faq.answer">
                            </div>
                        </div>
                    </template>
                </div>
            </div>
        </main>

        <!-- FOOTER SECTION CUSTOMER (ĐÃ ĐỔI CÂU THEO YÊU CẦU MỤC 13) -->
        <footer class="bg-slate-900 text-white mt-12 pt-12 pb-20 md:pb-12 border-t border-slate-800">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-5 gap-8">
                <div class="space-y-3 md:col-span-2">
                    <div class="flex items-center gap-2">
                        <div class="w-8 h-8 rounded-xl bg-brand-500 flex items-center justify-center text-white">
                            <i class="fa-solid fa-paw"></i>
                        </div>
                        <span class="text-lg font-bold">PetCare360</span>
                    </div>
                    <!-- Câu mới ở Footer theo yêu cầu mục 13 -->
                    <p class="text-xs text-slate-300 max-w-sm leading-relaxed">PetCare360 - Điểm tựa yêu thương & hệ sinh thái chăm sóc y tế, dinh dưỡng trọn đời cho thú cưng. Cam kết y đức thú y chuẩn mực, tận tâm như người thân trong gia đình.</p>
                    <div class="pt-2 text-xs text-slate-400 space-y-1">
                        <p><i class="fa-solid fa-phone mr-1.5 text-brand-400"></i> Hotline Cấp Cứu 24/7: 1900 6888 (Phím 1)</p>
                        <p><i class="fa-solid fa-envelope mr-1.5 text-brand-400"></i> Email CSKH: cskh@petcare360.vn</p>
                        <p><i class="fa-solid fa-location-dot mr-1.5 text-brand-400"></i> Trụ sở chính: 123 Nguyễn Thị Minh Khai, P.6, Q.3, TP.HCM</p>
                    </div>
                </div>

                <div>
                    <h4 class="font-bold text-sm text-slate-200 mb-3">Dịch Vụ Nổi Bật</h4>
                    <ul class="space-y-2 text-xs text-slate-400">
                        <li><a href="#" @click.prevent="activeCustomerTab = 'booking'" class="hover:text-brand-400 transition">Grooming & Spa Thú Cưng</a></li>
                        <li><a href="#" @click.prevent="activeCustomerTab = 'booking'" class="hover:text-brand-400 transition">Khám Thú Y & Tiêm Ngừa</a></li>
                        <li><a href="#" @click.prevent="activeCustomerTab = 'booking'" class="hover:text-brand-400 transition">Khách Sạn Thú Cưng 5 Sao</a></li>
                        <li><a href="#" @click.prevent="activeCustomerTab = 'shop'" class="hover:text-brand-400 transition">Sản Phẩm & Dinh Dưỡng</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="font-bold text-sm text-slate-200 mb-3">Chính Sách & Pháp Lý</h4>
                    <ul class="space-y-2 text-xs text-slate-400">
                        <li><button @click="openPolicyModal('privacy')" class="hover:text-brand-400 transition text-left">Chính sách Bảo mật</button></li>
                        <li><button @click="openPolicyModal('terms')" class="hover:text-brand-400 transition text-left">Điều khoản Dịch vụ</button></li>
                        <li><button @click="openPolicyModal('cookie')" class="hover:text-brand-400 transition text-left">Chính sách Cookie</button></li>
                        <li><button @click="openPolicyModal('community')" class="hover:text-brand-400 transition text-left">Nguyên tắc cộng đồng</button></li>
                        <li><button @click="openPolicyModal('refund')" class="hover:text-brand-400 transition text-left">Chính sách hoàn tiền</button></li>
                    </ul>
                </div>

                <div>
                    <h4 class="font-bold text-sm text-slate-200 mb-3">Thanh Toán An Toàn</h4>
                    <div class="flex gap-3 text-xl text-slate-400">
                        <i class="fa-solid fa-money-bill-wave hover:text-emerald-400 transition" title="Tiền mặt COD"></i>
                        <i class="fa-solid fa-building-columns hover:text-blue-400 transition" title="VietQR Banking"></i>
                        <i class="fa-solid fa-wallet hover:text-pink-400 transition" title="Ví MoMo"></i>
                    </div>
                    <p class="text-[11px] text-slate-500 mt-4">© 2026 PetCare360 Corporation. All rights reserved.</p>
                </div>
            </div>
        </footer>

        <!-- Mobile Bottom Navigation Bar Customer -->
        <div class="md:hidden fixed bottom-0 left-0 right-0 bg-white border-t border-slate-200 z-30 px-2 py-1.5 flex justify-around items-center text-[10px]">
            <button @click="activeCustomerTab = 'home'" :class="activeCustomerTab === 'home' ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1">
                <i class="fa-solid fa-house text-base mb-0.5"></i>
                <span>Trang chủ</span>
            </button>
            <button @click="activeCustomerTab = 'petshare'" :class="activeCustomerTab === 'petshare' ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1">
                <i class="fa-solid fa-newspaper text-base mb-0.5"></i>
                <span>PetShare</span>
            </button>
            <button @click="activeCustomerTab = 'shop'" :class="activeCustomerTab === 'shop' ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1">
                <i class="fa-solid fa-box-open text-base mb-0.5"></i>
                <span>Sản phẩm</span>
            </button>
            <button @click="activeCustomerTab = 'booking'" :class="activeCustomerTab === 'booking' ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1">
                <i class="fa-solid fa-scissors text-base mb-0.5"></i>
                <span>Dịch vụ</span>
            </button>
            <button @click="activeCustomerTab = 'orders'" :class="activeCustomerTab === 'orders' ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1 relative">
                <i class="fa-solid fa-receipt text-base mb-0.5"></i>
                <span>Đơn hàng</span>
                <span x-show="customerOrders.length > 0" class="absolute top-0 right-1 w-2 h-2 bg-amber-500 rounded-full"></span>
            </button>
            <button @click="activeCustomerTab = 'profile'" :class="activeCustomerTab === 'profile' ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1">
                <i class="fa-solid fa-user-gear text-base mb-0.5"></i>
                <span>Tài khoản</span>
            </button>
        </div>
    </div>
"""
