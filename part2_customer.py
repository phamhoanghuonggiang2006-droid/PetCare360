# -*- coding: utf-8 -*-
CUSTOMER_HTML = """
    <!-- ======================================================== -->
    <!-- VIEW 1: GIAO DIỆN KHÁCH HÀNG (CUSTOMER VIEW - MẶC ĐỊNH) -->
    <!-- ======================================================== -->
    <div x-show="currentRole === 'customer'" class="min-h-screen flex flex-col pb-16 md:pb-0" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 scale-98" x-transition:enter-end="opacity-100 scale-100">
        
        <!-- Header Navigation Customer -->
        <header class="sticky top-0 z-30 bg-white/95 backdrop-blur border-b border-slate-200 shadow-sm">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex items-center justify-between h-16 lg:h-20 gap-4">
                    
                    <!-- Brand Logo -->
                    <div class="flex items-center gap-3 cursor-pointer select-none" @click="activeCustomerTab = 'home'">
                        <div class="w-10 h-10 lg:w-11 lg:h-11 rounded-2xl bg-gradient-to-tr from-brand-600 to-teal-500 flex items-center justify-center text-white shadow-md shadow-brand-500/20 transform hover:scale-105 transition">
                            <i class="fa-solid fa-paw text-xl"></i>
                        </div>
                        <div>
                            <span class="text-xl lg:text-2xl font-black tracking-tight text-slate-800 leading-none block">PetCare<span class="text-brand-600">360</span></span>
                            <span class="text-[10px] text-slate-400 font-semibold tracking-wider uppercase block mt-0.5">Hệ sinh thái thú cưng 5 sao</span>
                        </div>
                    </div>

                    <!-- Thanh tìm kiếm sản phẩm lớn (Yêu cầu Header Shop PetCare360) -->
                    <div class="hidden lg:flex flex-1 max-w-xs xl:max-w-md mx-3 relative">
                        <div class="relative w-full">
                            <input type="text" x-model="searchQuery" @focus="if(activeCustomerTab !== 'shop') { activeCustomerTab = 'shop'; shopViewMode = 'catalog'; }" @keydown.enter="activeCustomerTab = 'shop'; shopViewMode = 'catalog'; scrollToCatalogGrid();" placeholder="Tìm kiếm hạt, pate, cát vệ sinh, phụ kiện..." class="w-full bg-slate-100 hover:bg-slate-50 focus:bg-white border border-slate-200 focus:border-orange-500 rounded-2xl pl-10 pr-9 py-2 text-xs text-slate-800 transition focus:outline-none focus:ring-2 focus:ring-orange-200 shadow-inner">
                            <i class="fa-solid fa-magnifying-glass absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 text-sm"></i>
                            <button x-show="searchQuery" @click="searchQuery = ''" class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 text-xs">
                                <i class="fa-solid fa-circle-xmark"></i>
                            </button>
                        </div>
                    </div>

                    <!-- Navigation Links Customer -->
                    <nav class="hidden md:flex items-center gap-1 lg:gap-2">
                        <button @click="activeCustomerTab = 'home'" :class="activeCustomerTab === 'home' ? 'text-brand-700 bg-brand-50 font-bold' : 'text-slate-600 hover:text-brand-600 hover:bg-slate-50'" class="px-3 py-2 rounded-xl text-xs lg:text-sm transition flex items-center gap-1.5">
                            <i class="fa-solid fa-house"></i>Trang Chủ
                        </button>
                        <button @click="activeCustomerTab = 'shop'; shopViewMode = 'catalog';" :class="activeCustomerTab === 'shop' ? 'text-brand-700 bg-brand-50 font-bold' : 'text-slate-600 hover:text-brand-600 hover:bg-slate-50'" class="px-3 py-2 rounded-xl text-xs lg:text-sm transition flex items-center gap-1.5">
                            <i class="fa-solid fa-box-open"></i>Sản Phẩm
                        </button>
                        <button @click="activeCustomerTab = 'booking'; syncPetBookingDetails(serviceBookingForm.petId)" :class="activeCustomerTab === 'booking' ? 'text-brand-700 bg-brand-50 font-bold' : 'text-slate-600 hover:text-brand-600 hover:bg-slate-50'" class="px-3 py-2 rounded-xl text-xs lg:text-sm transition flex items-center gap-1.5">
                            <i class="fa-solid fa-scissors"></i>Dịch Vụ
                        </button>
                        <button @click="activeCustomerTab = 'petshare'" :class="activeCustomerTab === 'petshare' ? 'text-brand-700 bg-brand-50 font-bold' : 'text-slate-600 hover:text-brand-600 hover:bg-slate-50'" class="px-3 py-2 rounded-xl text-xs lg:text-sm transition flex items-center gap-1.5 relative">
                            <i class="fa-solid fa-newspaper"></i>PetShare360
                            <span class="text-[9px] bg-rose-500 text-white font-bold px-1.5 py-0.2 rounded-full">Hot</span>
                        </button>
                        <button @click="activeCustomerTab = 'petshow'" :class="activeCustomerTab === 'petshow' ? 'text-brand-700 bg-brand-50 font-bold' : 'text-slate-600 hover:text-brand-600 hover:bg-slate-50'" class="px-3 py-2 rounded-xl text-xs lg:text-sm transition flex items-center gap-1.5 relative">
                            <i class="fa-solid fa-video text-rose-500 animate-pulse"></i>PetShow360
                            <span class="text-[9px] bg-rose-600 text-white font-extrabold px-1.5 py-0.2 rounded-full uppercase tracking-tighter">Live</span>
                        </button>
                        <button @click="activeCustomerTab = 'orders'" :class="activeCustomerTab === 'orders' ? 'text-brand-700 bg-brand-50 font-bold' : 'text-slate-600 hover:text-brand-600 hover:bg-slate-50'" class="px-3 py-2 rounded-xl text-xs lg:text-sm transition flex items-center gap-1.5 relative">
                            <i class="fa-solid fa-receipt"></i>Đơn Hàng
                            <span class="ml-1 px-1.5 py-0.2 text-[10px] bg-amber-500 text-white font-bold rounded-full" x-text="customerOrdersEnhanced.length"></span>
                        </button>
                        <!-- Khối Menu Tài Khoản: Chỉ hiển thị khi đã đăng nhập (Auth state), Khách (guest) sẽ ẩn -->
                        <template x-if="isAuth">
                            <button @click="activeCustomerTab = 'account'" :class="(activeCustomerTab === 'account' || activeCustomerTab === 'profile') ? 'text-brand-700 bg-brand-50 font-bold' : 'text-slate-600 hover:text-brand-600 hover:bg-slate-50'" class="px-3 py-2 rounded-xl text-xs lg:text-sm transition flex items-center gap-1.5">
                                <i class="fa-solid fa-user-gear"></i>Tài Khoản
                            </button>
                        </template>
                    </nav>

                    <!-- Actions: Chat CSKH, PetShare Notifications, Cart & Account -->
                    <div class="flex items-center gap-2 sm:gap-3">
                        <!-- Nút Chat CSKH trực tiếp -->
                        <button @click="openCustomerSupportChat()" class="relative p-2.5 rounded-xl text-slate-700 hover:text-brand-600 hover:bg-brand-50 transition border border-slate-200 flex items-center gap-1.5 group" title="Chat hỗ trợ CSKH 24/7">
                            <i class="fa-solid fa-headset text-base text-brand-600 group-hover:scale-110 transition"></i>
                            <span class="hidden xl:inline text-xs font-bold text-slate-700">Chat CSKH</span>
                            <span class="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                        </button>

                        <!-- Icon Chuông Thông Báo: Chỉ hiển thị khi đã đăng nhập (Guest sẽ ẩn hoàn toàn thông báo) -->
                        <template x-if="isAuth">
                            <div class="relative" x-data="{ openNotice: false }" @click.outside="openNotice = false">
                            <button @click="openNotice = !openNotice" class="relative p-2.5 rounded-xl text-slate-700 hover:text-brand-600 hover:bg-brand-50 transition border border-slate-200" title="Thông báo mạng xã hội PetShare360">
                                <i class="fa-solid fa-bell text-base"></i>
                                <span class="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-rose-500 text-white font-extrabold text-[9px] flex items-center justify-center border-2 border-white animate-bounce">3</span>
                            </button>
                            <!-- Popover Danh Sách Tương Tác Mới -->
                            <div x-show="openNotice" x-cloak class="absolute right-0 mt-2 w-80 sm:w-96 bg-white rounded-2xl shadow-2xl border border-slate-100 p-3 z-50 animate-fadeIn">
                                <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-100">
                                    <div class="flex items-center gap-2">
                                        <i class="fa-solid fa-bell text-brand-600 text-sm"></i>
                                        <span class="font-bold text-xs text-slate-800">Thông báo PetShare360</span>
                                    </div>
                                    <span class="text-[10px] text-brand-600 hover:underline cursor-pointer font-semibold">Đánh dấu đã đọc</span>
                                </div>
                                <div class="space-y-2 max-h-72 overflow-y-auto">
                                    <div class="p-2 rounded-xl hover:bg-slate-50 transition flex items-start gap-2.5 cursor-pointer">
                                        <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=100&q=80" class="w-8 h-8 rounded-full object-cover mt-0.5">
                                        <div class="flex-1 text-xs">
                                            <p class="text-slate-800 font-semibold"><span class="font-bold">Lan Hương</span> đã thích bài viết về bé Corgi của bạn.</p>
                                            <span class="text-[10px] text-slate-400">5 phút trước</span>
                                        </div>
                                    </div>
                                    <div class="p-2 rounded-xl hover:bg-slate-50 transition flex items-start gap-2.5 cursor-pointer">
                                        <img src="https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=100&q=80" class="w-8 h-8 rounded-full object-cover mt-0.5">
                                        <div class="flex-1 text-xs">
                                            <p class="text-slate-800 font-semibold"><span class="font-bold">BS. Minh Hoàng</span> đã bình luận: "Bé tăng cân rất chuẩn, tiếp tục duy trì nhé!".</p>
                                            <span class="text-[10px] text-slate-400">20 phút trước</span>
                                        </div>
                                    </div>
                                    <div class="p-2 rounded-xl hover:bg-slate-50 transition flex items-start gap-2.5 cursor-pointer">
                                        <div class="w-8 h-8 rounded-full bg-amber-100 text-amber-700 flex items-center justify-center font-bold text-xs mt-0.5">
                                            <i class="fa-solid fa-fire"></i>
                                        </div>
                                        <div class="flex-1 text-xs">
                                            <p class="text-slate-800 font-semibold">Chúc mừng! Bạn đã đạt chuỗi <span class="text-amber-600 font-bold">12 ngày streak</span> chăm sóc bé cưng.</p>
                                            <span class="text-[10px] text-slate-400">1 giờ trước</span>
                                        </div>
                                    </div>
                                </div>
                                <div class="pt-2 text-center border-t border-slate-100">
                                    <button @click="activeCustomerTab = 'petshare'; openNotice = false;" class="text-xs text-brand-600 font-bold hover:underline">Vào cộng đồng PetShare360</button>
                                </div>
                            </div>
                        </div>
                        </template>

                        <!-- Nút Giỏ hàng 5 Bước -->
                        <button @click="activeCustomerTab = 'cart'; cartStep = 1;" class="relative p-2.5 rounded-xl text-slate-700 hover:text-brand-600 hover:bg-brand-50 transition border border-slate-200" title="Giỏ hàng của bạn">
                            <i class="fa-solid fa-cart-shopping text-base"></i>
                            <span x-show="cartItemsCount > 0" x-text="cartItemsCount" class="absolute -top-1.5 -right-1.5 bg-orange-500 text-white font-bold text-[10px] w-5 h-5 rounded-full flex items-center justify-center shadow-sm animate-pulse"></span>
                        </button>

                        <!-- Khối Tài Khoản: Nếu chưa đăng nhập hiện Đăng nhập, nếu đã đăng nhập hiện thông tin và nút Đăng xuất -->
                        <div class="pl-2 border-l border-slate-200">
                            <template x-if="!isAuth">
                                <button @click="openLoginModal()" class="flex items-center gap-2 bg-gradient-to-r from-brand-600 to-teal-500 hover:from-brand-700 hover:to-teal-600 text-white font-bold text-xs sm:text-sm px-3.5 py-2 rounded-xl shadow-md transition transform active:scale-95">
                                    <i class="fa-solid fa-right-to-bracket text-xs"></i>
                                    <span>Đăng nhập</span>
                                </button>
                            </template>

                            <template x-if="isAuth">
                                <div class="flex items-center gap-2">
                                    <div @click="activeCustomerTab = 'account'" class="flex items-center gap-2 cursor-pointer hover:opacity-85 transition" title="Quản lý thông tin tài khoản">
                                        <img :src="customerProfile.avatar" :alt="customerProfile.name" class="w-9 h-9 rounded-full object-cover border-2 border-brand-500 shadow-sm">
                                        <div class="hidden lg:block text-left">
                                            <p class="text-xs font-bold text-slate-800 leading-none truncate max-w-[110px]" x-text="customerProfile.name"></p>
                                            <p class="text-[10px] text-brand-600 font-medium" x-text="customerProfile.rank"></p>
                                        </div>
                                    </div>
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

            <!-- ======================================================== -->
            <!-- TAB 1: TRANG CHỦ (HOME) -->
            <!-- ======================================================== -->
            <div x-show="activeCustomerTab === 'home'" class="space-y-8" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                
                <!-- Banner Announcement -->
                <div class="bg-gradient-to-r from-brand-600 via-teal-600 to-emerald-600 rounded-3xl p-6 sm:p-8 text-white shadow-xl relative overflow-hidden">
                    <div class="absolute -right-10 -bottom-10 opacity-20 text-9xl pointer-events-none">
                        <i class="fa-solid fa-bone"></i>
                    </div>
                    <div class="relative z-10 max-w-2xl">
                        <div class="flex items-center gap-2 mb-3">
                            <span class="bg-amber-400 text-slate-900 text-xs font-extrabold px-3 py-1 rounded-full uppercase tracking-wider inline-block">Ưu đãi tuần lễ Pet Care</span>
                            <span class="bg-white/20 text-white text-xs font-semibold px-2.5 py-0.5 rounded-full">Tiêu chuẩn 5 Sao</span>
                        </div>
                        <h1 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold mb-3 leading-tight">Chăm sóc toàn diện cho bé cưng của bạn</h1>
                        <p class="text-brand-100 text-sm sm:text-base mb-6 leading-relaxed">Hệ sinh thái thông minh tích hợp Sản phẩm dinh dưỡng chính hãng, Spa & Khách sạn thú cưng 5 sao, cùng giám sát Camera Live trực tuyến 24/7.</p>
                        <div class="flex flex-wrap gap-3">
                            <button @click="activeCustomerTab = 'shop'" class="bg-white text-brand-700 hover:bg-brand-50 text-xs sm:text-sm font-bold px-5 py-3 rounded-xl transition shadow-md flex items-center gap-2">
                                <i class="fa-solid fa-bag-shopping"></i>Khám Phá Sản Phẩm
                            </button>
                            <button @click="activeCustomerTab = 'booking'" class="bg-orange-500 hover:bg-orange-600 text-white text-xs sm:text-sm font-bold px-5 py-3 rounded-xl transition shadow-md flex items-center gap-2">
                                <i class="fa-solid fa-calendar-check"></i>Đặt Lịch Dịch Vụ 5 Sao
                            </button>
                            <button @click="activeCustomerTab = 'petshow'" class="bg-slate-900/60 hover:bg-slate-900 text-white text-xs sm:text-sm font-bold px-5 py-3 rounded-xl transition shadow-md flex items-center gap-2 border border-white/20">
                                <i class="fa-solid fa-video text-rose-400"></i>Xem Camera PetShow360
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Quick Services Categories Grid -->
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
                    <div @click="activeCustomerTab = 'shop'" class="bg-white p-5 rounded-2xl shadow-sm border border-slate-100 hover:border-brand-300 hover:shadow-md transition cursor-pointer text-center group">
                        <div class="w-12 h-12 mx-auto rounded-2xl bg-brand-50 text-brand-600 flex items-center justify-center text-xl mb-3 group-hover:scale-110 transition">
                            <i class="fa-solid fa-bowl-food"></i>
                        </div>
                        <h3 class="font-bold text-sm text-slate-800">Thức Ăn & Hạt</h3>
                        <p class="text-[11px] text-slate-400 mt-1">Dinh dưỡng nhập khẩu 100%</p>
                    </div>
                    <div @click="activeCustomerTab = 'booking'; servicePricingTab = 'grooming'; syncPetBookingDetails(serviceBookingForm.petId)" class="bg-white p-5 rounded-2xl shadow-sm border border-slate-100 hover:border-brand-300 hover:shadow-md transition cursor-pointer text-center group">
                        <div class="w-12 h-12 mx-auto rounded-2xl bg-amber-50 text-amber-600 flex items-center justify-center text-xl mb-3 group-hover:scale-110 transition">
                            <i class="fa-solid fa-scissors"></i>
                        </div>
                        <h3 class="font-bold text-sm text-slate-800">Grooming & Spa</h3>
                        <p class="text-[11px] text-slate-400 mt-1">Quy trình 7 bước thư giãn</p>
                    </div>
                    <div @click="activeCustomerTab = 'booking'; servicePricingTab = 'hotel'; syncPetBookingDetails(serviceBookingForm.petId)" class="bg-white p-5 rounded-2xl shadow-sm border border-slate-100 hover:border-brand-300 hover:shadow-md transition cursor-pointer text-center group">
                        <div class="w-12 h-12 mx-auto rounded-2xl bg-rose-50 text-rose-600 flex items-center justify-center text-xl mb-3 group-hover:scale-110 transition">
                            <i class="fa-solid fa-hotel"></i>
                        </div>
                        <h3 class="font-bold text-sm text-slate-800">Pet Hotel 5 Sao</h3>
                        <p class="text-[11px] text-slate-400 mt-1">Phòng điều hòa + Camera 24/7</p>
                    </div>
                    <div @click="activeCustomerTab = 'petshare'" class="bg-white p-5 rounded-2xl shadow-sm border border-slate-100 hover:border-brand-300 hover:shadow-md transition cursor-pointer text-center group">
                        <div class="w-12 h-12 mx-auto rounded-2xl bg-teal-50 text-teal-600 flex items-center justify-center text-xl mb-3 group-hover:scale-110 transition">
                            <i class="fa-solid fa-users"></i>
                        </div>
                        <h3 class="font-bold text-sm text-slate-800">PetShare Cộng Đồng</h3>
                        <p class="text-[11px] text-slate-400 mt-1">Kinh nghiệm & Bác sĩ tư vấn</p>
                    </div>
                </div>

                <!-- ======================================================== -->
                <!-- SECTION: SẢN PHẨM BÁN CHẠY (HORIZONTAL CAROUSEL / SLIDER - 4 CARDS TRÊN 1 VIEWPORT) -->
                <!-- ======================================================== -->
                <div class="space-y-4">
                    <div class="flex items-center justify-between">
                        <div>
                            <div class="flex items-center gap-2">
                                <span class="bg-orange-100 text-orange-700 text-xs font-bold px-2.5 py-0.5 rounded-full uppercase tracking-wider flex items-center gap-1">
                                    <i class="fa-solid fa-fire text-orange-500"></i> Bán Chạy Nhất
                                </span>
                                <span class="text-xs text-slate-400 font-medium">Top sản phẩm được Boss & Sen tin dùng</span>
                            </div>
                            <h2 class="text-xl sm:text-2xl font-black text-slate-800 tracking-tight mt-1">Sản Phẩm Bán Chạy</h2>
                        </div>
                        <!-- Điều hướng: Nút Xem tất cả + Nút mũi tên nhỏ gọn (Arrow Button) ở mép phải của section -->
                        <div class="flex items-center gap-2">
                            <button @click="activeCustomerTab = 'shop'; shopFilterCategory = 'all'; backToShopCatalog();" class="text-xs font-bold text-[#F97316] hover:underline mr-1 hidden sm:inline-flex items-center gap-1">
                                Xem tất cả 12 sản phẩm <i class="fa-solid fa-angle-right text-[11px]"></i>
                            </button>
                            <div class="flex items-center gap-1.5">
                                <button @click="scrollBestSellerLeft()" class="w-8 h-8 rounded-full border border-slate-200 bg-white hover:bg-orange-50 text-slate-600 hover:text-orange-600 shadow-sm flex items-center justify-center transition active:scale-90" title="Lướt sang trái">
                                    <i class="fa-solid fa-chevron-left text-xs"></i>
                                </button>
                                <button @click="scrollBestSellerRight()" class="w-8 h-8 rounded-full border border-slate-200 bg-white hover:bg-orange-50 text-slate-600 hover:text-orange-600 shadow-sm flex items-center justify-center transition active:scale-90" title="Lướt xem các sản phẩm tiếp theo">
                                    <i class="fa-solid fa-chevron-right text-xs"></i>
                                </button>
                            </div>
                        </div>
                    </div>

                    <!-- Product Carousel / Slider: Đúng 4 thẻ sản phẩm trên cùng 1 viewport ngang (desktop), vuốt trượt ngang mượt mà -->
                    <div id="homepage-bestseller-carousel" class="flex gap-4 overflow-x-auto scroll-smooth snap-x pb-3 pt-1 no-scrollbar hide-scrollbar">
                        <template x-for="prod in bestSellingProducts" :key="'best-' + prod.id">
                            <div @click="activeCustomerTab = 'shop'; openProductDetailPage(prod);" class="snap-start flex-shrink-0 w-[260px] sm:w-[calc(50%-8px)] md:w-[calc(33.333%-11px)] lg:w-[calc(25%-12px)] bg-white rounded-2xl p-3 border border-slate-200 shadow-sm hover:shadow-lg transition-all duration-200 flex flex-col justify-between group cursor-pointer relative overflow-hidden">
                                
                                <!-- Ảnh sản phẩm thumbnail tỷ lệ chuẩn 1:1 + Badge giảm giá & Giao nhanh 2h -->
                                <div class="relative w-full aspect-square rounded-xl overflow-hidden bg-slate-50 flex items-center justify-center p-2">
                                    <img :src="prod.image || prod.img" :alt="prod.name" class="w-full h-full object-contain group-hover:scale-105 transition-transform duration-300">
                                    <span class="absolute top-2 left-2 bg-rose-600 text-white font-extrabold text-[10px] px-2 py-0.5 rounded-md shadow-sm" x-text="prod.discountPercent || '-20%'"></span>
                                    <template x-if="prod.expressShip">
                                        <span class="absolute top-2 right-2 bg-amber-400 text-slate-900 font-black text-[9px] px-1.5 py-0.5 rounded-md shadow-sm flex items-center gap-0.5">
                                            <i class="fa-solid fa-bolt text-[8px]"></i> 2H
                                        </span>
                                    </template>
                                </div>

                                <!-- Chi tiết thẻ chuẩn: Tên sản phẩm (tối đa 2 dòng), Số sao & Đã bán, Giá bán nổi bật kèm giá gốc gạch ngang, Nút Thêm vào giỏ -->
                                <div class="pt-3 pb-1 space-y-1.5 flex-1 flex flex-col justify-between">
                                    <div>
                                        <p class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider truncate" x-text="prod.brand || prod.category"></p>
                                        <h4 class="text-xs sm:text-sm font-bold text-[#1E293B] line-clamp-2 leading-snug group-hover:text-[#F97316] transition" x-text="prod.name" :title="prod.name"></h4>
                                    </div>

                                    <div>
                                        <!-- Số sao đánh giá và lượt mua -->
                                        <div class="flex items-center gap-1.5 text-xs text-slate-500 pt-1">
                                            <div class="flex items-center text-amber-400 text-xs">
                                                <i class="fa-solid fa-star"></i>
                                                <span class="font-bold text-slate-800 ml-1" x-text="prod.rating || 5.0"></span>
                                            </div>
                                            <span class="text-slate-300">•</span>
                                            <span class="text-[11px] text-slate-400" x-text="(prod.sold || 128) + ' đã bán'"></span>
                                        </div>

                                        <!-- Giá bán nổi bật kèm giá gốc bị gạch ngang + Nút Thêm vào giỏ -->
                                        <div class="pt-2 flex items-center justify-between border-t border-slate-100 mt-2">
                                            <div>
                                                <div class="text-sm sm:text-base font-extrabold text-[#F97316]" x-text="formatCurrency(prod.price)"></div>
                                                <div class="text-[10px] text-slate-400 line-through font-medium" x-text="formatCurrency(prod.originalPrice || Math.round(prod.price * 1.25))"></div>
                                            </div>
                                            <button @click.stop="addToCart({ id: prod.id, name: prod.name, price: prod.price, image: prod.image || prod.img, weight: '3kg', flavor: 'Vị chuẩn' })" class="w-9 h-9 rounded-full bg-orange-50 text-[#F97316] hover:bg-[#F97316] hover:text-white transition flex items-center justify-center shadow-sm transform active:scale-90" title="Thêm vào giỏ hàng">
                                                <i class="fa-solid fa-cart-plus text-xs"></i>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>
            </div>

            <!-- ======================================================== -->
            <!-- TAB 2: SẢN PHẨM (CHUẨN E-COMMERCE CHUYÊN NGHIỆP THEO YÊU CẦU) -->
            <!-- ======================================================== -->
            <div x-show="activeCustomerTab === 'shop'" class="space-y-8" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                
                <!-- ======================================================== -->
                <!-- CHẾ ĐỘ 1: GIAO DIỆN SHOP - TRANG DANH SÁCH SẢN PHẨM (SHOP CATALOG PAGE) -->
                <!-- ======================================================== -->
                <div x-show="shopViewMode === 'catalog'" class="space-y-8 animate-fadeIn">
                    
                    <!-- BANNER KHUYẾN MÃI NGANG (HERO PROMO BANNER) -->
                    <!-- Hình ảnh ưu đãi hạt và phụ kiện giảm 30%, tiêu đề nổi bật, nút "Mua Ngay" -->
                    <div class="relative bg-gradient-to-r from-orange-600 via-amber-500 to-rose-600 rounded-3xl p-6 sm:p-10 text-white shadow-xl overflow-hidden">
                        <div class="absolute -right-10 -bottom-10 w-96 h-96 bg-white/10 rounded-full blur-3xl pointer-events-none"></div>
                        <div class="relative z-10 flex flex-col md:flex-row items-center justify-between gap-6">
                            <div class="space-y-3 max-w-xl text-center md:text-left">
                                <div class="inline-flex items-center gap-2 bg-white/20 backdrop-blur-md px-3.5 py-1 rounded-full text-xs font-black tracking-wider uppercase shadow-sm">
                                    <i class="fa-solid fa-fire text-amber-300 animate-pulse"></i>
                                    <span>Ưu Đãi Lớn Tháng 10 • Giảm Đến 30% Hạt & Phụ Kiện</span>
                                </div>
                                <h2 class="text-2xl sm:text-3xl lg:text-4xl font-black tracking-tight leading-tight">
                                    Đại Tiệc Hạt Dinh Dưỡng & Phụ Kiện Thú Cưng 5 Sao
                                </h2>
                                <p class="text-xs sm:text-sm text-white/95 leading-relaxed">
                                    Ưu đãi độc quyền cho Boss cưng: Giảm 30% toàn bộ hạt Royal Canin, Orijen, Pate Monge cao cấp và phụ kiện thú cưng nhập khẩu. Cam kết 100% chính hãng, tích điểm VIP và giao hàng nhanh PetShip360 chỉ 2 giờ!
                                </p>
                                <div class="pt-2 flex flex-wrap items-center justify-center md:justify-start gap-4">
                                    <button @click="scrollToCatalogGrid()" class="px-7 py-3.5 bg-white text-orange-600 hover:bg-orange-50 font-extrabold text-sm rounded-2xl shadow-xl transition transform active:scale-95 flex items-center gap-2">
                                        <span>MUA NGAY</span>
                                        <i class="fa-solid fa-arrow-right"></i>
                                    </button>
                                    <div class="flex items-center gap-3 text-xs text-white font-medium">
                                        <span class="flex items-center gap-1.5"><i class="fa-solid fa-bolt text-amber-300"></i> Giao hỏa tốc 2H</span>
                                        <span class="flex items-center gap-1.5"><i class="fa-solid fa-shield-check text-emerald-300"></i> Đổi trả 3 ngày</span>
                                        <span class="flex items-center gap-1.5"><i class="fa-solid fa-circle-check text-blue-200"></i> 100% Chính hãng</span>
                                    </div>
                                </div>
                            </div>

                            <!-- Hình ảnh ưu đãi hạt & phụ kiện -->
                            <div class="relative flex-shrink-0">
                                <div class="w-64 h-48 sm:w-80 sm:h-56 relative rounded-3xl overflow-hidden shadow-2xl border-4 border-white/25 bg-white/10 backdrop-blur-sm flex items-center justify-center group">
                                    <img src="https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=600&q=80" alt="Ưu đãi hạt và phụ kiện giảm 30%" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                    <div class="absolute top-3 right-3 bg-rose-600 text-white font-black text-xs sm:text-sm px-3 py-1 rounded-xl shadow-lg animate-bounce">
                                        GIẢM 30%
                                    </div>
                                    <div class="absolute bottom-3 left-3 bg-slate-900/80 backdrop-blur-md text-white text-[10px] font-bold px-2.5 py-1 rounded-lg">
                                        Hạt & Phụ kiện chính hãng
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- BỐ CỤC 2 CỘT BÊN DƯỚI: Sidebar Filter (280px) + Product Grid (1100px) -->
                    <div id="shopCatalogSection" class="flex flex-col lg:flex-row gap-8 items-start">
                        
                        <!-- CỘT BÊN TRÁI: SIDEBAR FILTER (RỘNG 280PX) -->
                        <aside class="w-full lg:w-[280px] flex-shrink-0 bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-6">
                            <div class="flex items-center justify-between pb-3 border-b border-slate-100">
                                <div class="flex items-center gap-2 font-bold text-sm text-[#1E293B]">
                                    <i class="fa-solid fa-sliders text-[#F97316]"></i>
                                    <span>Bộ Lọc Sản Phẩm</span>
                                </div>
                                <button @click="resetShopFilters()" class="text-[11px] text-slate-400 hover:text-orange-600 font-medium transition flex items-center gap-1">
                                    <i class="fa-solid fa-rotate-left text-[10px]"></i> Đặt lại
                                </button>
                            </div>

                            <!-- Nhóm 1: Loài thú cưng (Chó, Mèo, Thỏ) -->
                            <div class="space-y-2.5">
                                <label class="block text-xs font-bold text-[#1E293B] uppercase tracking-wider">Loài Thú Cưng</label>
                                <div class="flex flex-wrap gap-1.5">
                                    <button @click="shopSpecies = ''" :class="shopSpecies === '' ? 'bg-[#F97316] text-white font-bold shadow-sm' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'" class="px-3 py-1.5 rounded-xl text-xs transition">
                                        Tất cả
                                    </button>
                                    <button @click="shopSpecies = 'Chó'" :class="shopSpecies === 'Chó' ? 'bg-[#F97316] text-white font-bold shadow-sm' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'" class="px-3 py-1.5 rounded-xl text-xs transition flex items-center gap-1">
                                        <i class="fa-solid fa-dog text-[11px]"></i> Chó
                                    </button>
                                    <button @click="shopSpecies = 'Mèo'" :class="shopSpecies === 'Mèo' ? 'bg-[#F97316] text-white font-bold shadow-sm' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'" class="px-3 py-1.5 rounded-xl text-xs transition flex items-center gap-1">
                                        <i class="fa-solid fa-cat text-[11px]"></i> Mèo
                                    </button>
                                    <button @click="shopSpecies = 'Thỏ'" :class="shopSpecies === 'Thỏ' ? 'bg-[#F97316] text-white font-bold shadow-sm' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'" class="px-3 py-1.5 rounded-xl text-xs transition">
                                        Thỏ
                                    </button>
                                </div>
                            </div>

                            <!-- Nhóm 2: Loại sản phẩm (Thức ăn hạt, Pate, Cát vệ sinh, Phụ kiện & Đồ chơi, Thuốc thú y) -->
                            <div class="space-y-2.5 pt-3 border-t border-slate-100">
                                <label class="block text-xs font-bold text-[#1E293B] uppercase tracking-wider">Loại Sản Phẩm</label>
                                <div class="space-y-1.5 text-xs">
                                    <label class="flex items-center gap-2 p-1.5 rounded-xl hover:bg-slate-50 cursor-pointer transition">
                                        <input type="radio" name="prodType" value="" x-model="shopProductType" class="text-orange-500 focus:ring-orange-400">
                                        <span :class="shopProductType === '' ? 'font-bold text-[#F97316]' : 'text-slate-700'">Tất cả phân loại</span>
                                    </label>
                                    <label class="flex items-center gap-2 p-1.5 rounded-xl hover:bg-slate-50 cursor-pointer transition">
                                        <input type="radio" name="prodType" value="Thức ăn hạt" x-model="shopProductType" class="text-orange-500 focus:ring-orange-400">
                                        <span :class="shopProductType === 'Thức ăn hạt' ? 'font-bold text-[#F97316]' : 'text-slate-700'">Thức ăn hạt</span>
                                    </label>
                                    <label class="flex items-center gap-2 p-1.5 rounded-xl hover:bg-slate-50 cursor-pointer transition">
                                        <input type="radio" name="prodType" value="Pate" x-model="shopProductType" class="text-orange-500 focus:ring-orange-400">
                                        <span :class="shopProductType === 'Pate' ? 'font-bold text-[#F97316]' : 'text-slate-700'">Pate</span>
                                    </label>
                                    <label class="flex items-center gap-2 p-1.5 rounded-xl hover:bg-slate-50 cursor-pointer transition">
                                        <input type="radio" name="prodType" value="Cát vệ sinh" x-model="shopProductType" class="text-orange-500 focus:ring-orange-400">
                                        <span :class="shopProductType === 'Cát vệ sinh' ? 'font-bold text-[#F97316]' : 'text-slate-700'">Cát vệ sinh</span>
                                    </label>
                                    <label class="flex items-center gap-2 p-1.5 rounded-xl hover:bg-slate-50 cursor-pointer transition">
                                        <input type="radio" name="prodType" value="Phụ kiện & Đồ chơi" x-model="shopProductType" class="text-orange-500 focus:ring-orange-400">
                                        <span :class="shopProductType === 'Phụ kiện & Đồ chơi' ? 'font-bold text-[#F97316]' : 'text-slate-700'">Phụ kiện & Đồ chơi</span>
                                    </label>
                                    <label class="flex items-center gap-2 p-1.5 rounded-xl hover:bg-slate-50 cursor-pointer transition">
                                        <input type="radio" name="prodType" value="Thuốc thú y" x-model="shopProductType" class="text-orange-500 focus:ring-orange-400">
                                        <span :class="shopProductType === 'Thuốc thú y' ? 'font-bold text-[#F97316]' : 'text-slate-700'">Thuốc thú y</span>
                                    </label>
                                </div>
                            </div>

                            <!-- Nhóm 3: Thương hiệu -->
                            <div class="space-y-2.5 pt-3 border-t border-slate-100">
                                <label class="block text-xs font-bold text-[#1E293B] uppercase tracking-wider">Thương Hiệu</label>
                                <select x-model="shopBrand" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-orange-400">
                                    <option value="">Tất cả thương hiệu</option>
                                    <option value="Royal Canin">Royal Canin (Pháp)</option>
                                    <option value="Orijen">Orijen (Canada)</option>
                                    <option value="Monge">Monge (Ý)</option>
                                    <option value="Ciao Churu">Ciao Churu (Nhật)</option>
                                    <option value="Cature">Cature (Mỹ)</option>
                                    <option value="Davis">Davis (Mỹ)</option>
                                    <option value="Virbac">Virbac (Pháp)</option>
                                    <option value="Boehringer Ingelheim">Boehringer Ingelheim</option>
                                    <option value="Zoetis">Zoetis (Mỹ)</option>
                                </select>
                            </div>

                            <!-- Nhóm 4: Mức giá (Slider) -->
                            <div class="space-y-2.5 pt-3 border-t border-slate-100">
                                <div class="flex items-center justify-between text-xs">
                                    <label class="font-bold text-[#1E293B] uppercase tracking-wider">Mức Giá Tối Đa</label>
                                    <span class="font-extrabold text-[#F97316]" x-text="formatCurrency(shopMaxPrice)"></span>
                                </div>
                                <input type="range" min="100000" max="1500000" step="50000" x-model.number="shopMaxPrice" class="w-full accent-[#F97316] cursor-pointer">
                                <div class="flex justify-between text-[10px] text-slate-400">
                                    <span>100.000đ</span>
                                    <span>1.500.000đ</span>
                                </div>
                            </div>

                            <!-- Nhóm 5: Checkbox "Giao hỏa tốc PetShip360" -->
                            <div class="pt-3 border-t border-slate-100">
                                <label class="flex items-center gap-2.5 p-3 rounded-2xl bg-orange-50/70 border border-orange-200 hover:bg-orange-100/60 cursor-pointer transition">
                                    <input type="checkbox" x-model="shopExpressShip" class="rounded text-[#F97316] focus:ring-orange-400 w-4 h-4">
                                    <div class="text-xs">
                                        <span class="font-extrabold text-slate-800 flex items-center gap-1">
                                            <i class="fa-solid fa-bolt text-[#F97316]"></i>
                                            <span>Giao hỏa tốc PetShip360</span>
                                        </span>
                                        <span class="text-[10px] text-orange-700 block mt-0.5">Nhận hàng trong 2 Giờ tại nội thành</span>
                                    </div>
                                </label>
                            </div>
                        </aside>

                        <!-- CỘT BÊN PHẢI: PRODUCT GRID (RỘNG 1100PX) -->
                        <main class="flex-1 w-full space-y-6">
                            
                            <!-- Thanh Sắp Xếp Phía Trên -->
                            <div class="bg-white rounded-2xl p-4 border border-slate-200 shadow-sm flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                                <div class="flex items-center gap-2 text-xs sm:text-sm">
                                    <span class="font-bold text-[#1E293B]">Hiển thị:</span>
                                    <span class="text-[#F97316] font-extrabold" x-text="filteredCatalogProducts.length + ' sản phẩm'"></span>
                                    <span class="text-slate-400 hidden sm:inline">• Nền trắng #FFFFFF, Màu nhấn Cam #F97316</span>
                                </div>

                                <!-- "Xếp theo: Mới nhất | Bán chạy | Giá tăng/giảm" -->
                                <div class="flex items-center gap-2 text-xs">
                                    <span class="text-slate-500 font-medium">Xếp theo:</span>
                                    <div class="flex items-center gap-1 bg-slate-100 p-1 rounded-xl">
                                        <button @click="shopSortBy = 'newest'" :class="shopSortBy === 'newest' ? 'bg-white text-[#F97316] font-bold shadow-sm' : 'text-slate-600 hover:text-slate-900'" class="px-3 py-1.5 rounded-lg transition">
                                            Mới nhất
                                        </button>
                                        <button @click="shopSortBy = 'bestseller'" :class="shopSortBy === 'bestseller' ? 'bg-white text-[#F97316] font-bold shadow-sm' : 'text-slate-600 hover:text-slate-900'" class="px-3 py-1.5 rounded-lg transition">
                                            Bán chạy
                                        </button>
                                        <button @click="shopSortBy = 'price_asc'" :class="shopSortBy === 'price_asc' ? 'bg-white text-[#F97316] font-bold shadow-sm' : 'text-slate-600 hover:text-slate-900'" class="px-3 py-1.5 rounded-lg transition flex items-center gap-1">
                                            Giá <i class="fa-solid fa-arrow-up text-[10px]"></i>
                                        </button>
                                        <button @click="shopSortBy = 'price_desc'" :class="shopSortBy === 'price_desc' ? 'bg-white text-[#F97316] font-bold shadow-sm' : 'text-slate-600 hover:text-slate-900'" class="px-3 py-1.5 rounded-lg transition flex items-center gap-1">
                                            Giá <i class="fa-solid fa-arrow-down text-[10px]"></i>
                                        </button>
                                    </div>
                                </div>
                            </div>

                            <!-- LƯỚI SẢN PHẨM: 4 CỘT X 3 HÀNG (12 SẢN PHẨM) -->
                            <!-- Card sản phẩm: Tỷ lệ ảnh 1:1, Badge giảm giá đỏ góc trên, Tên thương hiệu nhạt, Tên sản phẩm (tối đa 2 dòng), Số sao đánh giá (4.9★ - 128 đã bán), Giá bán in đậm đỏ/cam + Giá gốc gạch ngang, Nút tròn icon Giỏ hàng góc dưới -->
                            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-4">
                                <template x-for="prod in paginatedCatalogProducts" :key="prod.id">
                                    <div @click="openProductDetailPage(prod)" class="bg-white rounded-2xl p-3 border border-slate-200 shadow-sm hover:shadow-lg transition-all duration-200 flex flex-col justify-between group cursor-pointer relative overflow-hidden">
                                        
                                        <!-- Ảnh 1:1 + Badge giảm giá đỏ góc trên -->
                                        <div class="relative w-full aspect-square rounded-xl overflow-hidden bg-slate-50 flex items-center justify-center p-2">
                                            <img :src="prod.image || prod.img" :alt="prod.name" class="w-full h-full object-contain group-hover:scale-105 transition-transform duration-300">
                                            
                                            <!-- Badge giảm giá đỏ góc trên -->
                                            <span class="absolute top-2 left-2 bg-rose-600 text-white font-extrabold text-[10px] px-2 py-0.5 rounded-md shadow-sm" x-text="prod.discountPercent || '-20%'"></span>

                                            <!-- Badge Giao hỏa tốc nếu có -->
                                            <template x-if="prod.expressShip">
                                                <span class="absolute top-2 right-2 bg-amber-400 text-slate-900 font-black text-[9px] px-1.5 py-0.5 rounded-md shadow-sm flex items-center gap-0.5" title="Giao hỏa tốc PetShip360 trong 2h">
                                                    <i class="fa-solid fa-bolt text-[8px]"></i> 2H
                                                </span>
                                            </template>
                                        </div>

                                        <!-- Thông tin sản phẩm -->
                                        <div class="pt-3 pb-1 space-y-1.5 flex-1 flex flex-col justify-between">
                                            <div>
                                                <!-- Tên thương hiệu nhạt -->
                                                <p class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider truncate" x-text="prod.brand"></p>
                                                
                                                <!-- Tên sản phẩm (tối đa 2 dòng) -->
                                                <h4 class="text-xs sm:text-sm font-bold text-[#1E293B] line-clamp-2 leading-snug group-hover:text-[#F97316] transition" x-text="prod.name" :title="prod.name"></h4>
                                            </div>

                                            <div>
                                                <!-- Số sao đánh giá (ví dụ: 4.9★ - 128 đã bán) -->
                                                <div class="flex items-center gap-1.5 text-xs text-slate-500 pt-1">
                                                    <div class="flex items-center text-amber-400 text-xs">
                                                        <i class="fa-solid fa-star"></i>
                                                        <span class="font-bold text-slate-800 ml-1" x-text="prod.rating"></span>
                                                    </div>
                                                    <span class="text-slate-300">•</span>
                                                    <span class="text-[11px] text-slate-400" x-text="(prod.sold || 128) + ' đã bán'"></span>
                                                </div>

                                                <!-- Giá bán in đậm đỏ/cam + Giá gốc gạch ngang + Nút tròn icon Giỏ hàng góc dưới -->
                                                <div class="pt-2 flex items-center justify-between border-t border-slate-100 mt-2">
                                                    <div>
                                                        <div class="text-sm sm:text-base font-extrabold text-[#F97316]" x-text="formatCurrency(prod.price)"></div>
                                                        <div class="text-[10px] text-slate-400 line-through font-medium" x-text="formatCurrency(prod.originalPrice || Math.round(prod.price * 1.25))"></div>
                                                    </div>

                                                    <!-- Nút tròn icon Giỏ hàng góc dưới -->
                                                    <button @click.stop="addToCart({ id: prod.id, name: prod.name, price: prod.price, image: prod.image || prod.img, weight: '3kg', flavor: 'Vị chuẩn' })" class="w-9 h-9 rounded-full bg-orange-50 text-[#F97316] hover:bg-[#F97316] hover:text-white transition flex items-center justify-center shadow-sm transform active:scale-90" title="Thêm vào giỏ hàng">
                                                        <i class="fa-solid fa-cart-plus text-xs"></i>
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </template>
                            </div>

                            <!-- Phân trang (Pagination) chuẩn ở cuối trang -->
                            <div class="bg-white rounded-2xl p-4 border border-slate-200 shadow-sm flex items-center justify-between">
                                <span class="text-xs text-slate-500 hidden sm:inline" x-text="'Trang ' + shopCurrentPage + ' / ' + shopTotalPages + ' (Tổng ' + filteredCatalogProducts.length + ' sản phẩm)'"></span>
                                <div class="flex items-center gap-1.5 mx-auto sm:mx-0">
                                    <button @click="if(shopCurrentPage > 1) shopCurrentPage--" :disabled="shopCurrentPage === 1" class="px-3 py-1.5 rounded-xl border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-50 disabled:opacity-40 disabled:cursor-not-allowed transition flex items-center gap-1">
                                        <i class="fa-solid fa-chevron-left text-[10px]"></i>
                                        <span>Trang trước</span>
                                    </button>
                                    <template x-for="p in shopTotalPages" :key="p">
                                        <button @click="shopCurrentPage = p" :class="shopCurrentPage === p ? 'bg-[#F97316] text-white font-bold' : 'bg-white border border-slate-200 text-slate-700 hover:bg-slate-50'" class="w-8 h-8 rounded-xl text-xs transition font-semibold" x-text="p"></button>
                                    </template>
                                    <button @click="if(shopCurrentPage < shopTotalPages) shopCurrentPage++" :disabled="shopCurrentPage === shopTotalPages" class="px-3 py-1.5 rounded-xl border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-50 disabled:opacity-40 disabled:cursor-not-allowed transition flex items-center gap-1">
                                        <span>Trang sau</span>
                                        <i class="fa-solid fa-chevron-right text-[10px]"></i>
                                    </button>
                                </div>
                            </div>
                        </main>
                    </div>
                </div>

                <!-- ======================================================== -->
                <!-- CHẾ ĐỘ 2: TRANG CHI TIẾT SẢN PHẨM (PRODUCT DETAIL PAGE) -->
                <!-- ======================================================== -->
                <div x-show="shopViewMode === 'detail'" class="space-y-8 animate-fadeIn">
                    <nav class="flex items-center gap-2 text-xs sm:text-sm text-slate-500 py-2 border-b border-slate-100">
                    <a href="#" @click.prevent="activeCustomerTab = 'home'" class="hover:text-brand-600 transition flex items-center gap-1">
                        <i class="fa-solid fa-house text-xs"></i>Trang chủ
                    </a>
                    <i class="fa-solid fa-chevron-right text-[10px] text-slate-400"></i>
                    <a href="#" @click.prevent="backToShopCatalog()" class="hover:text-orange-600 font-bold text-slate-700 transition flex items-center gap-1"><i class="fa-solid fa-box-open text-xs"></i>Sản phẩm (Cửa hàng)</a>
                    <i class="fa-solid fa-chevron-right text-[10px] text-slate-400"></i>
                    <span class="text-slate-600 font-medium">Thức ăn thú cưng</span>
                    <i class="fa-solid fa-chevron-right text-[10px] text-slate-400"></i>
                    <span class="text-slate-900 font-bold truncate max-w-xs" x-text="currentProductDetail.name"></span>
                </nav>

                <!-- BỐ CỤC CHÍNH 2 CỘT (THẺ SẢN PHẨM CHÍNH) -->
                <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm">
                    <div class="flex flex-col lg:flex-row gap-8 lg:gap-12 items-start justify-center">
                        
                        <!-- CỘT TRÁI (GALLERY ẢNH - 500PX) -->
                        <div class="w-full lg:w-[500px] flex-shrink-0 space-y-4">
                            <!-- Ảnh lớn trung tâm -->
                            <div class="relative w-full h-[360px] sm:h-[420px] rounded-2xl overflow-hidden border border-slate-200 bg-slate-50 group flex items-center justify-center p-4">
                                <img :src="mainProductImage" :alt="currentProductDetail.name" class="w-full h-full object-contain transform group-hover:scale-105 transition duration-300">
                                <div class="absolute top-3 left-3 bg-rose-500 text-white text-xs font-black px-2.5 py-1 rounded-lg uppercase tracking-wider shadow">
                                    -18% GIẢM
                                </div>
                                <div class="absolute top-3 right-3 bg-white/90 backdrop-blur text-slate-600 p-2 rounded-xl shadow hover:text-rose-500 cursor-pointer transition">
                                    <i class="fa-regular fa-heart text-base"></i>
                                </div>
                            </div>

                            <!-- Dãy 4 ảnh nhỏ thumbnail ở bên dưới để click chuyển ảnh -->
                            <div class="grid grid-cols-4 gap-3">
                                <template x-for="(thumb, index) in productThumbnails" :key="index">
                                    <button @click="mainProductImage = thumb" :class="mainProductImage === thumb ? 'border-2 border-orange-500 ring-2 ring-orange-200 shadow' : 'border border-slate-200 hover:border-slate-300 opacity-75 hover:opacity-100'" class="h-20 sm:h-24 rounded-xl overflow-hidden bg-slate-50 p-1 transition flex items-center justify-center">
                                        <img :src="thumb" class="w-full h-full object-cover rounded-lg">
                                    </button>
                                </template>
                            </div>
                        </div>

                        <!-- CỘT PHẢI (THÔNG TIN MUA HÀNG - 600PX) -->
                        <div class="w-full lg:w-[600px] flex-shrink-0 space-y-5">
                            
                            <!-- Tên sản phẩm to rõ (Font 24px, Bold) -->
                            <h1 class="text-2xl sm:text-[24px] font-bold text-slate-900 leading-snug tracking-tight" x-text="currentProductDetail.name"></h1>

                            <!-- Khối Đánh giá (4.8/5 sao - 86 nhận xét) + Mã SKU + Tình trạng -->
                            <div class="flex flex-wrap items-center gap-3 text-xs sm:text-sm text-slate-500 pb-3 border-b border-slate-100">
                                <div class="flex items-center gap-1.5 text-amber-500">
                                    <div class="flex text-sm">
                                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star-half-stroke"></i>
                                    </div>
                                    <span class="font-bold text-slate-800">4.8 / 5</span>
                                    <span class="text-slate-400">(86 nhận xét)</span>
                                </div>
                                <span class="text-slate-300">|</span>
                                <div class="font-mono text-slate-600">
                                    SKU: <span class="font-semibold text-slate-800">PC360-RC-MA01</span>
                                </div>
                                <span class="text-slate-300">|</span>
                                <div class="inline-flex items-center gap-1.5 text-emerald-600 font-semibold bg-emerald-50 px-2.5 py-0.5 rounded-full text-xs">
                                    <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
                                    <span>Còn hàng (24 bao trong kho)</span>
                                </div>
                            </div>

                            <!-- Khối Bảng Giá: Giá khuyến mãi to nổi bật (màu Cam), Giá niêm yết gạch ngang -->
                            <div class="bg-orange-50/60 rounded-2xl p-4 sm:p-5 border border-orange-100 flex items-baseline gap-4">
                                <div class="text-3xl sm:text-4xl font-extrabold text-orange-600 tracking-tight" x-text="formatCurrency(currentProductPrice)"></div>
                                <div class="text-base sm:text-lg text-slate-400 line-through font-medium" x-text="formatCurrency(currentProductOriginalPrice)"></div>
                                <span class="bg-orange-500 text-white text-xs font-bold px-2 py-0.5 rounded-md shadow-sm">Tiết kiệm 75.000đ</span>
                            </div>

                            <!-- Bộ chọn Biến thể (Variants selector) -->
                            <div class="space-y-4 pt-1">
                                <!-- Khối chọn Trọng lượng (1kg, 3kg, 10kg) -->
                                <div>
                                    <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">Chọn Trọng Lượng:</label>
                                    <div class="flex flex-wrap gap-2.5">
                                        <button @click="selectedWeight = '1kg'" :class="selectedWeight === '1kg' ? 'border-2 border-orange-500 bg-orange-50 text-orange-700 font-bold shadow-sm' : 'border border-slate-200 bg-white text-slate-700 hover:border-slate-300'" class="px-4 py-2.5 rounded-xl text-xs sm:text-sm transition flex items-center gap-1.5">
                                            <span>1kg (Dùng thử)</span>
                                        </button>
                                        <button @click="selectedWeight = '3kg'" :class="selectedWeight === '3kg' ? 'border-2 border-orange-500 bg-orange-50 text-orange-700 font-bold shadow-sm' : 'border border-slate-200 bg-white text-slate-700 hover:border-slate-300'" class="px-4 py-2.5 rounded-xl text-xs sm:text-sm transition flex items-center gap-1.5">
                                            <span>3kg (Phổ biến nhất)</span>
                                            <span class="text-[9px] bg-orange-500 text-white font-bold px-1.5 py-0.2 rounded-full">Hot</span>
                                        </button>
                                        <button @click="selectedWeight = '10kg'" :class="selectedWeight === '10kg' ? 'border-2 border-orange-500 bg-orange-50 text-orange-700 font-bold shadow-sm' : 'border border-slate-200 bg-white text-slate-700 hover:border-slate-300'" class="px-4 py-2.5 rounded-xl text-xs sm:text-sm transition flex items-center gap-1.5">
                                            <span>10kg (Bao lớn tiết kiệm)</span>
                                        </button>
                                    </div>
                                </div>

                                <!-- Khối chọn Hương vị (Vị Cá Hồi, Vị Thịt Bò) -->
                                <div>
                                    <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">Chọn Hương Vị:</label>
                                    <div class="flex flex-wrap gap-2.5">
                                        <button @click="selectedFlavor = 'salmon'" :class="selectedFlavor === 'salmon' ? 'border-2 border-orange-500 bg-orange-50 text-orange-700 font-bold shadow-sm' : 'border border-slate-200 bg-white text-slate-700 hover:border-slate-300'" class="px-4 py-2.5 rounded-xl text-xs sm:text-sm transition flex items-center gap-2">
                                            <i class="fa-solid fa-fish text-brand-600"></i>
                                            <span>Vị Cá Hồi (Dưỡng lông & Da)</span>
                                        </button>
                                        <button @click="selectedFlavor = 'beef'" :class="selectedFlavor === 'beef' ? 'border-2 border-orange-500 bg-orange-50 text-orange-700 font-bold shadow-sm' : 'border border-slate-200 bg-white text-slate-700 hover:border-slate-300'" class="px-4 py-2.5 rounded-xl text-xs sm:text-sm transition flex items-center gap-2">
                                            <i class="fa-solid fa-drumstick-bite text-amber-600"></i>
                                            <span>Vị Thịt Bò (Phát triển cơ bắp)</span>
                                        </button>
                                    </div>
                                </div>

                                <!-- Bộ chọn Số lượng (Nút - 1 +) -->
                                <div class="pt-2 flex items-center gap-4">
                                    <label class="text-xs font-bold text-slate-700 uppercase tracking-wider">Số lượng:</label>
                                    <div class="flex items-center border border-slate-300 rounded-xl overflow-hidden bg-white shadow-sm">
                                        <button @click="if (productDetailQty > 1) productDetailQty--" class="w-10 h-10 flex items-center justify-center text-slate-600 hover:bg-slate-100 transition font-bold text-base select-none">−</button>
                                        <input type="number" min="1" max="99" x-model.number="productDetailQty" class="w-14 h-10 text-center font-bold text-slate-800 text-sm focus:outline-none border-x border-slate-200">
                                        <button @click="productDetailQty++" class="w-10 h-10 flex items-center justify-center text-slate-600 hover:bg-slate-100 transition font-bold text-base select-none">+</button>
                                    </div>
                                    <span class="text-xs text-slate-400">Kho sẵn sàng giao trong 2h</span>
                                </div>
                            </div>

                            <!-- Khối Nút Thao Tác: Thêm Vào Giỏ (Viền cam) & MUA NGAY (Nền cam chữ trắng to) -->
                            <div class="pt-4 flex flex-col sm:flex-row gap-3">
                                <button @click="addProductDetailToCart()" class="flex-1 py-3.5 px-6 rounded-2xl border-2 border-orange-500 text-orange-600 hover:bg-orange-50 font-bold text-sm sm:text-base transition flex items-center justify-center gap-2 shadow-sm">
                                    <i class="fa-solid fa-cart-plus text-base"></i>
                                    <span>Thêm Vào Giỏ Hàng</span>
                                </button>
                                <button @click="buyNowProductDetail()" class="flex-1 py-3.5 px-6 rounded-2xl bg-orange-500 hover:bg-orange-600 text-white font-extrabold text-sm sm:text-base transition shadow-lg shadow-orange-500/30 flex items-center justify-center gap-2 transform active:scale-98">
                                    <i class="fa-solid fa-bolt text-base"></i>
                                    <span>MUA NGAY</span>
                                </button>
                            </div>

                            <!-- Khối Badge Cam Kết -->
                            <div class="pt-4 border-t border-slate-100 grid grid-cols-3 gap-3 text-center">
                                <div class="p-3 bg-slate-50 rounded-2xl border border-slate-100 space-y-1">
                                    <i class="fa-solid fa-shield-halved text-brand-600 text-lg"></i>
                                    <p class="text-xs font-bold text-slate-800">Chính hãng 100%</p>
                                    <p class="text-[10px] text-slate-400">Đầy đủ tem phụ & Hóa đơn</p>
                                </div>
                                <div class="p-3 bg-slate-50 rounded-2xl border border-slate-100 space-y-1">
                                    <i class="fa-solid fa-rotate-left text-teal-600 text-lg"></i>
                                    <p class="text-xs font-bold text-slate-800">Đổi trả 3 ngày</p>
                                    <p class="text-[10px] text-slate-400">Nếu bé dị ứng hạt</p>
                                </div>
                                <div class="p-3 bg-slate-50 rounded-2xl border border-slate-100 space-y-1">
                                    <i class="fa-solid fa-truck-fast text-orange-600 text-lg"></i>
                                    <p class="text-xs font-bold text-slate-800">Giao PetShip 2H</p>
                                    <p class="text-[10px] text-slate-400">Hỏa tốc nội thành</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- PHẦN BÊN DƯỚI (TABS THÔNG TIN CHI TIẾT) -->
                <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-6">
                    <!-- Tab Headers -->
                    <div class="flex border-b border-slate-200 gap-6 sm:gap-8 overflow-x-auto text-sm sm:text-base font-bold">
                        <button @click="productDetailTab = 'desc'" :class="productDetailTab === 'desc' ? 'text-orange-600 border-b-2 border-orange-500 pb-3' : 'text-slate-500 hover:text-slate-800 pb-3'" class="transition whitespace-nowrap">
                            <i class="fa-solid fa-circle-info mr-1.5"></i>Mô Tả & Thành Phần Dinh Dưỡng
                        </button>
                        <button @click="productDetailTab = 'guide'" :class="productDetailTab === 'guide' ? 'text-orange-600 border-b-2 border-orange-500 pb-3' : 'text-slate-500 hover:text-slate-800 pb-3'" class="transition whitespace-nowrap">
                            <i class="fa-solid fa-scale-balanced mr-1.5"></i>Hướng Dẫn Cho Ăn Theo Cân Nặng
                        </button>
                        <button @click="productDetailTab = 'reviews'" :class="productDetailTab === 'reviews' ? 'text-orange-600 border-b-2 border-orange-500 pb-3' : 'text-slate-500 hover:text-slate-800 pb-3'" class="transition whitespace-nowrap flex items-center gap-1.5">
                            <i class="fa-solid fa-comments mr-1"></i>Đánh Giá Từ Khách Hàng
                            <span class="bg-orange-100 text-orange-700 text-xs px-2 py-0.5 rounded-full font-bold">86</span>
                        </button>
                    </div>

                    <!-- TAB 1: Mô tả chi tiết sản phẩm & Thành phần dinh dưỡng -->
                    <div x-show="productDetailTab === 'desc'" class="space-y-6 text-sm text-slate-700 leading-relaxed animate-fadeIn">
                        <div>
                            <h4 class="font-bold text-base text-slate-900 mb-2">Đặc điểm nổi bật của dòng sản phẩm:</h4>
                            <p>Sản phẩm thức ăn hạt Royal Canin Mini Adult được thiết kế chuyên biệt đáp ứng nhu cầu năng lượng cao của các giống chó nhỏ (cân nặng khi trưởng thành dưới 10kg). Chứa hàm lượng L-Carnitine tối ưu giúp kích thích chuyển hóa chất béo, duy trì khối lượng cơ nạc và vóc dáng thon gọn.</p>
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
                            <div class="bg-slate-50 p-4 rounded-2xl border border-slate-100 space-y-2">
                                <h5 class="font-bold text-sm text-slate-800 flex items-center gap-2">
                                    <i class="fa-solid fa-dna text-brand-600"></i>Thành phần nguyên liệu chính
                                </h5>
                                <p class="text-xs text-slate-600 leading-normal">Protein gia cầm sấy khô, bắp, bột bắp, mỡ động vật, gluten bắp, protein thực vật cô lập (L.I.P.), lúa mì, protein động vật thủy phân, gạo, củ cải đường, khoáng chất, dầu cá, dầu đậu nành, men nấm, fructo-oligo-sacarit.</p>
                            </div>
                            <div class="bg-slate-50 p-4 rounded-2xl border border-slate-100 space-y-2">
                                <h5 class="font-bold text-sm text-slate-800 flex items-center gap-2">
                                    <i class="fa-solid fa-chart-pie text-orange-600"></i>Chỉ tiêu phân tích dinh dưỡng
                                </h5>
                                <div class="grid grid-cols-2 gap-2 text-xs">
                                    <div>Protein thô: <span class="font-bold text-slate-800">27.0%</span></div>
                                    <div>Chất béo thô: <span class="font-bold text-slate-800">16.0%</span></div>
                                    <div>Xơ thô: <span class="font-bold text-slate-800">1.3%</span></div>
                                    <div>Tro thô: <span class="font-bold text-slate-800">4.9%</span></div>
                                    <div>EPA/DHA: <span class="font-bold text-slate-800">0.25%</span></div>
                                    <div>Canxi & Photpho: <span class="font-bold text-slate-800">Cân đối 1.2:1</span></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- TAB 2: Hướng dẫn cho ăn theo cân nặng của Pet -->
                    <div x-show="productDetailTab === 'guide'" class="space-y-6 text-sm text-slate-700 animate-fadeIn">
                        <p class="text-xs sm:text-sm text-slate-600">Khẩu phần ăn hàng ngày được tính toán chuẩn theo cân nặng thực tế và mức độ vận động của thú cưng. Luôn chuẩn bị sẵn nước uống sạch cho bé.</p>
                        <div class="overflow-x-auto border border-slate-200 rounded-2xl shadow-sm">
                            <table class="w-full text-left text-xs sm:text-sm border-collapse">
                                <thead>
                                    <tr class="bg-slate-50 text-slate-800 border-b border-slate-200 font-bold">
                                        <th class="py-3 px-4">Cân Nặng Của Pet (kg)</th>
                                        <th class="py-3 px-4">Vận động ít (< 1h/ngày)</th>
                                        <th class="py-3 px-4">Vận động bình thường</th>
                                        <th class="py-3 px-4">Vận động nhiều (> 2h/ngày)</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-100">
                                    <tr class="hover:bg-slate-50/60">
                                        <td class="py-3 px-4 font-bold text-slate-800">2 kg (Chihuahua, Teacup)</td>
                                        <td class="py-3 px-4">40g (khoảng 3/8 cốc)</td>
                                        <td class="py-3 px-4 font-semibold text-orange-600">47g (khoảng 4/8 cốc)</td>
                                        <td class="py-3 px-4">53g (khoảng 5/8 cốc)</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50/60">
                                        <td class="py-3 px-4 font-bold text-slate-800">4 kg (Poodle Tiny, Phốc Sóc)</td>
                                        <td class="py-3 px-4">68g (khoảng 6/8 cốc)</td>
                                        <td class="py-3 px-4 font-semibold text-orange-600">79g (khoảng 1 cốc)</td>
                                        <td class="py-3 px-4">89g (khoảng 1 + 1/8 cốc)</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50/60">
                                        <td class="py-3 px-4 font-bold text-slate-800">6 kg (Corgi nhỏ, Pug nhỏ)</td>
                                        <td class="py-3 px-4">92g (khoảng 1 + 1/8 cốc)</td>
                                        <td class="py-3 px-4 font-semibold text-orange-600">107g (khoảng 1 + 2/8 cốc)</td>
                                        <td class="py-3 px-4">121g (khoảng 1 + 4/8 cốc)</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50/60">
                                        <td class="py-3 px-4 font-bold text-slate-800">8 kg (Poodle Standard, Corgi)</td>
                                        <td class="py-3 px-4">114g (khoảng 1 + 3/8 cốc)</td>
                                        <td class="py-3 px-4 font-semibold text-orange-600">132g (khoảng 1 + 5/8 cốc)</td>
                                        <td class="py-3 px-4">150g (khoảng 1 + 7/8 cốc)</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50/60">
                                        <td class="py-3 px-4 font-bold text-slate-800">10 kg (Pháp, Beagle nhỏ)</td>
                                        <td class="py-3 px-4">135g (khoảng 1 + 5/8 cốc)</td>
                                        <td class="py-3 px-4 font-semibold text-orange-600">156g (khoảng 1 + 7/8 cốc)</td>
                                        <td class="py-3 px-4">177g (khoảng 2 + 1/8 cốc)</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- TAB 3: Đánh giá từ khách hàng -->
                    <div x-show="productDetailTab === 'reviews'" class="space-y-6 animate-fadeIn">
                        <!-- Khối Tổng Điểm & Bộ Lọc -->
                        <div class="bg-slate-50 rounded-2xl p-5 border border-slate-100 flex flex-col md:flex-row items-center justify-between gap-6">
                            <div class="flex items-center gap-5">
                                <div class="text-center">
                                    <div class="text-4xl sm:text-5xl font-black text-slate-900">4.8</div>
                                    <div class="flex text-amber-400 text-sm mt-1">
                                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star-half-stroke"></i>
                                    </div>
                                    <span class="text-xs text-slate-400 mt-1 block">86 đánh giá</span>
                                </div>
                                <div class="space-y-1 text-xs text-slate-500 w-48 sm:w-60">
                                    <div class="flex items-center gap-2">
                                        <span>5★</span>
                                        <div class="flex-1 bg-slate-200 h-2 rounded-full overflow-hidden">
                                            <div class="bg-amber-400 h-full w-[88%]"></div>
                                        </div>
                                        <span>88%</span>
                                    </div>
                                    <div class="flex items-center gap-2">
                                        <span>4★</span>
                                        <div class="flex-1 bg-slate-200 h-2 rounded-full overflow-hidden">
                                            <div class="bg-amber-400 h-full w-[10%]"></div>
                                        </div>
                                        <span>10%</span>
                                    </div>
                                    <div class="flex items-center gap-2">
                                        <span>3★</span>
                                        <div class="flex-1 bg-slate-200 h-2 rounded-full overflow-hidden">
                                            <div class="bg-amber-400 h-full w-[2%]"></div>
                                        </div>
                                        <span>2%</span>
                                    </div>
                                </div>
                            </div>
                            <div class="flex flex-col sm:flex-row items-center gap-3">
                                <button @click="onlyWithPhotos = !onlyWithPhotos" :class="onlyWithPhotos ? 'bg-orange-500 text-white font-bold' : 'bg-white border border-slate-200 text-slate-700'" class="px-4 py-2.5 rounded-xl text-xs transition shadow-sm flex items-center gap-2">
                                    <i class="fa-solid fa-camera"></i>
                                    <span>Xem ảnh thực tế (24)</span>
                                </button>
                                <button @click="openReviewModal(customerOrdersEnhanced[0])" class="bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs px-5 py-2.5 rounded-xl transition shadow flex items-center gap-2">
                                    <i class="fa-solid fa-pen-to-square"></i>
                                    <span>Viết Đánh Giá</span>
                                </button>
                            </div>
                        </div>

                        <!-- Danh sách đánh giá -->
                        <div class="space-y-4">
                            <template x-for="(rev, idx) in productReviewsList" :key="idx">
                                <div class="p-4 sm:p-5 rounded-2xl border border-slate-100 hover:border-slate-200 transition bg-white space-y-3">
                                    <div class="flex items-center justify-between">
                                        <div class="flex items-center gap-3">
                                            <img :src="rev.avatar" class="w-10 h-10 rounded-full object-cover border border-slate-200">
                                            <div>
                                                <h5 class="font-bold text-xs sm:text-sm text-slate-800 flex items-center gap-2">
                                                    <span x-text="rev.author"></span>
                                                    <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.2 rounded-full">Đã mua tại PetCare360</span>
                                                </h5>
                                                <div class="flex items-center gap-2 mt-0.5">
                                                    <div class="flex text-amber-400 text-xs">
                                                        <template x-for="s in rev.stars" :key="s">
                                                            <i class="fa-solid fa-star"></i>
                                                        </template>
                                                    </div>
                                                    <span class="text-[11px] text-slate-400" x-text="rev.date"></span>
                                                </div>
                                            </div>
                                        </div>
                                        <span class="text-xs text-slate-400 font-mono hidden sm:inline" x-text="rev.variant"></span>
                                    </div>
                                    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed" x-text="rev.comment"></p>
                                    <template x-if="rev.photos && rev.photos.length > 0">
                                        <div class="flex gap-2 pt-1">
                                            <template x-for="(p, pidx) in rev.photos" :key="pidx">
                                                <img :src="p" class="w-16 h-16 sm:w-20 sm:h-20 rounded-xl object-cover border border-slate-200 shadow-sm hover:scale-105 transition cursor-pointer">
                                            </template>
                                        </div>
                                    </template>
                                </div>
                            </template>
                        </div>
                    </div>
                </div>

                <!-- ======================================================== -->
                <!-- SECTION: SẢN PHẨM TƯƠNG TỰ BẠN CÓ THỂ THÍCH (RESTORED 4-CARD HORIZONTAL CAROUSEL) -->
                <!-- ======================================================== -->
                <div class="space-y-4 pt-4 border-t border-slate-200">
                    <div class="flex items-center justify-between">
                        <div>
                            <h3 class="text-lg sm:text-xl font-bold text-slate-900">Sản phẩm tương tự bạn có thể thích</h3>
                            <p class="text-xs text-slate-500">Gợi ý từ các bác sĩ dinh dưỡng PetCare360</p>
                        </div>
                        <!-- Điều hướng: Xem tất cả 12 sản phẩm + Nút mũi tên điều hướng Trái/Phải -->
                        <div class="flex items-center gap-2">
                            <span class="text-xs text-[#F97316] font-bold hover:underline cursor-pointer mr-1 hidden sm:inline" @click="backToShopCatalog()">Xem tất cả 12 sản phẩm</span>
                            <div class="flex items-center gap-1.5">
                                <button @click="scrollSimilarLeft()" class="w-8 h-8 rounded-full border border-slate-200 bg-white hover:bg-orange-50 text-slate-600 hover:text-orange-600 shadow-sm flex items-center justify-center transition active:scale-90" title="Trượt sang trái">
                                    <i class="fa-solid fa-chevron-left text-xs"></i>
                                </button>
                                <button @click="scrollSimilarRight()" class="w-8 h-8 rounded-full border border-slate-200 bg-white hover:bg-orange-50 text-slate-600 hover:text-orange-600 shadow-sm flex items-center justify-center transition active:scale-90" title="Trượt xem tiếp sản phẩm">
                                    <i class="fa-solid fa-chevron-right text-xs"></i>
                                </button>
                            </div>
                        </div>
                    </div>

                    <!-- Product Carousel: Set thuộc tính hiển thị chính xác 4 thẻ sản phẩm (Product Card) nằm ngang trên cùng một hàng (desktop), kích hoạt trượt ngang (Horizontal scroll/Swipe) -->
                    <div id="product-detail-similar-carousel" class="flex gap-4 overflow-x-auto scroll-smooth snap-x pb-3 pt-1 no-scrollbar hide-scrollbar">
                        <template x-for="sim in similarProductsList" :key="'sim-' + sim.id">
                            <div @click="openProductDetailPage(sim)" class="snap-start flex-shrink-0 w-[260px] sm:w-[calc(50%-8px)] md:w-[calc(33.333%-11px)] lg:w-[calc(25%-12px)] bg-white rounded-2xl p-3 border border-slate-200 shadow-sm hover:shadow-lg transition-all duration-200 flex flex-col justify-between group cursor-pointer relative overflow-hidden">
                                
                                <!-- Ảnh thumbnail sản phẩm (bo góc, tỷ lệ 1:1) + Badge giảm giá & Giao nhanh 2h -->
                                <div class="relative w-full aspect-square rounded-xl overflow-hidden bg-slate-50 flex items-center justify-center p-2">
                                    <img :src="sim.image || sim.img" :alt="sim.name" class="w-full h-full object-contain group-hover:scale-105 transition-transform duration-300">
                                    <span class="absolute top-2 left-2 bg-rose-600 text-white font-extrabold text-[10px] px-2 py-0.5 rounded-md shadow-sm" x-text="sim.discountPercent || '-15%'"></span>
                                    <template x-if="sim.expressShip">
                                        <span class="absolute top-2 right-2 bg-amber-400 text-slate-900 font-black text-[9px] px-1.5 py-0.5 rounded-md shadow-sm flex items-center gap-0.5">
                                            <i class="fa-solid fa-bolt text-[8px]"></i> 2H
                                        </span>
                                    </template>
                                </div>

                                <!-- Cấu trúc Thẻ sản phẩm chuẩn: Tên sản phẩm tối đa 2 dòng (...), Số sao & Lượt mua, Giá khuyến mãi + gốc gạch ngang, Nút giỏ hàng -->
                                <div class="pt-3 pb-1 space-y-1.5 flex-1 flex flex-col justify-between">
                                    <div>
                                        <p class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider truncate" x-text="sim.brand || sim.category"></p>
                                        <h4 class="text-xs sm:text-sm font-bold text-[#1E293B] line-clamp-2 leading-snug group-hover:text-[#F97316] transition" x-text="sim.name" :title="sim.name"></h4>
                                    </div>

                                    <div>
                                        <!-- Số sao đánh giá và lượt mua -->
                                        <div class="flex items-center gap-1.5 text-xs text-slate-500 pt-1">
                                            <div class="flex items-center text-amber-400 text-xs">
                                                <i class="fa-solid fa-star"></i>
                                                <span class="font-bold text-slate-800 ml-1" x-text="sim.rating || 5.0"></span>
                                            </div>
                                            <span class="text-slate-300">•</span>
                                            <span class="text-[11px] text-slate-400" x-text="(sim.sold || 96) + ' đã bán'"></span>
                                        </div>

                                        <!-- Giá bán khuyến mãi (nổi bật, màu cam/đỏ) + Giá gốc gạch ngang + Nút Icon Giỏ hàng thao tác nhanh -->
                                        <div class="pt-2 flex items-center justify-between border-t border-slate-100 mt-2">
                                            <div>
                                                <div class="text-sm sm:text-base font-extrabold text-[#F97316]" x-text="formatCurrency(sim.price)"></div>
                                                <div class="text-[10px] text-slate-400 line-through font-medium" x-text="formatCurrency(sim.originalPrice || Math.round(sim.price * 1.25))"></div>
                                            </div>
                                            <button @click.stop="addToCart({ id: sim.id, name: sim.name, price: sim.price, image: sim.image || sim.img, weight: '3kg', flavor: 'Vị chuẩn' })" class="w-9 h-9 rounded-full bg-orange-50 text-[#F97316] hover:bg-[#F97316] hover:text-white transition flex items-center justify-center shadow-sm transform active:scale-90" title="Thêm vào giỏ hàng">
                                                <i class="fa-solid fa-cart-plus text-xs"></i>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>
                </div>
            </div>

            <!-- TAB 3: DỊCH VỤ (CHĂM SÓC & Y TẾ 5 SAO THEO YÊU CẦU) -->
            <!-- ======================================================== -->
            <div x-show="activeCustomerTab === 'booking'" class="space-y-8" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                
                <!-- Header Dịch vụ: Banner giới thiệu "Dịch Vụ Chăm Sóc & Y Tế Thú Cưng Chuyên Nghiệp - Tiêu chuẩn 5 Sao" -->
                <div class="bg-gradient-to-r from-teal-700 via-brand-700 to-indigo-800 rounded-3xl p-6 sm:p-8 text-white shadow-xl relative overflow-hidden">
                    <div class="relative z-10 max-w-3xl space-y-3">
                        <div class="flex items-center gap-2">
                            <span class="bg-amber-400 text-slate-900 text-xs font-black px-3 py-1 rounded-full uppercase tracking-wider">Tiêu chuẩn quốc tế 5 sao</span>
                            <span class="bg-white/20 text-white text-xs font-semibold px-2.5 py-0.5 rounded-full">Phòng vô trùng & Bác sĩ thú y trực</span>
                        </div>
                        <h2 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold tracking-tight">Dịch Vụ Chăm Sóc & Y Tế Thú Cưng Chuyên Nghiệp</h2>
                        <p class="text-brand-100 text-xs sm:text-sm leading-relaxed">Hệ thống phòng Grooming thủy lực, Khách sạn thú cưng cách âm điều hòa 2 chiều và Dịch vụ Y tế tại nhà PetCare Home Visit chu đáo, chuyên nghiệp.</p>
                        <div class="pt-2 flex flex-wrap gap-4 text-xs text-brand-200">
                            <span class="flex items-center gap-1.5"><i class="fa-solid fa-check text-amber-400"></i> Bác sĩ thú y hơn 8 năm kinh nghiệm</span>
                            <span class="flex items-center gap-1.5"><i class="fa-solid fa-check text-amber-400"></i> Mỹ phẩm thảo mộc nhập khẩu an toàn</span>
                            <span class="flex items-center gap-1.5"><i class="fa-solid fa-check text-amber-400"></i> Camera Live Stream 24/7 xem tận mắt</span>
                        </div>
                    </div>
                </div>

                <!-- Khối Chọn Nhanh Dịch Vụ (Tab Selector: 3 Tab chính) -->
                <div class="bg-white rounded-2xl p-2 border border-slate-200 shadow-sm flex flex-wrap gap-2">
                    <button @click="servicePricingTab = 'grooming'; syncPetBookingDetails(serviceBookingForm.petId)" :class="(servicePricingTab === 'grooming' || servicePricingTab === 'spa') ? 'bg-[#F97316] text-white font-bold shadow-md shadow-orange-500/20' : 'text-slate-600 hover:bg-slate-100'" class="flex-1 py-3 px-4 rounded-xl text-xs sm:text-sm transition flex items-center justify-center gap-2">
                        <i class="fa-solid fa-scissors"></i>
                        <span>Grooming & Spa</span>
                    </button>
                    <button @click="servicePricingTab = 'hotel'; syncPetBookingDetails(serviceBookingForm.petId)" :class="servicePricingTab === 'hotel' ? 'bg-[#F97316] text-white font-bold shadow-md shadow-orange-500/20' : 'text-slate-600 hover:bg-slate-100'" class="flex-1 py-3 px-4 rounded-xl text-xs sm:text-sm transition flex items-center justify-center gap-2">
                        <i class="fa-solid fa-hotel"></i>
                        <span>Pet Hotel 5 Sao</span>
                    </button>
                    <button @click="servicePricingTab = 'vaccine'; syncPetBookingDetails(serviceBookingForm.petId)" :class="servicePricingTab === 'vaccine' ? 'bg-[#F97316] text-white font-bold shadow-md shadow-orange-500/20' : 'text-slate-600 hover:bg-slate-100'" class="flex-1 py-3 px-4 rounded-xl text-xs sm:text-sm transition flex items-center justify-center gap-2">
                        <i class="fa-solid fa-syringe"></i>
                        <span>Tiêm Phòng & Home Visit</span>
                    </button>
                </div>

                <!-- BẢNG GIÁ DỊCH VỤ CHI TIẾT (PRICING MATRIX SECTION) - CHÍNH XÁC THEO 3 ẢNH THỰC TẾ -->
                <div class="space-y-6">

                    <!-- ========================================== -->
                    <!-- TAB 1: GROOMING & SPA (BẢNG GIÁ TƯƠNG TÁC TÙNG Ô GIÁ) -->
                    <!-- ========================================== -->
                    <div x-show="servicePricingTab === 'grooming' || servicePricingTab === 'spa'" class="space-y-6 animate-fadeIn">
                        
                        <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-6">
                            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-slate-100 gap-2">
                                <div>
                                    <div class="inline-flex items-center gap-2 bg-rose-50 text-rose-600 font-extrabold text-[11px] px-3 py-1 rounded-full uppercase tracking-wider mb-1">
                                        <i class="fa-solid fa-sparkles"></i> Bảng Giá Dịch Vụ Minh Bạch (Click chọn ô giá để đặt lịch)
                                    </div>
                                    <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">SERVICES PRICE LIST (Grooming & Spa)</h3>
                                    <p class="text-xs text-slate-500">Tùy biến tick chọn 'Spa' (Có/Không) và chọn 1 trong 2 gói 'Grooming' hoặc 'Shave' (Bắt buộc chọn 1 nếu không chọn Spa)</p>
                                </div>
                                <span class="text-xs bg-emerald-50 text-emerald-700 font-bold px-3 py-1.5 rounded-xl border border-emerald-200 self-start sm:self-auto">Mỹ phẩm Davis Mỹ 100%</span>
                            </div>

                            <!-- BẢNG ĐIỀU KHIỂN TÙY CHỌN GÓI (CHECKBOX SPA ĐỘC LẬP & RADIO GROOMING/SHAVE) -->
                            <div class="p-4 bg-orange-50/80 rounded-2xl border border-orange-200/80 flex flex-col md:flex-row md:items-center justify-between gap-4">
                                <div class="space-y-1">
                                    <div class="flex items-center gap-2 flex-wrap">
                                        <span class="text-xs font-black uppercase text-orange-900 tracking-wider flex items-center gap-1.5">
                                            <i class="fa-solid fa-sliders text-[#F97316]"></i> Tùy biến gói cho mốc <span class="text-orange-600 font-extrabold" x-text="currentPetGroomingTier"></span>:
                                        </span>
                                        <span class="text-[10px] bg-amber-200/80 text-amber-900 font-bold px-2 py-0.5 rounded-full" x-text="'Bé ' + petBookingDetail.name"></span>
                                    </div>
                                    <p class="text-[11px] text-slate-500">Tích chọn Spa độc lập và/hoặc chọn 1 trong 2 gói Cắt Tỉa (Grooming) / Cạo Lông (Shave)</p>
                                </div>

                                <!-- Checkbox Spa và Radio Grooming/Shave -->
                                <div class="flex flex-wrap items-center gap-2 sm:gap-3">
                                    <!-- Checkbox Độc Lập: Spa Tắm Sấy -->
                                    <button type="button" @click="toggleGroomingSpa()" class="cursor-pointer select-none px-3.5 py-2 rounded-xl border transition flex items-center gap-2"
                                           :class="groomingIncludeSpa ? 'bg-orange-500 text-white border-orange-600 shadow-sm font-bold ring-2 ring-orange-300' : 'bg-white text-slate-700 border-slate-200 hover:border-orange-300 font-medium'">
                                        <div class="w-4 h-4 rounded flex items-center justify-center border"
                                             :class="groomingIncludeSpa ? 'bg-white text-[#F97316] border-white' : 'border-slate-300 bg-slate-50'">
                                            <i x-show="groomingIncludeSpa" class="fa-solid fa-check text-[10px]"></i>
                                        </div>
                                        <span class="text-xs">Spa Tắm Sấy</span>
                                    </button>

                                    <!-- Divider -->
                                    <span class="text-slate-300 hidden sm:inline">|</span>

                                    <!-- Radio Button 1: Grooming (Cắt tạo kiểu) -->
                                    <button type="button" @click="setGroomingCutType('grooming')" class="cursor-pointer select-none px-3.5 py-2 rounded-xl border transition flex items-center gap-2"
                                           :class="groomingCutType === 'grooming' ? 'bg-[#F97316] text-white border-orange-600 shadow-sm font-bold ring-2 ring-orange-300' : 'bg-white text-slate-700 border-slate-200 hover:border-orange-300 font-medium'">
                                        <div class="w-4 h-4 rounded-full flex items-center justify-center border"
                                             :class="groomingCutType === 'grooming' ? 'border-white bg-white' : 'border-slate-300 bg-slate-50'">
                                            <div x-show="groomingCutType === 'grooming'" class="w-2 h-2 rounded-full bg-[#F97316]"></div>
                                        </div>
                                        <span class="text-xs">Cắt Tỉa (Grooming)</span>
                                    </button>

                                    <!-- Radio Button 2: Shave (Cạo lông) -->
                                    <button type="button" @click="setGroomingCutType('shave')" class="cursor-pointer select-none px-3.5 py-2 rounded-xl border transition flex items-center gap-2"
                                           :class="groomingCutType === 'shave' ? 'bg-[#F97316] text-white border-orange-600 shadow-sm font-bold ring-2 ring-orange-300' : 'bg-white text-slate-700 border-slate-200 hover:border-orange-300 font-medium'">
                                        <div class="w-4 h-4 rounded-full flex items-center justify-center border"
                                             :class="groomingCutType === 'shave' ? 'border-white bg-white' : 'border-slate-300 bg-slate-50'">
                                            <div x-show="groomingCutType === 'shave'" class="w-2 h-2 rounded-full bg-[#F97316]"></div>
                                        </div>
                                        <span class="text-xs">Cạo Lông (Shave)</span>
                                    </button>

                                    <!-- Radio Button 3: Không cắt/cạo (Chỉ khả dụng khi đã chọn Spa) -->
                                    <button type="button" x-show="groomingIncludeSpa" @click="setGroomingCutType('none')" class="cursor-pointer select-none px-3 py-2 rounded-xl border transition flex items-center gap-1.5"
                                           :class="groomingCutType === 'none' ? 'bg-slate-700 text-white border-slate-800 shadow-sm font-bold' : 'bg-white text-slate-600 border-slate-200 hover:border-slate-300 text-xs'">
                                        <div class="w-3.5 h-3.5 rounded-full flex items-center justify-center border"
                                             :class="groomingCutType === 'none' ? 'border-white bg-white' : 'border-slate-300 bg-slate-50'">
                                            <div x-show="groomingCutType === 'none'" class="w-1.5 h-1.5 rounded-full bg-slate-800"></div>
                                        </div>
                                        <span class="text-xs">Chỉ làm Spa</span>
                                    </button>
                                </div>
                            </div>

                            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                                
                                <!-- Bảng Giá Chính (Weight / Spa / Grooming / Shave) - Chiếm 2 Cột -->
                                <div class="lg:col-span-2 overflow-x-auto border border-slate-200 rounded-2xl shadow-sm bg-white">
                                    <table class="w-full text-left text-xs sm:text-sm border-collapse">
                                        <thead>
                                            <tr class="bg-gradient-to-r from-rose-50 to-orange-50 text-slate-900 border-b border-slate-200 font-black">
                                                <th class="py-3 px-4">Weight (Cân nặng)</th>
                                                <th class="py-3 px-4 text-center">Spa<br><span class="text-[10px] font-normal text-slate-500">(Tắm sấy vệ sinh)</span></th>
                                                <th class="py-3 px-4 text-center">Grooming<br><span class="text-[10px] font-normal text-slate-500">(Spa + Cắt tạo kiểu)</span></th>
                                                <th class="py-3 px-4 text-center">Shave<br><span class="text-[10px] font-normal text-slate-500">(Spa + Cạo lông)</span></th>
                                            </tr>
                                        </thead>
                                        <tbody class="divide-y divide-slate-100 font-medium text-slate-800">
                                            <template x-for="(row, ridx) in groomingPriceList" :key="ridx">
                                                <tr :class="currentPetGroomingTier === row.weight ? 'bg-amber-50/50' : ''" class="transition">
                                                    <td class="py-3.5 px-4 font-bold text-slate-900">
                                                        <div class="flex items-center gap-1.5 flex-wrap">
                                                            <span class="text-sm font-black text-slate-900" x-text="row.weight"></span>
                                                            <span x-show="currentPetGroomingTier === row.weight" class="text-[10px] font-bold bg-amber-100 text-amber-800 border border-amber-200 px-2 py-0.5 rounded-full inline-flex items-center gap-1 shadow-xs">
                                                                <i class="fa-solid fa-star text-amber-500"></i>Gợi ý cho <span x-text="petBookingDetail.name"></span>
                                                            </span>
                                                        </div>
                                                    </td>
                                                    
                                                    <!-- Ô giá Spa (Clickable cell) -->
                                                    <td @click="selectGroomingCell(row, 'spa')"
                                                        class="py-3 px-4 text-center cursor-pointer transition-all rounded-xl m-1"
                                                        :class="isGroomingCellSelected(row.weight, 'spa') ? 'bg-orange-100/90 text-orange-900 border-2 border-[#F97316] font-black ring-2 ring-orange-400/30 shadow-sm' : 'hover:bg-orange-50/60 text-slate-700 font-semibold border border-transparent'"
                                                        title="Click để chọn/bỏ chọn Spa cho mốc cân nặng này">
                                                        <div class="flex items-center justify-center gap-1.5">
                                                            <span class="w-4 h-4 rounded border flex items-center justify-center text-[10px]"
                                                                  :class="isGroomingCellSelected(row.weight, 'spa') ? 'bg-[#F97316] text-white border-[#F97316]' : 'border-slate-300 text-transparent'">
                                                                <i class="fa-solid fa-check"></i>
                                                            </span>
                                                            <span x-text="formatCurrency(row.spa)"></span>
                                                        </div>
                                                    </td>

                                                    <!-- Ô giá Grooming (Clickable cell) -->
                                                    <td @click="selectGroomingCell(row, 'grooming')"
                                                        class="py-3 px-4 text-center cursor-pointer transition-all rounded-xl m-1"
                                                        :class="isGroomingCellSelected(row.weight, 'grooming') ? 'bg-orange-100/90 text-orange-900 border-2 border-[#F97316] font-black ring-2 ring-orange-400/30 shadow-sm' : 'hover:bg-orange-50/60 text-slate-800 font-extrabold border border-transparent'"
                                                        title="Click để chọn gói Grooming (Cắt tạo kiểu)">
                                                        <div class="flex items-center justify-center gap-1.5">
                                                            <span class="w-3.5 h-3.5 rounded-full border flex items-center justify-center"
                                                                  :class="isGroomingCellSelected(row.weight, 'grooming') ? 'border-[#F97316] bg-white' : 'border-slate-300'">
                                                                <span x-show="isGroomingCellSelected(row.weight, 'grooming')" class="w-2 h-2 rounded-full bg-[#F97316]"></span>
                                                            </span>
                                                            <span x-text="formatCurrency(row.grooming)"></span>
                                                        </div>
                                                    </td>

                                                    <!-- Ô giá Shave (Clickable cell) -->
                                                    <td @click="selectGroomingCell(row, 'shave')"
                                                        class="py-3 px-4 text-center cursor-pointer transition-all rounded-xl m-1"
                                                        :class="isGroomingCellSelected(row.weight, 'shave') ? 'bg-orange-100/90 text-orange-900 border-2 border-[#F97316] font-black ring-2 ring-orange-400/30 shadow-sm' : 'hover:bg-orange-50/60 text-slate-600 font-semibold border border-transparent'"
                                                        title="Click để chọn gói Shave (Cạo lông)">
                                                        <div class="flex items-center justify-center gap-1.5">
                                                            <span class="w-3.5 h-3.5 rounded-full border flex items-center justify-center"
                                                                  :class="isGroomingCellSelected(row.weight, 'shave') ? 'border-[#F97316] bg-white' : 'border-slate-300'">
                                                                <span x-show="isGroomingCellSelected(row.weight, 'shave')" class="w-2 h-2 rounded-full bg-[#F97316]"></span>
                                                            </span>
                                                            <span x-text="formatCurrency(row.shave)"></span>
                                                        </div>
                                                    </td>
                                                </tr>
                                            </template>
                                        </tbody>
                                    </table>
                                </div>

                                <!-- Cột Phụ: OTHER SERVICES & BEAUTY PACKAGE (Theo Ảnh 2) -->
                                <div class="space-y-4">
                                    <!-- OTHER SERVICES (Dịch vụ lẻ khác) -->
                                    <div class="bg-slate-50 rounded-2xl p-4 sm:p-5 border border-slate-200 space-y-3">
                                        <h4 class="font-black text-xs sm:text-sm text-slate-900 uppercase tracking-wider flex items-center justify-between">
                                            <span>OTHER SERVICES (Dịch vụ lẻ)</span>
                                            <i class="fa-solid fa-list-check text-rose-500"></i>
                                        </h4>
                                        <div class="space-y-2 text-xs">
                                            <template x-for="(srv, sidx) in otherServicesList" :key="sidx">
                                                <div class="flex justify-between items-start gap-3 pb-2 border-b border-slate-200/60 last:border-0" style="display: flex; justify-content: space-between; align-items: flex-start;">
                                                    <span class="flex-1 text-slate-700 font-medium leading-snug break-words text-left" x-text="srv.name"></span>
                                                    <span class="min-w-[110px] text-right flex-shrink-0 font-bold text-slate-900" style="min-width: 110px; text-align: right;" x-text="srv.price"></span>
                                                </div>
                                            </template>
                                        </div>
                                    </div>

                                    <!-- BEAUTY PACKAGE (Gói tắm tháng) -->
                                    <div class="bg-gradient-to-br from-rose-500 to-orange-500 text-white rounded-2xl p-4 sm:p-5 shadow-md space-y-2">
                                        <div class="flex items-center justify-between">
                                            <span class="text-[10px] font-bold bg-white/20 px-2 py-0.5 rounded-full uppercase tracking-wider">Ưu Đãi Đặc Biệt</span>
                                            <i class="fa-solid fa-crown text-amber-300"></i>
                                        </div>
                                        <h4 class="font-black text-sm sm:text-base">BEAUTY PACKAGE (Gói Tắm Tháng)</h4>
                                        <div class="flex items-baseline justify-between pt-1">
                                            <span class="text-xs font-semibold">10 Buổi Spa Chăm Sóc</span>
                                            <span class="text-lg font-black bg-white text-rose-600 px-2.5 py-0.5 rounded-xl shadow-sm">OFF 15%</span>
                                        </div>
                                        <p class="text-[10px] text-white/90 italic">*Valid within 90 days (Sử dụng trong vòng 90 ngày kể từ ngày kích hoạt)</p>
                                    </div>
                                </div>
                            </div>

                            <!-- Điều Khoản Áp Dụng (Terms and Conditions theo Ảnh 2) -->
                            <div class="bg-slate-50/80 rounded-2xl p-4 border border-slate-200 text-xs text-slate-600 space-y-1.5">
                                <h5 class="font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                                    <i class="fa-solid fa-circle-info text-brand-600"></i>
                                    <span>TERMS AND CONDITIONS / ĐIỀU KHOẢN ÁP DỤNG:</span>
                                </h5>
                                <ul class="grid grid-cols-1 md:grid-cols-2 gap-2 pt-1 text-[11px] leading-relaxed">
                                    <li>• Vui lòng đặt hẹn trước 1 ngày để được phục vụ chu đáo nhất (Booking 1 day in advance is recommended).</li>
                                    <li>• PetCare360 có quyền từ chối nhận các bé quá hung dữ, không hợp tác (Pet that's too aggressive might be returned).</li>
                                    <li>• Phí dịch vụ không thể hoàn lại hoặc chuyển nhượng cho người khác (Service fee is non-refundable and non-exchangeable).</li>
                                    <li>• Phí dịch vụ có thể được điều chỉnh nhẹ vào các dịp Lễ Tết theo quy định chung.</li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <!-- TAB 2: PET HOTEL 5 SAO (BẢNG GIÁ TƯƠNG TÁC CHỌN GÓI POPUP) -->
                    <!-- ========================================== -->
                    <div x-show="servicePricingTab === 'hotel'" class="space-y-6 animate-fadeIn">
                        
                        <!-- Khối Bảng Giá Khách Sạn Thú Cưng Tiêu Chuẩn 5 Sao (Chung Cho Cả Chó & Mèo Theo Cân Nặng) -->
                        <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-6">
                            
                            <!-- Header Bảng Giá -->
                            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-slate-100 gap-2">
                                <div>
                                    <div class="inline-flex items-center gap-2 bg-orange-50 text-orange-600 font-extrabold text-[11px] px-3 py-1 rounded-full uppercase tracking-wider mb-1">
                                        <i class="fa-solid fa-hotel"></i> Khách Sạn Thú Cưng Tiêu Chuẩn 5 Sao
                                    </div>
                                    <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">SERVICES PRICE LIST (Pet Hotel 5 Sao)</h3>
                                    <p class="text-xs text-slate-500">Phòng Tiêu Chuẩn 5 Sao dùng chung cho cả Chó & Mèo — Bấm 'Chọn Đặt Lịch' để chọn Lưu Trú Qua Đêm hoặc Bán Trú Daycare</p>
                                </div>
                                <div class="flex items-center gap-2 self-start sm:self-auto">
                                    <span class="text-xs bg-emerald-50 text-emerald-700 font-bold px-3 py-1.5 rounded-xl border border-emerald-200 flex items-center gap-1.5 shadow-sm">
                                        <i class="fa-solid fa-circle-check text-emerald-600"></i>
                                        <span>1 Hạng Phòng Tiêu Chuẩn Duy Nhất</span>
                                    </span>
                                </div>
                            </div>

                            <!-- BỐ CỤC 3 CỘT (TƯƠNG TỰ TAB GROOMING & SPA) -->
                            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                                
                                <!-- Bảng Giá Chính Theo Cân Nặng (Chiếm 2 Cột) -->
                                <div class="lg:col-span-2 overflow-x-auto border border-slate-200 rounded-2xl shadow-sm bg-white">
                                    <table class="w-full text-left text-xs sm:text-sm border-collapse">
                                        <thead>
                                            <tr class="bg-gradient-to-r from-orange-50 to-amber-50 text-slate-900 border-b border-slate-200 font-black">
                                                <th class="py-3.5 px-4">Phân Hạng Kích Thước (Size)</th>
                                                <th class="py-3.5 px-4 text-center">Gói Dịch Vụ & Thời Gian</th>
                                                <th class="py-3.5 px-4 text-center">Mức Giá Niêm Yết</th>
                                                <th class="py-3.5 px-4 text-center">Thao Tác</th>
                                            </tr>
                                        </thead>
                                        <tbody class="divide-y divide-slate-100 font-medium text-slate-800">
                                            <template x-for="(plan, pidx) in petHotelWeightPriceList" :key="pidx">
                                                <tr :class="(selectedBaseService && selectedBaseService.category === 'hotel' && selectedBaseService.weightTier === plan.size) ? 'bg-orange-50/90 font-bold ring-2 ring-inset ring-[#F97316] border-l-4 border-l-[#F97316]' : (currentPetHotelTier === plan.size ? 'bg-amber-50/40 hover:bg-orange-50/40' : 'hover:bg-orange-50/40')"
                                                    class="transition-all relative">
                                                    
                                                    <td class="py-3.5 px-4 font-black text-slate-900">
                                                        <div class="flex items-center gap-2 flex-wrap">
                                                            <span class="w-2.5 h-2.5 rounded-full bg-[#F97316]"></span>
                                                            <span class="text-sm font-black text-slate-900" x-text="plan.size"></span>
                                                            <span x-show="currentPetHotelTier === plan.size" class="text-[10px] font-bold bg-amber-100 text-amber-800 border border-amber-200 px-2 py-0.5 rounded-full inline-flex items-center gap-1 shadow-xs">
                                                                <i class="fa-solid fa-star text-amber-500"></i>Gợi ý cho <span x-text="petBookingDetail.name"></span>
                                                            </span>
                                                            <span x-show="selectedBaseService && selectedBaseService.category === 'hotel' && selectedBaseService.weightTier === plan.size" class="text-[10px] font-black uppercase tracking-wider bg-orange-500 text-white px-2 py-0.5 rounded-full shadow-xs">
                                                                <span x-text="'Đang chọn: ' + (selectedBaseService.type === 'overnight' ? 'Qua Đêm 24h' : 'Daycare')"></span>
                                                            </span>
                                                        </div>
                                                        <div class="text-[11px] font-normal text-slate-500 mt-1 ml-4.5 max-w-xs" x-text="plan.desc"></div>
                                                    </td>

                                                    <td class="py-3.5 px-4 text-center">
                                                        <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-xl bg-slate-100 text-slate-700 font-bold text-xs">
                                                            <i class="fa-regular fa-clock text-orange-500"></i>
                                                            <span>Lưu trú 24h & Daycare</span>
                                                        </span>
                                                    </td>

                                                    <td class="py-3.5 px-4 text-center">
                                                        <div class="font-black text-[#F97316] text-sm sm:text-base">
                                                            Qua đêm: <span x-text="formatCurrency(plan.price)"></span>
                                                        </div>
                                                        <div class="text-[11px] text-slate-500 font-medium mt-0.5">
                                                            Daycare: <span x-text="formatCurrency(plan.daycarePrice)"></span>
                                                        </div>
                                                    </td>

                                                    <td class="py-3.5 px-4 text-center relative">
                                                        <div class="relative inline-block text-left">
                                                            <button type="button" @click.stop="hotelPopupRow = (hotelPopupRow === plan.size ? null : plan.size)" class="px-3.5 py-1.5 rounded-xl font-bold text-xs transition shadow-sm flex items-center justify-center gap-1.5 mx-auto"
                                                                    :class="(selectedBaseService && selectedBaseService.category === 'hotel' && selectedBaseService.weightTier === plan.size) ? 'bg-[#F97316] text-white shadow-orange-500/30 ring-2 ring-orange-300' : 'bg-orange-100 text-orange-700 hover:bg-[#F97316] hover:text-white'">
                                                                <i :class="(selectedBaseService && selectedBaseService.category === 'hotel' && selectedBaseService.weightTier === plan.size) ? 'fa-solid fa-circle-check' : 'fa-solid fa-calendar-plus'" class="text-[11px]"></i>
                                                                <span x-text="(selectedBaseService && selectedBaseService.category === 'hotel' && selectedBaseService.weightTier === plan.size) ? 'Đang Áp Dụng' : 'Chọn Đặt Lịch'"></span>
                                                                <i class="fa-solid fa-chevron-down text-[9px] ml-0.5"></i>
                                                            </button>

                                                            <!-- Popup Dropdown Options -->
                                                            <div x-show="hotelPopupRow === plan.size" @click.away="hotelPopupRow = null" class="absolute right-0 top-full mt-2 w-64 bg-white rounded-2xl shadow-xl border border-orange-200 p-3 z-30 space-y-2 animate-fadeIn text-left">
                                                                <div class="text-[11px] font-bold text-slate-500 uppercase tracking-wider pb-1.5 border-b border-slate-100 flex items-center justify-between">
                                                                    <span>Chọn gói (Size <span x-text="plan.size"></span>):</span>
                                                                    <button @click.stop="hotelPopupRow = null" class="text-slate-400 hover:text-slate-600"><i class="fa-solid fa-xmark"></i></button>
                                                                </div>
                                                                
                                                                <!-- Option 1: Lưu Trú Qua Đêm (24h) -->
                                                                <button type="button" @click.stop="selectHotelOption(plan, 'overnight')" class="w-full text-left p-2.5 rounded-xl border transition flex items-center justify-between group hover:bg-orange-50 hover:border-orange-400"
                                                                        :class="(selectedBaseService && selectedBaseService.category === 'hotel' && selectedBaseService.weightTier === plan.size && selectedBaseService.type === 'overnight') ? 'bg-orange-100/80 border-[#F97316] ring-1 ring-[#F97316]' : 'bg-slate-50 border-slate-200'">
                                                                    <div>
                                                                        <div class="font-bold text-xs text-slate-900 group-hover:text-orange-600 flex items-center gap-1.5">
                                                                            <i class="fa-solid fa-moon text-indigo-500 text-[11px]"></i>
                                                                            <span>Lưu Trú Qua Đêm</span>
                                                                        </div>
                                                                        <div class="text-[10px] text-slate-500">24h trọn gói, 3 bữa ăn</div>
                                                                    </div>
                                                                    <div class="font-black text-xs text-orange-600" x-text="formatCurrency(plan.price)"></div>
                                                                </button>

                                                                <!-- Option 2: Bán Trú Daycare (Trong Ngày) -->
                                                                <button type="button" @click.stop="selectHotelOption(plan, 'daycare')" class="w-full text-left p-2.5 rounded-xl border transition flex items-center justify-between group hover:bg-orange-50 hover:border-orange-400"
                                                                        :class="(selectedBaseService && selectedBaseService.category === 'hotel' && selectedBaseService.weightTier === plan.size && selectedBaseService.type === 'daycare') ? 'bg-orange-100/80 border-[#F97316] ring-1 ring-[#F97316]' : 'bg-slate-50 border-slate-200'">
                                                                    <div>
                                                                        <div class="font-bold text-xs text-slate-900 group-hover:text-orange-600 flex items-center gap-1.5">
                                                                            <i class="fa-solid fa-sun text-amber-500 text-[11px]"></i>
                                                                            <span>Bán Trú Daycare</span>
                                                                        </div>
                                                                        <div class="text-[10px] text-slate-500">09:00 - 19:00 trong ngày</div>
                                                                    </div>
                                                                    <div class="font-black text-xs text-orange-600" x-text="formatCurrency(plan.daycarePrice)"></div>
                                                                </button>
                                                            </div>
                                                        </div>
                                                    </td>
                                                </tr>
                                            </template>
                                        </tbody>
                                    </table>
                                </div>

                                <!-- Cột Phụ: TIỆN ÍCH TIÊU CHUẨN 5 SAO & ƯU ĐÃI DÀI HẠN (Chiếm 1 Cột) -->
                                <div class="space-y-4">
                                    <!-- TIÊU CHUẨN PHÒNG TIÊU CHUẨN 5 SAO DÙNG CHUNG CẢ CHÓ & MÈO -->
                                    <div class="bg-slate-50 rounded-2xl p-4 sm:p-5 border border-slate-200 space-y-3">
                                        <h4 class="font-black text-xs sm:text-sm text-slate-900 uppercase tracking-wider flex items-center justify-between">
                                            <span>TIỆN ÍCH PHÒNG TIÊU CHUẨN 5 SAO</span>
                                            <i class="fa-solid fa-hotel text-[#F97316]"></i>
                                        </h4>
                                        <p class="text-[11px] text-slate-500">Khách sạn tiêu chuẩn 5 sao dùng chung cho cả Chó & Mèo với hệ thống chăm sóc cao cấp:</p>
                                        <ul class="space-y-2 text-xs text-slate-700 font-medium">
                                            <li class="flex items-start gap-2">
                                                <i class="fa-solid fa-snowflake text-[#F97316] mt-0.5 text-xs"></i>
                                                <span>Điều hòa 2 chiều 25-26°C & Khử khuẩn tiệt trùng tia cực tím UV-C mỗi ngày.</span>
                                            </li>
                                            <li class="flex items-start gap-2">
                                                <i class="fa-solid fa-video text-[#F97316] mt-0.5 text-xs"></i>
                                                <span>Camera HD PetShow360 quan sát trực tuyến 24/7 trực tiếp trên điện thoại.</span>
                                            </li>
                                            <li class="flex items-start gap-2">
                                                <i class="fa-solid fa-bowl-food text-[#F97316] mt-0.5 text-xs"></i>
                                                <span>3 bữa ăn dinh dưỡng Royal Canin / Orijen nhập khẩu + Pate & Gel tráng miệng.</span>
                                            </li>
                                            <li class="flex items-start gap-2">
                                                <i class="fa-solid fa-tree text-[#F97316] mt-0.5 text-xs"></i>
                                                <span>2 cữ ra sân cỏ tự nhiên chạy nhảy, tương tác bắt bóng và chải lông thư giãn.</span>
                                            </li>
                                            <li class="flex items-start gap-2">
                                                <i class="fa-solid fa-shield-cat text-[#F97316] mt-0.5 text-xs"></i>
                                                <span>Khay cát vệ sinh riêng cho mèo, đệm lót nệm êm ái tiệt trùng hàng ngày.</span>
                                            </li>
                                        </ul>
                                    </div>

                                    <!-- ƯU ĐÃI LƯU TRÚ DÀI HẠN -->
                                    <div class="bg-gradient-to-br from-amber-50 to-orange-50 border border-orange-200 rounded-2xl p-4 sm:p-5 space-y-3">
                                        <h4 class="font-black text-xs sm:text-sm text-slate-900 uppercase tracking-wider flex items-center justify-between">
                                            <span>ƯU ĐÃI LƯU TRÚ DÀI HẠN</span>
                                            <i class="fa-solid fa-tags text-[#F97316]"></i>
                                        </h4>
                                        <div class="grid grid-cols-3 gap-2 text-center">
                                            <div class="bg-white/80 rounded-xl p-2.5 border border-orange-200/60 space-y-0.5">
                                                <span class="text-[10px] font-bold text-slate-600 block">1 TUẦN</span>
                                                <span class="text-sm font-black text-orange-600 block">GIẢM 10%</span>
                                                <span class="text-[9px] text-slate-400 block">Tự động trừ</span>
                                            </div>
                                            <div class="bg-white/80 rounded-xl p-2.5 border border-orange-200/60 space-y-0.5">
                                                <span class="text-[10px] font-bold text-slate-600 block">2 TUẦN</span>
                                                <span class="text-sm font-black text-orange-600 block">GIẢM 15%</span>
                                                <span class="text-[9px] text-slate-400 block">Tặng đồ chơi</span>
                                            </div>
                                            <div class="bg-gradient-to-br from-rose-500 to-orange-500 text-white rounded-xl p-2.5 shadow-sm space-y-0.5">
                                                <span class="text-[10px] font-bold text-white/90 block">1 THÁNG</span>
                                                <span class="text-sm font-black block">GIẢM 20%</span>
                                                <span class="text-[9px] text-white/80 block">+ TẶNG SPA</span>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- QUY ĐỊNH GIỜ GIẤC CHECK-IN / CHECK-OUT -->
                                    <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 text-xs space-y-2 text-slate-600">
                                        <h5 class="font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                                            <i class="fa-solid fa-clock text-[#F97316]"></i>
                                            <span>QUY ĐỊNH CHECK-IN / CHECK-OUT:</span>
                                        </h5>
                                        <ul class="space-y-1.5 text-[11px] leading-relaxed">
                                            <li>• <strong>Giờ check-in:</strong> Bắt đầu từ 09:00 AM mỗi ngày.</li>
                                            <li>• <strong>Giờ check-out:</strong> Trước 11:00 AM hôm sau (sau 11:00 AM tính phí bán trú Daycare).</li>
                                            <li>• <strong>PetShip360:</strong> Hỗ trợ xe chuyên dụng đưa đón tận nhà 2 chiều.</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- ========================================== -->
                    <!-- TAB 3: TIÊM PHÒNG & HOME VISIT (HÀNG CLICKABLE & CỘT THAO TÁC) -->
                    <!-- ========================================== -->
                    <div x-show="servicePricingTab === 'vaccine'" class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-6 animate-fadeIn">
                        <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-slate-100 gap-2">
                            <div>
                                <div class="inline-flex items-center gap-2 bg-blue-50 text-blue-600 font-extrabold text-[11px] px-3 py-1 rounded-full uppercase tracking-wider mb-1">
                                    <i class="fa-solid fa-syringe"></i> Dịch Vụ Thú Y Tận Tâm Chuẩn Quốc Tế
                                </div>
                                <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Bảng Giá Tiêm Phòng & Bác Sĩ Khám Tận Nhà (Home Visit)</h3>
                                <p class="text-xs text-slate-500">Bấm trực tiếp vào từng hàng hoặc bấm 'Chọn Đặt Lịch' để đặt lịch hẹn bác sĩ thú y</p>
                            </div>
                            <span class="text-xs bg-blue-50 text-blue-700 font-bold px-3 py-1.5 rounded-xl border border-blue-200 self-start sm:self-auto">Cấp Sổ Tiêm Quốc Tế</span>
                        </div>

                        <div class="overflow-x-auto border border-slate-200 rounded-2xl shadow-sm bg-white">
                            <table class="w-full text-left text-xs sm:text-sm border-collapse">
                                <thead>
                                    <tr class="bg-blue-50/70 text-slate-900 border-b border-slate-200 font-black">
                                        <th class="py-3.5 px-4">Gói Tiêm Chủng / Dịch Vụ Y Tế</th>
                                        <th class="py-3.5 px-4">Thời Gian</th>
                                        <th class="py-3.5 px-4">Quy Trình Chuẩn Bác Sĩ Thú Y</th>
                                        <th class="py-3.5 px-4 text-center">Chi Phí Niêm Yết</th>
                                        <th class="py-3.5 px-4 text-center">Thao Tác</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-100 font-medium text-slate-800">
                                    <template x-for="(vac, vidx) in vaccinePriceList" :key="vidx">
                                        <tr @click="selectVaccineRow(vac)"
                                            class="cursor-pointer transition"
                                            :class="(selectedBaseService && selectedBaseService.category === 'vaccine' && selectedBaseService.name === vac.name) ? 'bg-blue-50/90 font-bold ring-2 ring-inset ring-blue-500 border-l-4 border-l-blue-500' : 'hover:bg-blue-50/30'">
                                            
                                            <td class="py-3.5 px-4 font-bold text-slate-900">
                                                <div class="flex items-center gap-2 flex-wrap">
                                                    <span x-text="vac.name"></span>
                                                    <span x-show="selectedBaseService && selectedBaseService.category === 'vaccine' && selectedBaseService.name === vac.name" class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-blue-600 text-white shadow-xs">
                                                        Đang chọn gói này
                                                    </span>
                                                </div>
                                            </td>
                                            <td class="py-3.5 px-4 text-slate-500" x-text="vac.duration"></td>
                                            <td class="py-3.5 px-4 text-xs text-slate-600 max-w-md" x-text="vac.desc"></td>
                                            <td class="py-3.5 px-4 text-center font-extrabold text-[#F97316] text-sm sm:text-base" x-text="formatCurrency(vac.price)"></td>
                                            <td class="py-3.5 px-4 text-center">
                                                <button type="button" @click.stop="selectVaccineRow(vac)" class="px-3.5 py-1.5 rounded-xl font-bold text-xs transition shadow-sm flex items-center justify-center gap-1.5 mx-auto"
                                                        :class="(selectedBaseService && selectedBaseService.category === 'vaccine' && selectedBaseService.name === vac.name) ? 'bg-blue-600 text-white shadow-blue-500/30 ring-2 ring-blue-300' : 'bg-blue-100 text-blue-700 hover:bg-blue-600 hover:text-white'">
                                                    <i :class="(selectedBaseService && selectedBaseService.category === 'vaccine' && selectedBaseService.name === vac.name) ? 'fa-solid fa-circle-check' : 'fa-solid fa-calendar-plus'" class="text-[11px]"></i>
                                                    <span x-text="(selectedBaseService && selectedBaseService.category === 'vaccine' && selectedBaseService.name === vac.name) ? 'Đã Chọn' : 'Chọn Đặt Lịch'"></span>
                                                </button>
                                            </td>
                                        </tr>
                                    </template>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

                <!-- KHỐI FORM ĐẶT LỊCH GIỮ CHỖ (BOOKING FORM BOX - 6 BƯỚC) -->
                <div id="pet-service-booking-box" class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-6">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-slate-100 gap-2">
                        <div>
                            <h3 class="text-xl font-bold text-slate-900">Phiếu Đặt Lịch & Giữ Chỗ Trực Tuyến</h3>
                            <p class="text-xs text-slate-500">Hoàn thành các bước để kiểm tra slot phòng và tính toán chi phí chính xác</p>
                        </div>
                        <!-- Nút Chỉnh sửa thông tin đặt lịch mở Modal 800px theo yêu cầu -->
                        <button @click="openPetBookingDetailModal()" class="self-start sm:self-auto px-4 py-2 bg-brand-50 hover:bg-brand-100 text-brand-700 font-bold text-xs rounded-xl border border-brand-200 transition flex items-center gap-1.5 shadow-sm">
                            <i class="fa-solid fa-file-pen text-brand-600"></i>
                            <span>Chỉnh sửa thông tin đặt lịch (Phiếu Chi Tiết 800px)</span>
                        </button>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        
                        <!-- Bước 1: Chọn Thú Cưng Từ Hồ Sơ (Auto-map cân nặng) -->
                        <div class="space-y-2">
                            <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                                Bước 1: Chọn Thú Cưng Từ Hồ Sơ
                            </label>
                            <select x-model.number="serviceBookingForm.petId" @change="syncPetBookingDetails(serviceBookingForm.petId)" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-xs sm:text-sm font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-brand-500">
                                <template x-for="p in (pets || customerProfile.pets)" :key="p.id">
                                    <option :value="p.id" x-text="p.name + ' - ' + (p.breed || p.species) + ' (' + p.weight + 'kg)'"></option>
                                </template>
                            </select>
                            <!-- Tự động hiển thị Avatar, Cân nặng, Giống loài, Trạng thái tiêm vắc-xin, Hạng Size & Giá tương ứng -->
                            <div class="p-3.5 bg-orange-50/70 rounded-2xl border border-orange-200 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
                                <div class="flex items-center gap-3">
                                    <img :src="petBookingDetail.vaccinePhoto || 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=150&q=80'" class="w-12 h-12 rounded-xl object-cover border border-orange-200 shadow-sm">
                                    <div class="text-xs">
                                        <div class="flex items-center gap-2">
                                            <h5 class="font-black text-slate-900" x-text="petBookingDetail.name + ' (' + petBookingDetail.species + ')'"></h5>
                                            <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-full">Đã tiêm vắc-xin</span>
                                        </div>
                                        <p class="text-slate-500 text-[11px] mt-0.5">Giống: <span class="font-medium text-slate-700" x-text="petBookingDetail.breed"></span> | Cân nặng: <span class="font-extrabold text-orange-600" x-text="petBookingDetail.weight + ' kg'"></span></p>
                                    </div>
                                </div>
                                <div class="flex flex-wrap sm:flex-col items-start sm:items-end gap-1.5 pt-2 sm:pt-0 border-t sm:border-t-0 border-orange-200/60 w-full sm:w-auto text-right">
                                    <div class="flex items-center gap-1">
                                        <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-rose-100 text-rose-800 font-bold text-[10px]" x-text="'Grooming: ' + currentPetGroomingTier"></span>
                                        <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-orange-100 text-orange-800 font-bold text-[10px]" x-text="'Hotel: ' + currentPetHotelTier"></span>
                                    </div>
                                    <div class="text-xs font-black text-[#F97316]" x-text="selectedBaseService ? (selectedBaseService.name + ' (' + formatCurrency(baseServicePrice) + ')') : ('Giá chuẩn: ' + formatCurrency(baseServicePrice))"></div>
                                </div>
                            </div>
                        </div>

                        <!-- Bước 2: Cố Định Chi Nhánh Chính (Xóa dropdown, thay bằng input disabled/readonly) -->
                        <div class="space-y-2">
                            <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                                Bước 2: Chi Nhánh Cố Định
                            </label>
                            <div class="relative">
                                <input type="text" value="Cơ sở Chính: 88 Nguyễn Thị Minh Khai, Quận 1, TPHCM" readonly disabled
                                       class="w-full bg-slate-100 border border-slate-300 rounded-xl px-4 py-3 text-xs sm:text-sm font-bold text-slate-700 cursor-not-allowed">
                                <span class="absolute right-3.5 top-1/2 -translate-y-1/2 text-[10px] font-bold bg-amber-100 text-amber-800 border border-amber-200 px-2.5 py-1 rounded-lg">
                                    <i class="fa-solid fa-lock mr-1"></i>Trụ Sở Chính
                                </span>
                            </div>
                            <p class="text-[11px] text-slate-400 flex items-center gap-1">
                                <i class="fa-solid fa-location-dot text-brand-600"></i>
                                <span>88 Nguyễn Thị Minh Khai, P. Bến Thành, Quận 1, TP.HCM (Khu dịch vụ 5 sao, bãi đỗ ô tô và sân cỏ ngoài trời)</span>
                            </p>
                        </div>

                        <!-- Bước 3: Chọn Ngày & Giờ (Phân tách theo loại dịch vụ) -->
                        <div class="md:col-span-2 space-y-3">
                            
                            <!-- KHỐI DÀNH RIÊNG CHO TAB PET HOTEL 5 SAO: Date Range Picker & Dropdown Giờ Check-in/Check-out -->
                            <div x-show="servicePricingTab === 'hotel'" class="space-y-3 animate-fadeIn">
                                <div class="flex items-center justify-between">
                                    <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                                        Bước 3: Chọn Khoảng Thời Gian Lưu Trú (Date Range & Giờ Nhận/Trả Pet)
                                    </label>
                                    <span class="text-[11px] font-bold bg-orange-100 text-orange-800 px-2.5 py-0.5 rounded-full border border-orange-200">
                                        Khách Sạn 5 Sao
                                    </span>
                                </div>

                                <!-- Date Range Picker: Ngày Check-in & Ngày Check-out -->
                                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 bg-orange-50/50 p-4 rounded-2xl border border-orange-200">
                                    <div>
                                        <label class="text-xs font-bold text-slate-700 block mb-1 flex items-center gap-1">
                                            <i class="fa-solid fa-calendar-check text-orange-500"></i>
                                            <span>Ngày Check-in (Nhận phòng):</span>
                                        </label>
                                        <input type="date" x-model="serviceBookingForm.hotelCheckInDate" class="w-full bg-white border border-slate-300 rounded-xl px-4 py-2.5 text-xs sm:text-sm font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-orange-500">
                                    </div>
                                    <div>
                                        <label class="text-xs font-bold text-slate-700 block mb-1 flex items-center gap-1">
                                            <i class="fa-solid fa-calendar-xmark text-orange-500"></i>
                                            <span>Ngày Check-out (Trả phòng):</span>
                                        </label>
                                        <input type="date" x-model="serviceBookingForm.hotelCheckOutDate" class="w-full bg-white border border-slate-300 rounded-xl px-4 py-2.5 text-xs sm:text-sm font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-orange-500">
                                    </div>

                                    <!-- 2 Dropdown Giờ Check-in & Giờ Check-out (Thay thế các block giờ tĩnh) -->
                                    <div>
                                        <label class="text-xs font-bold text-slate-700 block mb-1 flex items-center gap-1">
                                            <i class="fa-regular fa-clock text-orange-500"></i>
                                            <span>Giờ Check-in dự kiến:</span>
                                        </label>
                                        <select x-model="serviceBookingForm.hotelCheckInTime" class="w-full bg-white border border-slate-300 rounded-xl px-4 py-2.5 text-xs sm:text-sm font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-orange-500">
                                            <template x-for="t in ['07:00', '08:00', '09:00', '10:00', '11:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00']" :key="t">
                                                <option :value="t" x-text="t + ' (Giờ sáng/chiều đón)'"></option>
                                            </template>
                                        </select>
                                    </div>
                                    <div>
                                        <label class="text-xs font-bold text-slate-700 block mb-1 flex items-center gap-1">
                                            <i class="fa-regular fa-clock text-orange-500"></i>
                                            <span>Giờ Check-out dự kiến:</span>
                                        </label>
                                        <select x-model="serviceBookingForm.hotelCheckOutTime" class="w-full bg-white border border-slate-300 rounded-xl px-4 py-2.5 text-xs sm:text-sm font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-orange-500">
                                            <template x-for="t in ['08:00', '09:00', '10:00', '11:00', '12:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00']" :key="t">
                                                <option :value="t" x-text="t + ' (Giờ trả bé)'"></option>
                                            </template>
                                        </select>
                                    </div>
                                </div>

                                <!-- Tóm Tắt Số Ngày & Phí Phòng Pet Hotel -->
                                <div class="p-3.5 bg-white rounded-xl border border-orange-200 text-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 shadow-xs">
                                    <div class="flex items-center gap-2">
                                        <span class="w-2.5 h-2.5 rounded-full bg-orange-500"></span>
                                        <span class="font-bold text-slate-800">Thời gian lưu trú:</span>
                                        <span class="font-black text-orange-600 px-2 py-0.5 rounded-md bg-orange-100" x-text="hotelTotalDays + ' Ngày'"></span>
                                        <span class="text-slate-500 text-[11px]" x-text="'(Check-in ' + serviceBookingForm.hotelCheckInTime + ' ' + serviceBookingForm.hotelCheckInDate + ' -> Check-out ' + serviceBookingForm.hotelCheckOutTime + ' ' + serviceBookingForm.hotelCheckOutDate + ')'"></span>
                                    </div>
                                    <div class="font-bold text-slate-700">
                                        Phí phòng: <span class="font-black text-[#F97316]" x-text="formatCurrency(baseServicePrice) + ' x ' + hotelTotalDays + ' ngày = ' + formatCurrency(hotelFee)"></span>
                                    </div>
                                </div>
                            </div>

                            <!-- KHỐI DÀNH CHO TAB GROOMING & SPA VÀ TIÊM PHÒNG (Ẩn hoàn toàn khối thời gian lưu trú) -->
                            <div x-show="servicePricingTab !== 'hotel'" class="space-y-3 animate-fadeIn">
                                <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                                    Bước 3: Chọn Ngày & Khung Giờ Đặt Lịch
                                </label>
                                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                    <div>
                                        <span class="text-[11px] text-slate-500 block mb-1">Ngày đặt hẹn dịch vụ:</span>
                                        <input type="date" x-model="serviceBookingForm.date" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 text-xs sm:text-sm font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-brand-500">
                                    </div>
                                    <div>
                                        <span class="text-[11px] text-slate-500 block mb-1">Khung giờ đang chọn:</span>
                                        <input type="text" :value="'Giờ hẹn: ' + (serviceBookingForm.timeSlot || '09:30') + ' (Thời gian phục vụ: 45 - 90 phút)'" readonly class="w-full bg-slate-100 border border-slate-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm font-bold text-slate-700">
                                    </div>
                                </div>

                                <!-- Lưới Slot Giờ Real-time cho Grooming & Tiêm phòng -->
                                <div>
                                    <span class="text-[11px] text-slate-500 block mb-1.5 font-medium">Chọn khung giờ rảnh trong ngày:</span>
                                    <div class="grid grid-cols-3 sm:grid-cols-7 gap-2 pt-1">
                                        <template x-for="slot in ['08:30', '09:30', '10:30', '14:00', '15:30', '17:00', '18:30']" :key="slot">
                                            <button type="button" @click="if (slot !== '10:30') serviceBookingForm.timeSlot = slot" :class="{
                                                'bg-orange-500 text-white font-bold ring-2 ring-orange-300 shadow-sm': serviceBookingForm.timeSlot === slot,
                                                'bg-emerald-50 text-emerald-700 border border-emerald-200 hover:bg-emerald-100': slot !== '10:30' && serviceBookingForm.timeSlot !== slot,
                                                'bg-rose-50 text-rose-400 border border-rose-200 cursor-not-allowed opacity-60': slot === '10:30'
                                            }" class="py-2.5 px-2 rounded-xl text-xs font-semibold text-center transition">
                                                <div x-text="slot"></div>
                                                <span class="text-[9px] block" x-text="slot === '10:30' ? 'Đã kín' : 'Còn slot'"></span>
                                            </button>
                                        </template>
                                    </div>
                                </div>
                            </div>

                        </div>

                        <!-- Bước 4: Tích chọn Dịch vụ cộng thêm -->
                        <div class="space-y-2">
                            <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                                Bước 4: Dịch Vụ Cộng Thêm
                            </label>
                            <div class="space-y-2">
                                <label class="flex items-center justify-between p-3 rounded-xl border border-slate-200 hover:bg-slate-50 cursor-pointer transition">
                                    <div class="flex items-center gap-2.5 text-xs">
                                        <input type="checkbox" x-model="serviceBookingForm.addOnMassage" class="rounded text-brand-600 focus:ring-brand-500 w-4 h-4">
                                        <span class="font-medium text-slate-800">Tắm massage sục khí bọt Nano</span>
                                    </div>
                                    <span class="text-xs font-bold text-orange-600">+50.000đ</span>
                                </label>
                                <label class="flex items-center justify-between p-3 rounded-xl border border-slate-200 hover:bg-slate-50 cursor-pointer transition">
                                    <div class="flex items-center gap-2.5 text-xs">
                                        <input type="checkbox" x-model="serviceBookingForm.addOnFurDetangle" class="rounded text-brand-600 focus:ring-brand-500 w-4 h-4">
                                        <span class="font-medium text-slate-800">Gỡ rối lông & Phục hồi keratin</span>
                                    </div>
                                    <span class="text-xs font-bold text-orange-600">+80.000đ</span>
                                </label>
                                <label class="flex items-center justify-between p-3 rounded-xl border border-slate-200 hover:bg-slate-50 cursor-pointer transition">
                                    <div class="flex items-center gap-2.5 text-xs">
                                        <input type="checkbox" x-model="serviceBookingForm.addOnWalk" class="rounded text-brand-600 focus:ring-brand-500 w-4 h-4">
                                        <span class="font-medium text-slate-800">Dắt đi dạo sân cỏ tự nhiên (30p)</span>
                                    </div>
                                    <span class="text-xs font-bold text-orange-600">+40.000đ</span>
                                </label>
                            </div>
                        </div>

                        <!-- Bước 5: Tích chọn "Dịch vụ Xe Đưa Đón PetShip360 tận nhà" -->
                        <div class="space-y-2">
                            <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                                Bước 5: Xe Đưa Đón PetShip360 Tận Nhà
                            </label>
                            <label class="flex items-center gap-2.5 p-3 rounded-xl border border-orange-200 bg-orange-50/50 cursor-pointer">
                                <input type="checkbox" x-model="serviceBookingForm.usePetShip" class="rounded text-orange-500 focus:ring-orange-400 w-4 h-4">
                                <div class="text-xs">
                                    <span class="font-bold text-slate-800">Đăng ký xe chuyên dụng PetShip360</span>
                                    <span class="text-orange-600 font-bold block">(+60.000đ / lượt đưa đón)</span>
                                </div>
                            </label>
                            <template x-if="serviceBookingForm.usePetShip">
                                <div class="pt-1">
                                    <input type="text" x-model="serviceBookingForm.petShipAddress" placeholder="Nhập địa chỉ nhà cụ thể để tài xế qua đón..." class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-orange-500">
                                </div>
                            </template>
                        </div>

                        <!-- Bước 6: Khối Thông Tin Đặc Nhiệm -->
                        <div class="md:col-span-2 space-y-2">
                            <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                                Bước 6: Khối Thông Tin Đặc Nhiệm (Dị ứng, ăn uống, tính cách)
                            </label>
                            <textarea x-model="serviceBookingForm.specialNotes" rows="2" placeholder="Ví dụ: Bé sợ tiếng sấy mạnh, dị ứng hạt đậu nành, cần bôi kem tai sau khi tắm..." class="w-full bg-slate-50 border border-slate-300 rounded-xl p-3 text-xs sm:text-sm text-slate-800 focus:outline-none focus:ring-2 focus:ring-brand-500"></textarea>
                        </div>
                    </div>

                    <!-- KHỐI THANH TOÁN & TÓM TẮT CHI PHÍ ĐẶT LỊCH (CHECKOUT SUMMARY) -->
                    <div class="pt-6 border-t border-slate-200 bg-slate-50/90 -mx-6 -mb-6 sm:-mx-8 sm:-mb-8 p-6 sm:p-8 rounded-b-3xl space-y-4">
                        <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-6">
                            
                            <!-- BẢNG TỔNG CHI PHÍ THEO LOẠI DỊCH VỤ -->
                            <div class="space-y-2 flex-1">
                                
                                <!-- 1. DÀNH CHO TAB PET HOTEL 5 SAO: TÍNH CỌC 50% HIỂN THỊ 3 DÒNG RẠCH RÒI -->
                                <template x-if="servicePricingTab === 'hotel'">
                                    <div class="space-y-2">
                                        <!-- Dòng 1: Tổng chi phí dịch vụ (100%) - text màu xám, font thường -->
                                        <div class="flex items-center justify-between sm:justify-start gap-3 text-xs sm:text-sm text-slate-700">
                                            <span class="font-medium">Tổng chi phí dịch vụ (100%):</span>
                                            <span class="font-bold text-slate-900 text-sm sm:text-base" x-text="formatCurrency(totalServiceCost)"></span>
                                        </div>

                                        <!-- Dòng 2: Tiền cọc cần thanh toán (50%) - text to, in đậm, màu cam nổi bật -->
                                        <div class="flex items-center justify-between sm:justify-start gap-3 py-2 border-y border-dashed border-orange-200 bg-orange-50/70 px-3.5 rounded-xl">
                                            <div class="flex items-center gap-1.5">
                                                <span class="text-xs sm:text-sm font-black text-orange-600 uppercase tracking-wide">Tiền cọc cần thanh toán (50%):</span>
                                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-orange-500 text-white shadow-xs">Cọc giữ phòng</span>
                                            </div>
                                            <div class="text-2xl sm:text-3xl font-black text-[#F97316] tracking-tight" x-text="formatCurrency(depositAmount)"></div>
                                        </div>

                                        <!-- Dòng 3: Thanh toán khi trả pet (50%) - text nhỏ hơn, màu xám, in nghiêng -->
                                        <div class="flex items-center justify-between sm:justify-start gap-2 text-[11px] sm:text-xs text-slate-500 italic">
                                            <div class="flex items-center gap-1">
                                                <i class="fa-solid fa-clock-rotate-left text-slate-400"></i>
                                                <span>Thanh toán khi trả pet (50%):</span>
                                            </div>
                                            <span class="font-bold text-slate-700 not-italic" x-text="formatCurrency(remainingAmount)"></span>
                                            <span class="text-[10px] text-slate-400 hidden sm:inline">(Thanh toán trực tiếp tại quầy hoặc tài xế PetShip360 thu hộ)</span>
                                        </div>
                                    </div>
                                </template>

                                <!-- 2. DÀNH CHO TAB GROOMING & SPA VÀ TIÊM PHÒNG: KHÔNG TÍNH CỌC, 100% TỔNG TIỀN -->
                                <template x-if="servicePricingTab !== 'hotel'">
                                    <div class="space-y-2">
                                        <div class="flex items-center justify-between sm:justify-start gap-3 py-2 border-y border-dashed border-orange-200 bg-orange-50/70 px-3.5 rounded-xl">
                                            <span class="text-xs sm:text-sm font-black text-slate-800 uppercase tracking-wide">Tổng chi phí dịch vụ (100%):</span>
                                            <div class="text-2xl sm:text-3xl font-black text-[#F97316] tracking-tight" x-text="formatCurrency(totalServiceCost)"></div>
                                        </div>
                                        <p class="text-[11px] text-emerald-700 font-bold flex items-center gap-1.5">
                                            <i class="fa-solid fa-circle-check text-emerald-500"></i>
                                            <span>Thanh toán 100% giá trị dịch vụ khi xác nhận lịch hẹn (Không áp dụng đặt cọc)</span>
                                        </p>
                                    </div>
                                </template>

                                <!-- Diễn giải chi tiết cấu thành giá -->
                                <div class="text-[11px] text-slate-500 pt-1 flex items-center gap-1.5 flex-wrap">
                                    <i class="fa-solid fa-circle-info text-orange-500"></i>
                                    <span x-text="'(Dịch vụ: ' + (selectedBaseService ? selectedBaseService.name : 'Dịch vụ chuẩn') + ' [' + (servicePricingTab === 'hotel' ? formatCurrency(hotelFee) : formatCurrency(baseServicePrice)) + ']' + (totalAddonsCost > 0 ? ' + DV thêm: ' + formatCurrency(totalAddonsCost) : '') + (petShipCost > 0 ? ' + PetShip: ' + formatCurrency(petShipCost) : '') + ')'"></span>
                                </div>
                            </div>

                            <!-- VÙNG CALL-TO-ACTION (CTA) GỒM 2 NÚT ĐẶT CẠNH NHAU THEO YÊU CẦU 1 -->
                            <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3 flex-shrink-0">
                                <!-- Nút phụ (Secondary): THÊM VÀO GIỎ HÀNG -->
                                <button type="button" @click="submitServiceBooking(false)"
                                        class="w-full sm:w-auto border-2 border-[#F97316] bg-white text-[#F97316] hover:bg-orange-50 active:scale-98 font-black text-xs sm:text-sm px-6 py-3.5 rounded-2xl shadow-xs transition flex items-center justify-center gap-2">
                                    <i class="fa-solid fa-cart-plus"></i>
                                    <span>THÊM VÀO GIỎ HÀNG</span>
                                </button>

                                <!-- Nút chính (Primary): Đổi text theo Tab, nền cam nổi bật, chuyển hướng checkout -->
                                <button type="button" @click="submitServiceBooking(true)"
                                        class="w-full sm:w-auto bg-gradient-to-r from-orange-500 to-amber-500 hover:from-orange-600 hover:to-amber-600 text-white font-black text-xs sm:text-sm px-8 py-3.5 rounded-2xl shadow-lg shadow-orange-500/30 transition transform active:scale-98 flex items-center justify-center gap-2">
                                    <i class="fa-solid fa-calendar-check"></i>
                                    <span x-text="servicePricingTab === 'hotel' ? 'THANH TOÁN CỌC 50% & ĐẶT LỊCH' : 'THANH TOÁN NGAY & ĐẶT LỊCH'"></span>
                                    <i class="fa-solid fa-arrow-right text-xs"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ======================================================== -->
            <!-- TAB 4: PETSHARE360 (MẠNG XÃ HỘI HIỆN ĐẠI 1440PX - 3 CỘT) -->
            <!-- ======================================================== -->
            <div x-show="activeCustomerTab === 'petshare'" class="space-y-6" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                
                <!-- BỐ CỤC 3 CỘT (SOCIAL FEED LAYOUT 1440PX) -->
                <div class="flex flex-col lg:flex-row gap-6 justify-center items-start">
                    
                    <!-- CỘT TRÁI (SIDEBAR TRÁI - 280PX) -->
                    <div class="w-full lg:w-[280px] flex-shrink-0 space-y-4">
                        
                        <!-- Thẻ Hồ Sơ Chủ & Pet -->
                        <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm text-center relative overflow-hidden">
                            <div class="h-16 bg-gradient-to-r from-brand-600 to-teal-500 -mx-5 -mt-5 mb-4"></div>
                            <img :src="customerProfile.avatar" class="w-16 h-16 rounded-full object-cover border-4 border-white shadow-md mx-auto -mt-12 relative z-10">
                            <h4 class="font-bold text-base text-slate-800 mt-2" x-text="customerProfile.name"></h4>
                            <p class="text-xs text-brand-600 font-semibold" x-text="'Bé yêu: ' + customerProfile.pets[0].name + ' (Corgi)'"></p>
                            
                            <div class="grid grid-cols-2 gap-2 mt-4 pt-3 border-t border-slate-100 text-center">
                                <div>
                                    <span class="text-xs text-slate-400 block">Bài viết</span>
                                    <span class="font-extrabold text-slate-800 text-sm">18</span>
                                </div>
                                <div>
                                    <span class="text-xs text-slate-400 block">Thành viên</span>
                                    <span class="text-xs font-bold text-amber-600 bg-amber-50 px-2 py-0.5 rounded-full inline-block mt-0.5">VIP Gold</span>
                                </div>
                            </div>
                        </div>

                        <!-- Menu Nhanh -->
                        <div class="bg-white rounded-3xl p-4 border border-slate-200 shadow-sm space-y-1 text-xs sm:text-sm font-semibold">
                            <button class="w-full py-2.5 px-3 rounded-xl bg-brand-50 text-brand-700 flex items-center gap-2.5 text-left">
                                <i class="fa-solid fa-newspaper text-brand-600"></i>
                                <span>Bảng tin chung</span>
                            </button>
                            <button class="w-full py-2.5 px-3 rounded-xl text-slate-600 hover:bg-slate-50 flex items-center gap-2.5 text-left transition">
                                <i class="fa-solid fa-user-pen text-slate-400"></i>
                                <span>Bài viết của tôi</span>
                            </button>
                            <button class="w-full py-2.5 px-3 rounded-xl text-slate-600 hover:bg-slate-50 flex items-center gap-2.5 text-left transition">
                                <i class="fa-solid fa-stethoscope text-teal-500"></i>
                                <span>Mẹo chăm sóc từ Bác sĩ Thú y</span>
                            </button>
                            <button class="w-full py-2.5 px-3 rounded-xl text-slate-600 hover:bg-slate-50 flex items-center gap-2.5 text-left transition">
                                <i class="fa-solid fa-fire text-amber-500"></i>
                                <span>Chuỗi Streak chăm sóc Pet</span>
                            </button>
                        </div>

                        <!-- Khối Hashtag Hot -->
                        <div class="bg-white rounded-3xl p-4 border border-slate-200 shadow-sm space-y-3">
                            <h5 class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                                <i class="fa-solid fa-hashtag text-brand-600"></i>Hashtag Đang Hot
                            </h5>
                            <div class="flex flex-wrap gap-1.5">
                                <span class="text-xs bg-slate-100 hover:bg-brand-50 hover:text-brand-600 text-slate-600 font-medium px-2.5 py-1 rounded-lg cursor-pointer transition">#PoodleSàiGòn</span>
                                <span class="text-xs bg-slate-100 hover:bg-brand-50 hover:text-brand-600 text-slate-600 font-medium px-2.5 py-1 rounded-lg cursor-pointer transition">#MèoAnhLôngNgắn</span>
                                <span class="text-xs bg-slate-100 hover:bg-brand-50 hover:text-brand-600 text-slate-600 font-medium px-2.5 py-1 rounded-lg cursor-pointer transition">#KinhNghiệmTắmPet</span>
                                <span class="text-xs bg-slate-100 hover:bg-brand-50 hover:text-brand-600 text-slate-600 font-medium px-2.5 py-1 rounded-lg cursor-pointer transition">#PetCare360Spa</span>
                            </div>
                        </div>
                    </div>

                    <!-- CỘT GIỮA (MAIN FEED - 600PX) -->
                    <div class="w-full lg:w-[600px] flex-shrink-0 space-y-5">
                        
                        <!-- Widget "Tạo Bài Viết Mới" -->
                        <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-4">
                            <div class="flex items-center gap-3">
                                <img :src="customerProfile.avatar" class="w-10 h-10 rounded-full object-cover">
                                <input type="text" x-model="newPostText" placeholder="Hôm nay bé cưng của bạn thế nào?" class="w-full bg-slate-50 border border-slate-200 rounded-2xl px-4 py-2.5 text-xs sm:text-sm text-slate-800 focus:outline-none focus:ring-2 focus:ring-brand-500">
                            </div>
                            <div class="flex items-center justify-between pt-2 border-t border-slate-100">
                                <div class="flex items-center gap-1 sm:gap-2 text-slate-500 text-xs">
                                    <button class="p-2 rounded-xl hover:bg-slate-100 transition flex items-center gap-1 text-emerald-600 font-semibold" title="Tải ảnh / Video">
                                        <i class="fa-solid fa-image text-sm"></i>
                                        <span class="hidden sm:inline">Ảnh/Video</span>
                                    </button>
                                    <button class="p-2 rounded-xl hover:bg-slate-100 transition flex items-center gap-1 text-brand-600 font-semibold" title="Gắn thẻ Hồ sơ Pet">
                                        <i class="fa-solid fa-paw text-sm"></i>
                                        <span class="hidden sm:inline">Gắn thẻ Pet</span>
                                    </button>
                                    <button class="p-2 rounded-xl hover:bg-slate-100 transition flex items-center gap-1 text-amber-500 font-semibold" title="Cảm xúc">
                                        <i class="fa-solid fa-face-smile text-sm"></i>
                                        <span class="hidden sm:inline">Cảm xúc</span>
                                    </button>
                                </div>
                                <button @click="createSocialPost()" class="bg-orange-500 hover:bg-orange-600 text-white font-bold text-xs sm:text-sm px-5 py-2 rounded-xl shadow-md shadow-orange-500/20 transition">
                                    Đăng bài
                                </button>
                            </div>
                        </div>

                        <!-- DANH SÁCH BÀI ĐĂNG (POST CARDS) -->
                        <div class="space-y-5">
                            <template x-for="post in socialPosts" :key="post.id">
                                <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-4">
                                    
                                    <!-- Header Post -->
                                    <div class="flex items-center justify-between">
                                        <div class="flex items-center gap-3">
                                            <img :src="post.avatar" class="w-10 h-10 rounded-full object-cover border border-slate-200">
                                            <div>
                                                <div class="flex items-center gap-2">
                                                    <h5 class="font-bold text-xs sm:text-sm text-slate-900" x-text="post.author"></h5>
                                                    <span class="text-[10px] bg-brand-50 text-brand-700 font-bold px-2 py-0.2 rounded-full" x-text="'Bé: ' + post.petName"></span>
                                                </div>
                                                <span class="text-[11px] text-slate-400" x-text="post.time"></span>
                                            </div>
                                        </div>
                                        <button class="text-slate-400 hover:text-slate-600 p-1">
                                            <i class="fa-solid fa-ellipsis"></i>
                                        </button>
                                    </div>

                                    <!-- Nội dung text (Hỗ trợ hashtag màu xanh) -->
                                    <p class="text-xs sm:text-sm text-slate-700 leading-relaxed whitespace-pre-line" x-text="post.content"></p>

                                    <!-- Lưới Hình ảnh (Layout 1-4 ảnh) -->
                                    <template x-if="post.images && post.images.length > 0">
                                        <div :class="post.images.length === 1 ? 'grid grid-cols-1' : (post.images.length === 2 ? 'grid grid-cols-2 gap-2' : 'grid grid-cols-2 gap-2')" class="rounded-2xl overflow-hidden">
                                            <template x-for="(img, iidx) in post.images" :key="iidx">
                                                <img :src="img" class="w-full h-48 sm:h-56 object-cover hover:scale-105 transition duration-300 cursor-pointer">
                                            </template>
                                        </div>
                                    </template>

                                    <!-- Thanh Tương Tác: Thả tim, Bình luận, Chia sẻ -->
                                    <div class="flex items-center justify-between pt-2 border-t border-slate-100 text-xs font-semibold text-slate-500">
                                        <button @click="toggleLikePost(post.id)" :class="post.isLiked ? 'text-rose-500' : 'hover:text-rose-500'" class="flex items-center gap-1.5 py-1.5 px-3 rounded-xl hover:bg-slate-50 transition">
                                            <i :class="post.isLiked ? 'fa-solid fa-heart' : 'fa-regular fa-heart'" class="text-base"></i>
                                            <span x-text="post.likes"></span>
                                        </button>
                                        <button class="flex items-center gap-1.5 py-1.5 px-3 rounded-xl hover:bg-slate-50 transition hover:text-brand-600">
                                            <i class="fa-regular fa-comment text-base"></i>
                                            <span x-text="post.comments.length + ' bình luận'"></span>
                                        </button>
                                        <button @click="sharePost(post.id)" class="flex items-center gap-1.5 py-1.5 px-3 rounded-xl hover:bg-slate-50 transition hover:text-teal-600">
                                            <i class="fa-solid fa-share-nodes text-base"></i>
                                            <span>Chia sẻ</span>
                                        </button>
                                    </div>

                                    <!-- Khối Bình luận nhanh bên dưới mỗi bài viết -->
                                    <div class="pt-2 border-t border-slate-100 space-y-2">
                                        <template x-for="(c, cidx) in post.comments" :key="cidx">
                                            <div class="bg-slate-50 rounded-2xl p-2.5 text-xs flex items-start gap-2.5">
                                                <span class="font-bold text-slate-800" x-text="c.user + ':'"></span>
                                                <span class="text-slate-600 flex-1" x-text="c.text"></span>
                                            </div>
                                        </template>
                                        <div class="flex items-center gap-2 pt-1">
                                            <input type="text" x-model="quickCommentText[post.id]" @keyup.enter="addCommentToPost(post.id)" placeholder="Viết bình luận nhanh..." class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-1.5 text-xs text-slate-800 focus:outline-none focus:ring-1 focus:ring-brand-500">
                                            <button @click="addCommentToPost(post.id)" class="px-3 py-1.5 bg-brand-50 hover:bg-brand-100 text-brand-700 font-bold rounded-xl text-xs transition">Gửi</button>
                                        </div>
                                    </div>
                                </div>
                            </template>
                        </div>
                    </div>

                    <!-- CỘT PHẢI (SIDEBAR PHẢI - 300PX) -->
                    <div class="w-full lg:w-[300px] flex-shrink-0 space-y-4">
                        
                        <!-- Khối "Bác sĩ Thú y Tư vấn" -->
                        <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-3">
                            <h5 class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-2">
                                <i class="fa-solid fa-user-doctor text-brand-600"></i>Bác Sĩ Thú Y Tư Vấn
                            </h5>
                            <div class="space-y-3 text-xs">
                                <div class="p-2.5 rounded-2xl bg-slate-50 hover:bg-brand-50/60 transition cursor-pointer space-y-1">
                                    <span class="text-[10px] text-teal-600 font-bold">BS. Nguyễn Thanh Tùng</span>
                                    <h6 class="font-bold text-slate-800 leading-snug">Lịch tiêm phòng dại & 7 bệnh chuẩn nhất cho cún con 2026</h6>
                                </div>
                                <div class="p-2.5 rounded-2xl bg-slate-50 hover:bg-brand-50/60 transition cursor-pointer space-y-1">
                                    <span class="text-[10px] text-teal-600 font-bold">BS. Vũ Mai Anh</span>
                                    <h6 class="font-bold text-slate-800 leading-snug">Cách sơ cứu hạ thân nhiệt cho thú cưng vào mùa nóng</h6>
                                </div>
                            </div>
                        </div>

                        <!-- Khối "Thành viên tích cực trong tuần" (Leaderboard) -->
                        <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-3">
                            <h5 class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-2">
                                <i class="fa-solid fa-trophy text-amber-500"></i>Thành Viên Tích Cực Tuần
                            </h5>
                            <div class="space-y-2 text-xs">
                                <div class="flex items-center justify-between p-2 rounded-xl bg-amber-50/60 border border-amber-100">
                                    <div class="flex items-center gap-2">
                                        <span class="font-black text-amber-600 text-sm">#1</span>
                                        <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=80&q=80" class="w-7 h-7 rounded-full object-cover">
                                        <span class="font-bold text-slate-800">Lan Hương (Bé Miu)</span>
                                    </div>
                                    <span class="font-bold text-amber-600">340 tim</span>
                                </div>
                                <div class="flex items-center justify-between p-2 rounded-xl bg-slate-50">
                                    <div class="flex items-center gap-2">
                                        <span class="font-bold text-slate-500 text-sm">#2</span>
                                        <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=80&q=80" class="w-7 h-7 rounded-full object-cover">
                                        <span class="font-bold text-slate-800">Hoàng Nam (LuLu)</span>
                                    </div>
                                    <span class="font-bold text-slate-600">285 tim</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ======================================================== -->
            <!-- TAB 5: PETSHOW360 (CAMERA LIVE STREAM & GIÁM SÁT DỊCH VỤ) -->
            <!-- ======================================================== -->
            <div x-show="activeCustomerTab === 'petshow'" class="space-y-6" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                
                <!-- THANH TRẠNG THÁI ĐƠN HÀNG ACTIVE (TOP SERVICE BAR) -->
                <div class="bg-slate-900 text-white rounded-3xl p-5 sm:p-6 shadow-xl border border-slate-800 space-y-4">
                    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-4 border-b border-slate-800">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-2xl bg-orange-500 flex items-center justify-center text-white text-lg shadow-lg shadow-orange-500/30">
                                <i class="fa-solid fa-video animate-pulse"></i>
                            </div>
                            <div>
                                <span class="text-xs text-orange-400 font-mono font-bold tracking-wider">ĐANG GIÁM SÁT TRỰC TUYẾN</span>
                                <h3 class="text-base sm:text-lg font-extrabold text-white">Đơn hàng #SV-2026-8899 - Bé Poodle Lu đang gửi tại Pet Hotel VIP</h3>
                            </div>
                        </div>
                        <!-- Nút Liên Hệ Trực Tiếp Qua Zalo -->
                        <a href="https://zalo.me" target="_blank" class="self-start md:self-auto bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-xs sm:text-sm px-5 py-2.5 rounded-xl transition shadow flex items-center gap-2">
                            <i class="fa-solid fa-comment-dots text-base"></i>
                            <span>Liên Hệ Trực Tiếp Qua Zalo</span>
                        </a>
                    </div>

                    <!-- Thanh Tiến Độ Dịch Vụ 4 Bước (Bước 2 đang sáng màu cam) -->
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-xs pt-1">
                        <div class="p-3 rounded-2xl bg-slate-800/80 border border-slate-700 flex items-center gap-2.5 text-slate-300">
                            <span class="w-6 h-6 rounded-full bg-emerald-500 text-white font-bold flex items-center justify-center text-xs">✓</span>
                            <div>
                                <p class="font-bold text-white">1. Tiếp Nhận Pet</p>
                                <span class="text-[10px] text-slate-400">08:00 AM (Xong)</span>
                            </div>
                        </div>
                        <div class="p-3 rounded-2xl bg-orange-500/20 border-2 border-orange-500 flex items-center gap-2.5 text-orange-400">
                            <span class="w-6 h-6 rounded-full bg-orange-500 text-white font-bold flex items-center justify-center text-xs animate-ping">2</span>
                            <div>
                                <p class="font-bold text-orange-300">2. Đang Phục Vụ</p>
                                <span class="text-[10px] text-orange-400">Đang tại Khách sạn VIP</span>
                            </div>
                        </div>
                        <div class="p-3 rounded-2xl bg-slate-800/40 border border-slate-800 flex items-center gap-2.5 text-slate-500">
                            <span class="w-6 h-6 rounded-full bg-slate-700 text-slate-400 font-bold flex items-center justify-center text-xs">3</span>
                            <div>
                                <p class="font-bold">3. Hoàn Tất Spa</p>
                                <span class="text-[10px]">Dự kiến 04:00 PM</span>
                            </div>
                        </div>
                        <div class="p-3 rounded-2xl bg-slate-800/40 border border-slate-800 flex items-center gap-2.5 text-slate-500">
                            <span class="w-6 h-6 rounded-full bg-slate-700 text-slate-400 font-bold flex items-center justify-center text-xs">4</span>
                            <div>
                                <p class="font-bold">4. Sẵn Sàng Trả Pet</p>
                                <span class="text-[10px]">Dự kiến 06:00 PM</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- KHỐI CHÍNH: CAMERA LIVE STREAM & QUY TRÌNH CHĂM SÓC -->
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    
                    <!-- Khung Video Player Chính (2 Cột rộng) -->
                    <div class="lg:col-span-2 space-y-4">
                        <div class="bg-black rounded-3xl overflow-hidden shadow-2xl border border-slate-800 relative group aspect-video flex items-center justify-center">
                            <!-- Stream Video Mockup (Hình ảnh động chất lượng cao) -->
                            <img :src="activeLiveZone === 'dog' ? 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=1200&q=80' : (activeLiveZone === 'cat' ? 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=1200&q=80' : 'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?auto=format&fit=crop&w=1200&q=80')" class="w-full h-full object-cover">
                            
                            <!-- Badge Đỏ LIVE - 1080p -->
                            <div class="absolute top-4 left-4 flex items-center gap-2 z-10">
                                <span class="bg-rose-600 text-white font-black text-xs px-3 py-1 rounded-full uppercase tracking-wider flex items-center gap-1.5 shadow-lg animate-pulse">
                                    <span class="w-2 h-2 rounded-full bg-white"></span>
                                    <span>LIVE - 1080p</span>
                                </span>
                                <span class="bg-black/60 backdrop-blur text-white font-mono text-xs px-2.5 py-1 rounded-full border border-white/20">
                                    CAM-03 VIP | 60 FPS
                                </span>
                            </div>

                            <!-- Nút điều khiển Player (Phóng to, Chụp ảnh, Đổi góc quay 360) -->
                            <div class="absolute bottom-4 left-4 right-4 flex items-center justify-between text-white z-10 bg-gradient-to-t from-black/80 to-transparent p-3 rounded-2xl">
                                <div class="flex items-center gap-2 text-xs">
                                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                                    <span class="font-medium">Camera HD Góc rộng 360°</span>
                                </div>
                                <div class="flex items-center gap-2">
                                    <button @click="takeLiveSnapshot()" class="p-2 rounded-xl bg-white/20 hover:bg-white/30 backdrop-blur transition text-xs flex items-center gap-1.5" title="Chụp ảnh khoảnh khắc bé">
                                        <i class="fa-solid fa-camera"></i>
                                        <span class="hidden sm:inline">Chụp khoảnh khắc</span>
                                    </button>
                                    <button @click="toggleLiveCameraAngle()" class="p-2 rounded-xl bg-white/20 hover:bg-white/30 backdrop-blur transition text-xs flex items-center gap-1.5" title="Đổi góc quay 360">
                                        <i class="fa-solid fa-arrows-rotate"></i>
                                        <span class="hidden sm:inline" x-text="'Góc quay ' + liveCameraAngle + '°'"></span>
                                    </button>
                                    <button class="p-2 rounded-xl bg-white/20 hover:bg-white/30 backdrop-blur transition text-xs" title="Toàn màn hình">
                                        <i class="fa-solid fa-expand"></i>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <!-- Thanh chuyển đổi Khu Vực (Zone Switcher Tabs) -->
                        <div class="bg-white rounded-2xl p-2 border border-slate-200 shadow-sm flex gap-2">
                            <button @click="activeLiveZone = 'dog'" :class="activeLiveZone === 'dog' ? 'bg-brand-600 text-white font-bold' : 'text-slate-600 hover:bg-slate-100'" class="flex-1 py-2.5 px-3 rounded-xl text-xs sm:text-sm transition flex items-center justify-center gap-1.5">
                                <i class="fa-solid fa-dog"></i>
                                <span>Khu Vực Chó</span>
                            </button>
                            <button @click="activeLiveZone = 'cat'" :class="activeLiveZone === 'cat' ? 'bg-brand-600 text-white font-bold' : 'text-slate-600 hover:bg-slate-100'" class="flex-1 py-2.5 px-3 rounded-xl text-xs sm:text-sm transition flex items-center justify-center gap-1.5">
                                <i class="fa-solid fa-cat"></i>
                                <span>Khu Vực Mèo</span>
                            </button>
                            <button @click="activeLiveZone = 'play'" :class="activeLiveZone === 'play' ? 'bg-brand-600 text-white font-bold' : 'text-slate-600 hover:bg-slate-100'" class="flex-1 py-2.5 px-3 rounded-xl text-xs sm:text-sm transition flex items-center justify-center gap-1.5">
                                <i class="fa-solid fa-baseball"></i>
                                <span>Khu Vực Vui Chơi</span>
                            </button>
                        </div>
                    </div>

                    <!-- Khối Quy Trình Chăm Sóc Trong Ngày (Daily Care Workflow - 1 Cột) -->
                    <div class="bg-white rounded-3xl p-5 sm:p-6 border border-slate-200 shadow-sm space-y-4">
                        <div class="pb-3 border-b border-slate-100">
                            <h4 class="font-extrabold text-base text-slate-900">Nhật Ký Chăm Sóc Bé Lu Hôm Nay</h4>
                            <p class="text-xs text-slate-400">Cập nhật trực tiếp từ nhân viên trực ca</p>
                        </div>

                        <!-- Vertical Timeline -->
                        <div class="space-y-4 relative before:absolute before:left-3 before:top-2 before:bottom-2 before:w-0.5 before:bg-slate-200">
                            <template x-for="(tl, tidx) in dailyCareTimeline" :key="tidx">
                                <div class="relative pl-7 space-y-1">
                                    <div :class="tl.status === 'done' ? 'bg-emerald-500' : (tl.status === 'in_progress' ? 'bg-orange-500 ring-4 ring-orange-200' : 'bg-slate-300')" class="w-4 h-4 rounded-full absolute left-1 top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <span class="text-xs font-bold text-slate-900" x-text="tl.time"></span>
                                        <span :class="tl.status === 'done' ? 'bg-emerald-100 text-emerald-800' : (tl.status === 'in_progress' ? 'bg-orange-100 text-orange-800 font-bold' : 'bg-slate-100 text-slate-600')" class="text-[10px] px-2 py-0.2 rounded-full" x-text="tl.statusText"></span>
                                    </div>
                                    <p class="text-xs text-slate-700 font-medium" x-text="tl.task"></p>
                                    <template x-if="tl.photo">
                                        <img :src="tl.photo" class="w-20 h-16 rounded-xl object-cover border border-slate-200 shadow-sm mt-1">
                                    </template>
                                    <div class="flex items-center justify-between pt-1">
                                        <span class="text-[10px] text-slate-400" x-text="'Phụ trách: ' + tl.staff"></span>
                                        <button @click="sendStaffMessage(tl.staff)" class="text-[10px] text-brand-600 hover:underline font-bold">Gửi lời nhắn</button>
                                    </div>
                                </div>
                            </template>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ======================================================== -->
            <!-- TAB 6: ĐƠN HÀNG (DASHBOARD QUẢN LÝ ĐƠN HÀNG CHUYÊN NGHIỆP) -->
            <!-- ======================================================== -->
            <div x-show="activeCustomerTab === 'orders'" class="space-y-6" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                
                <!-- Header Dashboard -->
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-200">
                    <div>
                        <h2 class="text-2xl font-black text-slate-900">Quản Lý Đơn Hàng & Dịch Vụ</h2>
                        <p class="text-xs sm:text-sm text-slate-500">Xem tiến độ vận chuyển, xem hóa đơn chi tiết, đánh giá và mua lại nhanh chóng</p>
                    </div>
                    <!-- Bộ lọc trạng thái -->
                    <div class="flex flex-wrap gap-1.5">
                        <button @click="orderFilterStatus = 'all'" :class="orderFilterStatus === 'all' ? 'bg-brand-600 text-white font-bold' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-50'" class="px-3 py-1.5 rounded-xl text-xs transition">Tất cả</button>
                        <button @click="orderFilterStatus = 'shipping'" :class="orderFilterStatus === 'shipping' ? 'bg-brand-600 text-white font-bold' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-50'" class="px-3 py-1.5 rounded-xl text-xs transition">Đang giao</button>
                        <button @click="orderFilterStatus = 'delivered'" :class="orderFilterStatus === 'delivered' ? 'bg-brand-600 text-white font-bold' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-50'" class="px-3 py-1.5 rounded-xl text-xs transition">Đã giao</button>
                    </div>
                </div>

                <!-- Danh sách thẻ đơn hàng -->
                <div class="space-y-5">
                    <template x-for="ord in customerOrdersEnhanced" :key="ord.id">
                        <div x-show="orderFilterStatus === 'all' || orderFilterStatus === ord.status" class="bg-white rounded-3xl p-5 sm:p-6 border border-slate-200 shadow-sm space-y-4">
                            
                            <!-- Header Đơn Hàng: Mã, Ngày, Trạng thái -->
                            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-3 border-b border-slate-100 gap-2">
                                <div class="flex items-center gap-3">
                                    <span class="text-base font-extrabold text-slate-900 cursor-pointer hover:text-brand-600 transition" @click="openOrderCheckoutSummary(ord)" x-text="ord.orderCode"></span>
                                    <span class="text-xs text-slate-400" x-text="'Ngày đặt: ' + ord.date"></span>
                                </div>
                                <div class="flex items-center gap-2">
                                    <!-- Badge Trạng thái vận chuyển -->
                                    <span :class="ord.badgeColor" class="px-3 py-1 rounded-full text-xs font-bold border" x-text="ord.statusText"></span>
                                </div>
                            </div>

                            <!-- Khối Shipper (Nếu đang giao) -->
                            <template x-if="ord.status === 'shipping' && ord.shipper">
                                <div class="p-3 bg-indigo-50/70 rounded-2xl border border-indigo-100 flex items-center justify-between gap-3">
                                    <div class="flex items-center gap-2.5 text-xs text-indigo-900">
                                        <i class="fa-solid fa-motorcycle text-indigo-600 text-base"></i>
                                        <span>Shipper: <strong x-text="ord.shipper.name"></strong> - SĐT: <strong x-text="ord.shipper.phone"></strong></span>
                                    </div>
                                    <a :href="'tel:' + ord.shipper.phone" class="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs rounded-xl shadow-sm transition flex items-center gap-1.5">
                                        <i class="fa-solid fa-phone"></i>
                                        <span>Gọi Shipper</span>
                                    </a>
                                </div>
                            </template>

                            <!-- Danh sách sản phẩm trong đơn -->
                            <div class="space-y-3">
                                <template x-for="(item, iidx) in ord.items" :key="iidx">
                                    <div class="flex items-center gap-3 sm:gap-4">
                                        <img :src="item.image || item.img || getItemImage(item)" @error="$event.target.src='https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=300&q=80'" class="w-16 h-16 rounded-2xl object-cover border border-slate-200">
                                        <div class="flex-1 min-w-0">
                                            <h5 class="font-bold text-xs sm:text-sm text-slate-800 truncate" x-text="item.name"></h5>
                                            <p class="text-xs text-slate-400 mt-0.5" x-text="'Phân loại: ' + item.variant + ' | SL: x' + item.qty"></p>
                                        </div>
                                        <div class="text-right">
                                            <span class="text-xs sm:text-sm font-bold text-slate-900" x-text="formatCurrency(item.price * item.qty)"></span>
                                        </div>
                                    </div>
                                </template>
                            </div>

                            <!-- Tóm tắt thanh toán & 4 Nút Hành Động ở góc dưới bên phải -->
                            <div class="pt-4 border-t border-slate-100 flex flex-col md:flex-row md:items-center justify-between gap-4">
                                <div>
                                    <span class="text-xs text-slate-500">Tổng số tiền thanh toán:</span>
                                    <span class="text-lg font-extrabold text-orange-600 ml-1.5" x-text="formatCurrency(ord.total)"></span>
                                </div>
                                <div class="flex flex-wrap items-center gap-2">
                                    <!-- 1. Nút Chi tiết đơn hàng -->
                                    <button @click="openOrderCheckoutSummary(ord)" class="px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs transition flex items-center gap-1.5">
                                        <i class="fa-solid fa-receipt"></i>
                                        <span>Chi tiết đơn hàng</span>
                                    </button>

                                    <!-- 2. Nút Mua lại -->
                                    <button @click="reorderItems(ord)" class="px-4 py-2 rounded-xl bg-orange-50 hover:bg-orange-100 text-orange-700 font-bold text-xs transition flex items-center gap-1.5">
                                        <i class="fa-solid fa-rotate-right"></i>
                                        <span>Mua lại</span>
                                    </button>

                                    <!-- 3. Nút Đánh giá sản phẩm (chỉ khi Đã giao / Hoàn thành) -->
                                    <template x-if="ord.status === 'delivered'">
                                        <button @click="openReviewModal(ord)" class="px-4 py-2 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-700 font-bold text-xs transition flex items-center gap-1.5">
                                            <i class="fa-solid fa-star"></i>
                                            <span>Đánh giá sản phẩm</span>
                                        </button>
                                    </template>

                                    <!-- Xem ảnh xác nhận giao hàng (POD) -->
                                    <template x-if="ord.status === 'delivered' && ord.podPhoto">
                                        <button @click="openPODModal(ord)" class="px-4 py-2 rounded-xl bg-emerald-50 hover:bg-emerald-100 text-emerald-700 font-bold text-xs transition flex items-center gap-1.5">
                                            <i class="fa-solid fa-image"></i>
                                            <span>Xem ảnh POD</span>
                                        </button>
                                    </template>

                                    <!-- 4. Nút Yêu cầu Trả hàng / Hoàn tiền -->
                                    <template x-if="ord.status === 'delivered'">
                                        <button @click="openRefundModal(ord)" class="px-4 py-2 rounded-xl bg-rose-50 hover:bg-rose-100 text-rose-700 font-bold text-xs transition flex items-center gap-1.5">
                                            <i class="fa-solid fa-arrow-rotate-left"></i>
                                            <span>Trả hàng / Hoàn tiền</span>
                                        </button>
                                    </template>
                                </div>
                            </div>
                        </div>
                    </template>
                </div>
            </div>

            <!-- ======================================================== -->
            <!-- TAB 7: TÀI KHOẢN (SAAS DASHBOARD ACCOUNT THEO YÊU CẦU) -->
            <!-- ======================================================== -->
            <div x-show="activeCustomerTab === 'account' || activeCustomerTab === 'profile'" class="space-y-6" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                
                <!-- Header Trang Tài Khoản -->
                <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-slate-200 gap-2">
                    <div>
                        <h2 class="text-2xl font-black text-slate-900">Quản Lý Tài Khoản Cá Nhân</h2>
                        <p class="text-xs sm:text-sm text-slate-500">Cập nhật hồ sơ chủ nuôi, hạng thành viên tích điểm, hồ sơ thú cưng và sổ địa chỉ giao hàng</p>
                    </div>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    
                    <!-- CỘT TRÁI: 1. THÔNG TIN TÀI KHOẢN & 2. CẤP BẬC THÀNH VIÊN -->
                    <div class="space-y-6">
                        
                        <!-- 1. THÔNG TIN TÀI KHOẢN CƠ BẢN -->
                        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                            <h3 class="font-extrabold text-base text-slate-900 flex items-center gap-2">
                                <i class="fa-solid fa-user-circle text-brand-600"></i>Thông Tin Tài Khoản
                            </h3>
                            
                            <div class="flex items-center gap-4">
                                <div class="relative">
                                    <img :src="customerProfile.avatar" class="w-16 h-16 rounded-full object-cover border-2 border-brand-500 shadow">
                                    <button class="absolute -bottom-1 -right-1 w-6 h-6 rounded-full bg-slate-900 text-white text-[10px] flex items-center justify-center hover:bg-brand-600 transition" title="Thay đổi avatar">
                                        <i class="fa-solid fa-camera"></i>
                                    </button>
                                </div>
                                <div class="flex-1 min-w-0">
                                    <h4 class="font-bold text-sm text-slate-900 truncate" x-text="customerProfile.name"></h4>
                                    <div class="flex items-center gap-1.5 text-xs text-emerald-600 font-semibold mt-0.5">
                                        <i class="fa-solid fa-circle-check text-[10px]"></i>
                                        <span>Email đã xác thực</span>
                                    </div>
                                </div>
                            </div>

                            <div class="space-y-3 pt-2 text-xs">
                                <div>
                                    <label class="block text-slate-500 mb-1">Họ và tên:</label>
                                    <input type="text" x-model="customerProfile.name" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-slate-800 font-semibold focus:outline-none focus:ring-1 focus:ring-brand-500">
                                </div>
                                <div>
                                    <label class="block text-slate-500 mb-1">Địa chỉ Email:</label>
                                    <input type="email" x-model="customerProfile.email" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-slate-800 font-semibold focus:outline-none focus:ring-1 focus:ring-brand-500">
                                </div>
                                <div>
                                    <label class="block text-slate-500 mb-1">Số điện thoại liên hệ:</label>
                                    <input type="tel" x-model="customerProfile.phone" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-slate-800 font-semibold focus:outline-none focus:ring-1 focus:ring-brand-500">
                                </div>
                                <div class="grid grid-cols-2 gap-2">
                                    <div>
                                        <label class="block text-slate-500 mb-1">Ngày sinh:</label>
                                        <input type="date" value="1998-05-15" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-slate-800 focus:outline-none">
                                    </div>
                                    <div>
                                        <label class="block text-slate-500 mb-1">Giới tính:</label>
                                        <select class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-slate-800 focus:outline-none">
                                            <option>Nữ</option>
                                            <option>Nam</option>
                                            <option>Khác</option>
                                        </select>
                                    </div>
                                </div>
                            </div>

                            <div class="pt-3 flex gap-2">
                                <button @click="saveAccountProfile()" class="flex-1 py-2.5 bg-brand-600 hover:bg-brand-700 text-white font-bold text-xs rounded-xl shadow transition">
                                    Lưu thay đổi
                                </button>
                                <button @click="showChangePasswordModal = true" class="py-2.5 px-3 bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs rounded-xl transition">
                                    Đổi mật khẩu
                                </button>
                            </div>
                        </div>

                        <!-- 2. CẤP BẬC THÀNH VIÊN (MEMBERSHIP TIER) -->
                        <div class="bg-gradient-to-br from-amber-500 to-orange-600 rounded-3xl p-6 text-white shadow-xl space-y-4 relative overflow-hidden">
                            <div class="flex items-center justify-between">
                                <div>
                                    <span class="text-xs uppercase tracking-wider text-amber-200 font-bold">Hạng Hội Viên</span>
                                    <h4 class="text-2xl font-black">Thẻ Vàng (Gold VIP)</h4>
                                </div>
                                <i class="fa-solid fa-crown text-3xl text-amber-200"></i>
                            </div>

                            <div class="space-y-1">
                                <div class="flex justify-between text-xs font-semibold">
                                    <span>Điểm tích lũy hiện có:</span>
                                    <span class="font-extrabold text-white text-sm">1.250 điểm</span>
                                </div>
                                <div class="w-full bg-black/20 h-2.5 rounded-full overflow-hidden p-0.5">
                                    <div class="bg-white h-full rounded-full w-[65%]"></div>
                                </div>
                                <p class="text-[10px] text-amber-100 pt-0.5">Cần thêm 750 điểm nữa để thăng hạng Kim Cương (Diamond)</p>
                            </div>

                            <div class="pt-3 border-t border-white/20 space-y-1.5 text-xs">
                                <span class="font-bold text-amber-100 block">Đặc quyền hội viên Vàng:</span>
                                <p class="flex items-center gap-2"><i class="fa-solid fa-check text-amber-200 text-[10px]"></i> Giảm 5% mọi hóa đơn mua sắm & Spa</p>
                                <p class="flex items-center gap-2"><i class="fa-solid fa-check text-amber-200 text-[10px]"></i> Miễn phí vận chuyển PetShip 2H trong bán kính 5km</p>
                                <p class="flex items-center gap-2"><i class="fa-solid fa-check text-amber-200 text-[10px]"></i> Ưu tiên giữ phòng Pet Hotel mùa cao điểm lễ tết</p>
                            </div>
                        </div>
                    </div>

                    <!-- CỘT PHẢI: 3. THÔNG TIN THÚ CƯNG & 4. SỔ ĐỊA CHỈ GIAO HÀNG -->
                    <div class="lg:col-span-2 space-y-6">
                        
                        <!-- 3. THÔNG TIN THÚ CƯNG (PET PROFILES) -->
                        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                            <div class="flex items-center justify-between">
                                <h3 class="font-extrabold text-base text-slate-900 flex items-center gap-2">
                                    <i class="fa-solid fa-paw text-brand-600"></i>Hồ Sơ Thú Cưng Đã Lưu
                                </h3>
                                <button @click="openAddPetModal()" class="px-4 py-2 bg-brand-50 hover:bg-brand-100 text-brand-700 font-bold text-xs rounded-xl border border-brand-200 transition flex items-center gap-1.5 shadow-sm">
                                    <i class="fa-solid fa-plus"></i>
                                    <span>Thêm thú cưng mới</span>
                                </button>
                            </div>

                            <!-- Lưới thẻ thú cưng -->
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                <template x-for="p in customerProfile.pets" :key="p.id">
                                    <div class="p-4 rounded-2xl border border-slate-200 hover:border-brand-300 transition bg-slate-50/50 space-y-3 flex flex-col justify-between">
                                        <div class="flex items-center gap-3">
                                            <img :src="p.avatar || 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=150&q=80'" class="w-14 h-14 rounded-2xl object-cover border border-slate-200">
                                            <div>
                                                <h4 class="font-bold text-sm text-slate-900" x-text="p.name"></h4>
                                                <p class="text-xs text-brand-600 font-medium" x-text="p.species + ' • ' + p.breed"></p>
                                                <div class="flex items-center gap-2 text-[11px] text-slate-400 mt-1">
                                                    <span x-text="p.age"></span>
                                                    <span>•</span>
                                                    <span class="font-bold text-slate-700" x-text="p.weight + ' kg'"></span>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="flex items-center justify-between pt-2 border-t border-slate-200 text-xs">
                                            <button @click="openPetBookingDetailModal()" class="text-brand-600 hover:underline font-bold">Chỉnh sửa hồ sơ y tế</button>
                                            <button class="text-rose-500 hover:underline text-[11px]">Xóa</button>
                                        </div>
                                    </div>
                                </template>
                            </div>
                        </div>

                        <!-- 4. ĐỊA CHỈ GIAO HÀNG (SHIPPING ADDRESSES) -->
                        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                            <div class="flex items-center justify-between">
                                <h3 class="font-extrabold text-base text-slate-900 flex items-center gap-2">
                                    <i class="fa-solid fa-map-location-dot text-brand-600"></i>Sổ Địa Chỉ Giao Hàng
                                </h3>
                                <button @click="showAddressModal = true" class="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold text-xs rounded-xl transition flex items-center gap-1.5">
                                    <i class="fa-solid fa-plus"></i>
                                    <span>Thêm địa chỉ mới</span>
                                </button>
                            </div>

                            <div class="space-y-3">
                                <template x-for="addr in shippingAddresses" :key="addr.id">
                                    <div class="p-4 rounded-2xl border border-slate-200 bg-white space-y-2">
                                        <div class="flex items-center justify-between">
                                            <div class="flex items-center gap-2">
                                                <span class="font-bold text-xs sm:text-sm text-slate-900" x-text="addr.name"></span>
                                                <span class="text-xs text-slate-400" x-text="'(' + addr.phone + ')'"></span>
                                                <template x-if="addr.isDefault">
                                                    <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-full">Địa chỉ mặc định</span>
                                                </template>
                                            </div>
                                            <div class="flex items-center gap-2 text-xs">
                                                <button @click="setDefaultAddress(addr.id)" x-show="!addr.isDefault" class="text-brand-600 hover:underline font-medium">Đặt làm mặc định</button>
                                                <button class="text-slate-500 hover:text-slate-800">Sửa</button>
                                                <button @click="deleteAddress(addr.id)" x-show="!addr.isDefault" class="text-rose-500 hover:underline">Xóa</button>
                                            </div>
                                        </div>
                                        <p class="text-xs text-slate-600" x-text="addr.fullAddress"></p>
                                    </div>
                                </template>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ======================================================== -->
            <!-- TAB 8: GIỎ HÀNG (QUY TRÌNH 5 BƯỚC HOÀN THIỆN THEO YÊU CẦU) -->
            <!-- ======================================================== -->
            <div x-show="activeCustomerTab === 'cart'" class="space-y-6" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                
                <!-- BƯỚC 1: XEM GIỎ HÀNG ĐANG CÓ NHỮNG GÌ -->
                <div x-show="cartStep === 1" class="space-y-6">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-slate-200 gap-2">
                        <div>
                            <h2 class="text-2xl font-black text-slate-900">GIỎ HÀNG CỦA BẠN</h2>
                            <p class="text-xs sm:text-sm text-slate-500" x-text="'Bạn đang có ' + cartItemsCount + ' sản phẩm trong giỏ hàng'"></p>
                        </div>
                        <button @click="activeCustomerTab = 'shop'" class="text-brand-600 hover:underline text-xs font-bold flex items-center gap-1">
                            <i class="fa-solid fa-arrow-left"></i>Tiếp tục mua hàng
                        </button>
                    </div>

                    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                        <!-- Danh sách sản phẩm dạng bảng/dòng -->
                        <div class="lg:col-span-2 space-y-6">
                            <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm overflow-x-auto">
                                <table class="w-full text-left text-xs sm:text-sm border-collapse">
                                    <thead>
                                        <tr class="border-b border-slate-200 text-slate-500 font-semibold pb-3">
                                            <th class="py-3 px-2">Sản phẩm</th>
                                            <th class="py-3 px-2">Phân loại</th>
                                            <th class="py-3 px-2 text-center">Số lượng</th>
                                            <th class="py-3 px-2 text-right">Đơn giá</th>
                                            <th class="py-3 px-2 text-right">Thành tiền</th>
                                            <th class="py-3 px-2 text-center">Xóa</th>
                                        </tr>
                                    </thead>
                                    <tbody class="divide-y divide-slate-100">
                                        <template x-for="(item, cidx) in cart" :key="cidx">
                                            <tr class="hover:bg-slate-50/50">
                                                <td class="py-3.5 px-2">
                                                    <div class="flex items-center gap-3">
                                                        <img :src="item.image || item.img || getItemImage(item)" @error="$event.target.src='https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=300&q=80'" class="w-12 h-12 rounded-xl object-cover border border-slate-200">
                                                        <span class="font-bold text-slate-900 line-clamp-1 max-w-[180px]" x-text="item.name"></span>
                                                    </div>
                                                </td>
                                                <td class="py-3.5 px-2 text-xs text-slate-500" x-text="item.weight ? (item.weight + ' • ' + (item.flavor || 'Vị chuẩn')) : 'Tiêu chuẩn'"></td>
                                                <td class="py-3.5 px-2 text-center">
                                                    <div class="inline-flex items-center border border-slate-200 rounded-lg overflow-hidden bg-white">
                                                        <button @click="decreaseQty(item.id)" class="px-2 py-1 text-slate-500 hover:bg-slate-100 font-bold">−</button>
                                                        <span class="px-2 py-1 font-bold text-xs" x-text="item.quantity || 1"></span>
                                                        <button @click="increaseQty(item.id)" class="px-2 py-1 text-slate-500 hover:bg-slate-100 font-bold">+</button>
                                                    </div>
                                                </td>
                                                <td class="py-3.5 px-2 text-right text-slate-700" x-text="formatCurrency(item.price)"></td>
                                                <td class="py-3.5 px-2 text-right font-extrabold text-orange-600" x-text="formatCurrency(item.price * (item.quantity || 1))"></td>
                                                <td class="py-3.5 px-2 text-center">
                                                    <button @click="removeFromCart(item.id)" class="text-slate-400 hover:text-rose-600 transition" title="Xóa món này">
                                                        <i class="fa-solid fa-trash-can"></i>
                                                    </button>
                                                </td>
                                            </tr>
                                        </template>
                                    </tbody>
                                </table>
                            </div>

                            <!-- Khu vực bổ trợ: Ghi chú đơn hàng & Chính sách đổi trả -->
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-2">
                                    <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">Ghi chú đơn hàng:</label>
                                    <textarea x-model="cartNotes" rows="3" placeholder="Ghi chú thêm về thời gian nhận hàng, giao giờ hành chính..." class="w-full bg-slate-50 border border-slate-200 rounded-2xl p-3 text-xs text-slate-800 focus:outline-none focus:ring-1 focus:ring-brand-500"></textarea>
                                </div>
                                <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-2">
                                    <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">Chính sách Đổi/Trả PetCare360:</label>
                                    <ul class="text-xs text-slate-500 space-y-1">
                                        <li>• Đổi trả miễn phí trong 3 ngày nếu phát hiện lỗi bao bì.</li>
                                        <li>• Hỗ trợ đổi vị hạt nếu bé thú cưng mẫn cảm không hợp.</li>
                                        <li>• Đền bù 200% nếu phát hiện sản phẩm không chính hãng.</li>
                                    </ul>
                                </div>
                            </div>
                        </div>

                        <!-- Cột tổng quan bên phải (Thông tin đơn hàng) -->
                        <div class="space-y-4">
                            <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                                <h3 class="font-extrabold text-base text-slate-900 pb-3 border-b border-slate-100">Thông Tin Đơn Hàng</h3>
                                <div class="flex justify-between text-sm">
                                    <span class="text-slate-500">Tạm tính:</span>
                                    <span class="font-extrabold text-slate-900 text-base" x-text="formatCurrency(cartSubtotal)"></span>
                                </div>
                                <!-- KHỐI COMPONENT CHỌN MÃ KHUYẾN MÃI (TICKET STYLE COMPONENT - YÊU CẦU 3.1) -->
                                <div @click="openVoucherWallet()" class="p-3.5 rounded-2xl border-2 border-dashed border-orange-300 bg-orange-50/50 hover:bg-orange-50 cursor-pointer transition flex items-center justify-between group">
                                    <div class="flex items-center gap-3">
                                        <div class="w-9 h-9 rounded-xl bg-orange-500 text-white flex items-center justify-center font-bold text-base shadow-sm group-hover:scale-105 transition">
                                            <i class="fa-solid fa-ticket"></i>
                                        </div>
                                        <div>
                                            <div class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
                                                <span>PetCare Voucher</span>
                                                <span class="text-[9px] bg-orange-100 text-orange-800 font-bold px-1.5 py-0.5 rounded">Kho Voucher</span>
                                            </div>
                                            <template x-if="!hasAppliedVouchers">
                                                <p class="text-[11px] text-slate-500 font-medium mt-0.5">Chọn hoặc nhập mã khuyến mãi</p>
                                            </template>
                                            <template x-if="hasAppliedVouchers">
                                                <div class="flex flex-wrap gap-1 mt-1">
                                                    <template x-if="appliedVouchers.shipping">
                                                        <span class="inline-flex items-center gap-1 bg-blue-100 text-blue-800 text-[10px] font-bold px-2 py-0.5 rounded-md border border-blue-200">
                                                            <i class="fa-solid fa-truck-fast text-[9px]"></i>
                                                            <span x-text="appliedVouchers.shipping.code"></span>
                                                            <button type="button" @click.stop="removeVoucher('shipping')" class="text-blue-600 hover:text-blue-900 font-black ml-1 text-xs">&times;</button>
                                                        </span>
                                                    </template>
                                                    <template x-if="appliedVouchers.order">
                                                        <span class="inline-flex items-center gap-1 bg-emerald-100 text-emerald-800 text-[10px] font-bold px-2 py-0.5 rounded-md border border-emerald-200">
                                                            <i class="fa-solid fa-tag text-[9px]"></i>
                                                            <span x-text="appliedVouchers.order.code"></span>
                                                            <button type="button" @click.stop="removeVoucher('order')" class="text-emerald-600 hover:text-emerald-900 font-black ml-1 text-xs">&times;</button>
                                                        </span>
                                                    </template>
                                                </div>
                                            </template>
                                        </div>
                                    </div>
                                    <div class="flex items-center gap-1 text-xs font-bold text-orange-600 group-hover:translate-x-1 transition">
                                        <span x-text="hasAppliedVouchers ? 'Đổi mã' : 'Chọn'"></span>
                                        <i class="fa-solid fa-chevron-right text-[10px]"></i>
                                    </div>
                                </div>
                                <template x-if="totalDiscount > 0">
                                    <div class="flex justify-between text-xs text-emerald-600 font-extrabold">
                                        <span>Giảm giá:</span>
                                        <span x-text="'-' + formatCurrency(totalDiscount)"></span>
                                    </div>
                                </template>
                                <!-- Nút bấm lớn màu đen "THANH TOÁN" -->
                                <button @click="goToCartStep(2)" class="w-full py-4 rounded-2xl bg-black hover:bg-slate-800 text-white font-extrabold text-base transition shadow-lg flex items-center justify-center gap-2">
                                    <span>THANH TOÁN</span>
                                    <i class="fa-solid fa-arrow-right"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- BƯỚC 2: XÁC THỰC THÔNG TIN NHẬN HÀNG (THÔNG TIN GIAO HÀNG & LỊCH HẸN DỊCH VỤ) -->
                <div x-show="cartStep === 2" class="space-y-6">
                    <!-- Header thanh tiến trình -->
                    <div class="py-3 border-b border-slate-200 flex items-center gap-2 text-xs sm:text-sm font-bold text-slate-500">
                        <span class="text-slate-400 hover:text-orange-600 cursor-pointer flex items-center gap-1" @click="goToCartStep(1)">
                            <i class="fa-solid fa-cart-shopping text-xs"></i>
                            <span>1. Giỏ hàng</span>
                        </span>
                        <i class="fa-solid fa-chevron-right text-[10px] text-slate-300"></i>
                        <span class="text-orange-600 font-extrabold flex items-center gap-1 bg-orange-50 px-2.5 py-1 rounded-lg">
                            <i class="fa-solid fa-truck-ramp-box text-xs"></i>
                            <span>2. Thông tin nhận hàng & Lịch hẹn</span>
                        </span>
                        <i class="fa-solid fa-chevron-right text-[10px] text-slate-300"></i>
                        <span class="text-slate-400 flex items-center gap-1">
                            <i class="fa-solid fa-credit-card text-xs"></i>
                            <span>3. Phương thức thanh toán</span>
                        </span>
                    </div>

                    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                        <!-- CỘT BÊN TRÁI: THÔNG TIN GIAO NHẬN HÀNG / LỊCH HẸN (CONDITIONAL RENDERING) -->
                        <div class="lg:col-span-2 space-y-5">

                            <!-- TRƯỜNG HỢP 1: CHỈ CÓ SẢN PHẨM VẬT LÝ (hasProduct = true & hasService = false) -->
                            <template x-if="hasProduct && !hasService">
                                <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-5">
                                    <div class="flex items-center justify-between pb-3 border-b border-slate-100">
                                        <div>
                                            <span class="px-2.5 py-0.5 bg-orange-100 text-orange-700 font-extrabold text-[10px] rounded-full uppercase tracking-wider">Đơn Sản Phẩm</span>
                                            <h3 class="font-extrabold text-lg text-slate-900 mt-1 flex items-center gap-2">
                                                <i class="fa-solid fa-box-open text-orange-500"></i>
                                                <span>Thông tin nhận sản phẩm</span>
                                            </h3>
                                            <p class="text-xs text-slate-400" x-text="'Tài khoản: ' + customerProfile.name + ' (' + customerProfile.phone + ')'"></p>
                                        </div>
                                        <button @click="logout()" class="text-xs text-rose-500 hover:underline font-bold">Đăng xuất</button>
                                    </div>

                                    <!-- Option Giao tận nơi / Nhận tại cửa hàng -->
                                    <div class="space-y-2">
                                        <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">Phương thức nhận hàng:</label>
                                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                            <label class="p-3.5 rounded-2xl border cursor-pointer transition flex items-center gap-2.5" :class="deliveryMethod === 'door' ? 'border-orange-500 bg-orange-50/60 ring-2 ring-orange-500/20' : 'border-slate-200 hover:bg-slate-50'">
                                                <input type="radio" value="door" x-model="deliveryMethod" class="text-orange-500">
                                                <div>
                                                    <span class="font-bold text-xs sm:text-sm text-slate-800 block">Giao tận nơi</span>
                                                    <span class="text-[11px] text-slate-500">Phí giao hàng: 35.000đ (2-3 ngày)</span>
                                                </div>
                                            </label>
                                            <label class="p-3.5 rounded-2xl border cursor-pointer transition flex items-center gap-2.5" :class="deliveryMethod === 'store' ? 'border-orange-500 bg-orange-50/60 ring-2 ring-orange-500/20' : 'border-slate-200 hover:bg-slate-50'">
                                                <input type="radio" value="store" x-model="deliveryMethod" class="text-orange-500">
                                                <div>
                                                    <span class="font-bold text-xs sm:text-sm text-slate-800 block">Nhận tại cửa hàng</span>
                                                    <span class="text-[11px] text-emerald-600 font-semibold">Miễn phí nhận tại cơ sở 88 NTMK</span>
                                                </div>
                                            </label>
                                        </div>
                                    </div>

                                    <!-- Form điền địa chỉ người nhận (Kèm Validation & Inline Errors) -->
                                    <div class="space-y-3.5 text-xs sm:text-sm pt-2">
                                        <div>
                                            <label class="block text-slate-600 font-bold mb-1">Quốc gia:</label>
                                            <input type="text" value="Việt Nam" readonly class="w-full bg-slate-100 border border-slate-200 rounded-xl px-4 py-2.5 text-slate-600 font-semibold cursor-not-allowed">
                                        </div>
                                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                            <div>
                                                <label class="block text-slate-600 font-bold mb-1">Họ và tên người nhận: <span class="text-rose-500">*</span></label>
                                                <input type="text" x-model="checkoutShippingForm.name" @blur="checkoutShippingForm.touched.name = true" placeholder="Nguyễn Văn A" class="w-full bg-slate-50 border rounded-xl px-4 py-2.5 text-slate-800 font-semibold focus:outline-none focus:bg-white" :class="checkoutFormErrors.name ? 'border-rose-400 bg-rose-50/20' : 'border-slate-300'">
                                                <p x-show="checkoutFormErrors.name" x-text="checkoutFormErrors.name" class="text-rose-500 text-[11px] font-semibold mt-1 flex items-center gap-1"></p>
                                            </div>
                                            <div>
                                                <label class="block text-slate-600 font-bold mb-1">Số điện thoại người nhận: <span class="text-rose-500">*</span></label>
                                                <input type="tel" x-model="checkoutShippingForm.phone" @blur="checkoutShippingForm.touched.phone = true" placeholder="0909123456 (10 số)" class="w-full bg-slate-50 border rounded-xl px-4 py-2.5 text-slate-800 font-semibold focus:outline-none focus:bg-white font-mono" :class="checkoutFormErrors.phone ? 'border-rose-400 bg-rose-50/20' : 'border-slate-300'">
                                                <p x-show="checkoutFormErrors.phone" x-text="checkoutFormErrors.phone" class="text-rose-500 text-[11px] font-semibold mt-1 flex items-center gap-1"></p>
                                            </div>
                                        </div>

                                        <template x-if="deliveryMethod === 'door'">
                                            <div class="space-y-3 pt-1">
                                                <div>
                                                    <label class="block text-slate-600 font-bold mb-1">Địa chỉ cụ thể (Số nhà, tên đường): <span class="text-rose-500">*</span></label>
                                                    <input type="text" x-model="checkoutShippingForm.address" @blur="checkoutShippingForm.touched.address = true" placeholder="Ví dụ: 125 Hoàng Quốc Việt" class="w-full bg-slate-50 border rounded-xl px-4 py-2.5 text-slate-800 font-semibold focus:outline-none focus:bg-white" :class="checkoutFormErrors.address ? 'border-rose-400 bg-rose-50/20' : 'border-slate-300'">
                                                    <p x-show="checkoutFormErrors.address" x-text="checkoutFormErrors.address" class="text-rose-500 text-[11px] font-semibold mt-1 flex items-center gap-1"></p>
                                                </div>
                                                <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
                                                    <div>
                                                        <label class="block text-slate-500 text-[11px] font-bold mb-1">Tỉnh / Thành phố: <span class="text-rose-500">*</span></label>
                                                        <select x-model="checkoutShippingForm.city" @change="onCityChange(); checkoutShippingForm.touched.city = true" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold focus:outline-none focus:bg-white">
                                                            <template x-for="p in vnProvinces" :key="p.name">
                                                                <option :value="p.name" x-text="p.name"></option>
                                                            </template>
                                                        </select>
                                                    </div>
                                                    <div>
                                                        <label class="block text-slate-500 text-[11px] font-bold mb-1">Quận / Huyện: <span class="text-rose-500">*</span></label>
                                                        <select x-model="checkoutShippingForm.district" @change="onDistrictChange(); checkoutShippingForm.touched.district = true" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold focus:outline-none focus:bg-white">
                                                            <template x-for="d in currentProvinceDistricts" :key="d.name">
                                                                <option :value="d.name" x-text="d.name"></option>
                                                            </template>
                                                        </select>
                                                    </div>
                                                    <div>
                                                        <label class="block text-slate-500 text-[11px] font-bold mb-1">Phường / Xã: <span class="text-rose-500">*</span></label>
                                                        <select x-model="checkoutShippingForm.ward" @change="checkoutShippingForm.touched.ward = true" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold focus:outline-none focus:bg-white">
                                                            <template x-for="w in currentDistrictWards" :key="w">
                                                                <option :value="w" x-text="w"></option>
                                                            </template>
                                                        </select>
                                                    </div>
                                                </div>
                                            </div>
                                        </template>

                                        <template x-if="deliveryMethod === 'store'">
                                            <div class="p-4 bg-orange-50/60 rounded-2xl border border-orange-200 text-xs space-y-1.5 text-slate-700">
                                                <div class="font-bold text-orange-800 flex items-center gap-1.5">
                                                    <i class="fa-solid fa-store"></i>
                                                    <span>Địa chỉ nhận hàng tại shop:</span>
                                                </div>
                                                <p class="font-semibold text-slate-900">• Cơ sở Chính: 88 Nguyễn Thị Minh Khai, Phường Đa Kao, Quận 1, TP.HCM</p>
                                                <p class="text-slate-500">• Giờ mở cửa đón khách: 08:00 - 21:00 hàng ngày (Hotline: 028 3930 8888)</p>
                                            </div>
                                        </template>
                                    </div>
                                </div>
                            </template>

                            <!-- TRƯỜNG HỢP 2: CHỈ CÓ DỊCH VỤ (!hasProduct && hasService) -->
                            <template x-if="!hasProduct && hasService">
                                <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-5">
                                    <div class="flex items-center justify-between pb-3 border-b border-slate-100">
                                        <div>
                                            <span class="px-2.5 py-0.5 bg-blue-100 text-blue-700 font-extrabold text-[10px] rounded-full uppercase tracking-wider">Đơn Dịch Vụ Trực Tiếp</span>
                                            <h3 class="font-extrabold text-lg text-slate-900 mt-1 flex items-center gap-2">
                                                <i class="fa-solid fa-calendar-check text-blue-600"></i>
                                                <span>Thông Tin Lịch Hẹn Dịch Vụ</span>
                                            </h3>
                                            <p class="text-xs text-slate-400">Dịch vụ thực hiện trực tiếp tại cơ sở hoặc qua PetShip đưa đón</p>
                                        </div>
                                        <span class="text-xs font-bold text-blue-600 bg-blue-50 px-3 py-1 rounded-full border border-blue-200 flex items-center gap-1">
                                            <i class="fa-solid fa-lock text-[10px]"></i> Read-only
                                        </span>
                                    </div>

                                    <!-- Khối Read-only: Tên khách hàng, SĐT, Cơ sở thực hiện và Địa chỉ PetShip -->
                                    <div class="bg-slate-50 rounded-2xl p-5 border border-slate-200 space-y-4">
                                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs sm:text-sm">
                                            <div class="space-y-1">
                                                <label class="text-slate-500 text-xs font-bold block">Tên khách hàng:</label>
                                                <div class="p-3 bg-white rounded-xl border border-slate-200 font-extrabold text-slate-800" x-text="checkoutShippingForm.name || customerProfile.name"></div>
                                            </div>
                                            <div class="space-y-1">
                                                <label class="text-slate-500 text-xs font-bold block">Số điện thoại liên hệ:</label>
                                                <div class="p-3 bg-white rounded-xl border border-slate-200 font-extrabold text-slate-800 font-mono" x-text="checkoutShippingForm.phone || customerProfile.phone"></div>
                                            </div>
                                        </div>

                                        <div class="space-y-1 text-xs sm:text-sm">
                                            <label class="text-slate-500 text-xs font-bold block">Cơ sở thực hiện:</label>
                                            <div class="p-3.5 bg-white rounded-xl border border-blue-200 text-slate-800 font-bold flex items-center gap-2.5 shadow-sm">
                                                <div class="w-8 h-8 rounded-lg bg-rose-50 text-rose-600 flex items-center justify-center font-bold text-sm">
                                                    <i class="fa-solid fa-location-dot"></i>
                                                </div>
                                                <div>
                                                    <span class="text-slate-900 block font-extrabold">Cơ sở Chính: 88 Nguyễn Thị Minh Khai, Phường Đa Kao, Quận 1, TPHCM</span>
                                                    <span class="block text-[11px] text-slate-400 font-normal">Hotline cơ sở: 028 3930 8888 • Giờ mở cửa: 08:00 - 21:00 hàng ngày</span>
                                                </div>
                                            </div>
                                        </div>

                                        <div class="space-y-1 text-xs sm:text-sm">
                                            <label class="text-slate-500 text-xs font-bold block">Phương thức đưa đón PetShip:</label>
                                            <div class="p-3.5 bg-white rounded-xl border border-slate-200 text-slate-700">
                                                <template x-if="servicePetShipAddress">
                                                    <div class="flex items-start gap-2.5 text-orange-700">
                                                        <i class="fa-solid fa-van-shuttle mt-1 text-orange-600 text-sm"></i>
                                                        <div>
                                                            <span class="font-bold">Đưa đón PetShip tận nơi: </span>
                                                            <strong class="text-slate-900 font-semibold" x-text="servicePetShipAddress"></strong>
                                                            <p class="text-[11px] text-slate-500 font-normal mt-0.5">Phí PetShip đã được tính trọn gói trong giá dịch vụ</p>
                                                        </div>
                                                    </div>
                                                </template>
                                                <template x-if="!servicePetShipAddress">
                                                    <div class="flex items-center gap-2 text-slate-600">
                                                        <i class="fa-solid fa-person-walking text-slate-400 text-sm"></i>
                                                        <span class="font-medium">Khách hàng tự đưa đón thú cưng tại Cơ sở 88 Nguyễn Thị Minh Khai</span>
                                                    </div>
                                                </template>
                                            </div>
                                        </div>

                                        <!-- Danh sách dịch vụ trong giỏ -->
                                        <div class="pt-3 border-t border-slate-200/80">
                                            <label class="text-slate-600 text-xs font-bold block mb-2">Chi tiết các dịch vụ đã chọn:</label>
                                            <div class="space-y-2">
                                                <template x-for="(srv, sidx) in serviceCartItems" :key="sidx">
                                                    <div class="p-3 bg-white rounded-xl border border-slate-200 flex items-center justify-between text-xs">
                                                        <div class="flex items-center gap-2.5">
                                                            <span class="w-2.5 h-2.5 rounded-full" :class="isHotelItem(srv) ? 'bg-orange-500' : 'bg-blue-500'"></span>
                                                            <div>
                                                                <p class="font-bold text-slate-900" x-text="srv.name"></p>
                                                                <p class="text-slate-400 text-[11px]" x-text="srv.variant || (srv.bookingDetails ? srv.bookingDetails.petName + ' (' + (srv.bookingDetails.date || srv.bookingDetails.checkInDate) + ')' : '')"></p>
                                                            </div>
                                                        </div>
                                                        <div class="text-right">
                                                            <span class="font-extrabold text-slate-900" x-text="formatCurrency(srv.totalCost || srv.price)"></span>
                                                            <template x-if="isHotelItem(srv)">
                                                                <span class="block text-[10px] text-orange-600 font-semibold">(Cọc 50%: <span x-text="formatCurrency(hotelDeposit)"></span>)</span>
                                                            </template>
                                                        </div>
                                                    </div>
                                                </template>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </template>

                            <!-- TRƯỜNG HỢP 3: MIXED CART (hasProduct = true & hasService = true) -->
                            <template x-if="hasProduct && hasService">
                                <div class="space-y-5">
                                    <div class="p-4 bg-gradient-to-r from-orange-50 via-amber-50 to-orange-50 rounded-2xl border border-orange-200 flex items-center justify-between">
                                        <div class="flex items-center gap-3">
                                            <div class="w-10 h-10 rounded-xl bg-orange-500 text-white flex items-center justify-center font-bold text-base shadow">
                                                <i class="fa-solid fa-layer-group"></i>
                                            </div>
                                            <div>
                                                <h4 class="font-extrabold text-sm text-slate-900">Giỏ Hàng Hỗn Hợp (Mixed Cart)</h4>
                                                <p class="text-xs text-slate-600">Đơn hàng gồm cả Sản phẩm vật lý & Dịch vụ thú cưng</p>
                                            </div>
                                        </div>
                                        <span class="text-[11px] font-bold text-orange-700 bg-white px-3 py-1 rounded-full border border-orange-200 shadow-sm">2 Khối Tách Biệt</span>
                                    </div>

                                    <!-- Khối 1 - "Thông tin nhận Sản phẩm" (Thẻ/Card có viền xám nhạt) -->
                                    <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm space-y-4">
                                        <div class="flex items-center justify-between pb-3 border-b border-slate-100">
                                            <div class="flex items-center gap-2.5">
                                                <span class="w-7 h-7 rounded-lg bg-orange-500 text-white font-black text-xs flex items-center justify-center shadow-sm">1</span>
                                                <h4 class="font-extrabold text-base text-slate-900">Thông tin nhận Sản phẩm</h4>
                                            </div>
                                            <span class="text-xs text-slate-400 font-semibold">Giao hàng / Nhận tại shop</span>
                                        </div>

                                        <!-- Option Giao hàng / Nhận tại shop -->
                                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                            <label class="p-3.5 rounded-2xl border cursor-pointer transition flex items-center gap-2.5" :class="deliveryMethod === 'door' ? 'border-orange-500 bg-orange-50/60 ring-2 ring-orange-500/20' : 'border-slate-200 hover:bg-slate-50'">
                                                <input type="radio" value="door" x-model="deliveryMethod" class="text-orange-500">
                                                <div>
                                                    <span class="font-bold text-xs sm:text-sm text-slate-800 block">Giao tận nơi</span>
                                                    <span class="text-[11px] text-slate-500">Phí giao hàng: 35.000đ</span>
                                                </div>
                                            </label>
                                            <label class="p-3.5 rounded-2xl border cursor-pointer transition flex items-center gap-2.5" :class="deliveryMethod === 'store' ? 'border-orange-500 bg-orange-50/60 ring-2 ring-orange-500/20' : 'border-slate-200 hover:bg-slate-50'">
                                                <input type="radio" value="store" x-model="deliveryMethod" class="text-orange-500">
                                                <div>
                                                    <span class="font-bold text-xs sm:text-sm text-slate-800 block">Nhận tại cửa hàng</span>
                                                    <span class="text-[11px] text-emerald-600 font-semibold">Miễn phí tại 88 NTMK, Q1</span>
                                                </div>
                                            </label>
                                        </div>

                                        <!-- Form điền địa chỉ người nhận Sản phẩm -->
                                        <div class="space-y-3 text-xs sm:text-sm pt-1">
                                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                                <div>
                                                    <label class="block text-slate-600 font-bold mb-1">Họ tên người nhận: <span class="text-rose-500">*</span></label>
                                                    <input type="text" x-model="checkoutShippingForm.name" @blur="checkoutShippingForm.touched.name = true" placeholder="Nguyễn Văn A" class="w-full bg-slate-50 border rounded-xl px-4 py-2.5 text-slate-800 font-semibold focus:outline-none focus:bg-white" :class="checkoutFormErrors.name ? 'border-rose-400 bg-rose-50/20' : 'border-slate-300'">
                                                    <p x-show="checkoutFormErrors.name" x-text="checkoutFormErrors.name" class="text-rose-500 text-[11px] font-semibold mt-1"></p>
                                                </div>
                                                <div>
                                                    <label class="block text-slate-600 font-bold mb-1">Số điện thoại: <span class="text-rose-500">*</span></label>
                                                    <input type="tel" x-model="checkoutShippingForm.phone" @blur="checkoutShippingForm.touched.phone = true" placeholder="0909123456" class="w-full bg-slate-50 border rounded-xl px-4 py-2.5 text-slate-800 font-semibold focus:outline-none focus:bg-white font-mono" :class="checkoutFormErrors.phone ? 'border-rose-400 bg-rose-50/20' : 'border-slate-300'">
                                                    <p x-show="checkoutFormErrors.phone" x-text="checkoutFormErrors.phone" class="text-rose-500 text-[11px] font-semibold mt-1"></p>
                                                </div>
                                            </div>

                                            <template x-if="deliveryMethod === 'door'">
                                                <div class="space-y-3 pt-1">
                                                    <div>
                                                        <label class="block text-slate-600 font-bold mb-1">Địa chỉ cụ thể: <span class="text-rose-500">*</span></label>
                                                        <input type="text" x-model="checkoutShippingForm.address" @blur="checkoutShippingForm.touched.address = true" placeholder="Số nhà, tên đường" class="w-full bg-slate-50 border rounded-xl px-4 py-2.5 text-slate-800 font-semibold focus:outline-none focus:bg-white" :class="checkoutFormErrors.address ? 'border-rose-400 bg-rose-50/20' : 'border-slate-300'">
                                                        <p x-show="checkoutFormErrors.address" x-text="checkoutFormErrors.address" class="text-rose-500 text-[11px] font-semibold mt-1"></p>
                                                    </div>
                                                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
                                                        <div>
                                                            <label class="block text-slate-500 text-[11px] font-bold mb-1">Tỉnh / Thành phố: <span class="text-rose-500">*</span></label>
                                                            <select x-model="checkoutShippingForm.city" @change="onCityChange(); checkoutShippingForm.touched.city = true" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold focus:outline-none focus:bg-white">
                                                                <template x-for="p in vnProvinces" :key="p.name">
                                                                    <option :value="p.name" x-text="p.name"></option>
                                                                </template>
                                                            </select>
                                                        </div>
                                                        <div>
                                                            <label class="block text-slate-500 text-[11px] font-bold mb-1">Quận / Huyện: <span class="text-rose-500">*</span></label>
                                                            <select x-model="checkoutShippingForm.district" @change="onDistrictChange(); checkoutShippingForm.touched.district = true" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold focus:outline-none focus:bg-white">
                                                                <template x-for="d in currentProvinceDistricts" :key="d.name">
                                                                    <option :value="d.name" x-text="d.name"></option>
                                                                </template>
                                                            </select>
                                                        </div>
                                                        <div>
                                                            <label class="block text-slate-500 text-[11px] font-bold mb-1">Phường / Xã: <span class="text-rose-500">*</span></label>
                                                            <select x-model="checkoutShippingForm.ward" @change="checkoutShippingForm.touched.ward = true" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold focus:outline-none focus:bg-white">
                                                                <template x-for="w in currentDistrictWards" :key="w">
                                                                    <option :value="w" x-text="w"></option>
                                                                </template>
                                                            </select>
                                                        </div>
                                                    </div>
                                                </div>
                                            </template>
                                        </div>
                                    </div>

                                    <!-- Khối 2 - "Thông tin Lịch hẹn Dịch vụ" (Thẻ/Card có viền xám nhạt) -->
                                    <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm space-y-4">
                                        <div class="flex items-center justify-between pb-3 border-b border-slate-100">
                                            <div class="flex items-center gap-2.5">
                                                <span class="w-7 h-7 rounded-lg bg-blue-600 text-white font-black text-xs flex items-center justify-center shadow-sm">2</span>
                                                <h4 class="font-extrabold text-base text-slate-900">Thông tin Lịch hẹn Dịch vụ</h4>
                                            </div>
                                            <span class="text-xs text-blue-700 font-bold bg-blue-50 px-2.5 py-0.5 rounded-full border border-blue-200">Read-only</span>
                                        </div>

                                        <!-- Nội dung Read-only cho dịch vụ -->
                                        <div class="bg-slate-50 rounded-xl p-4 border border-slate-200 space-y-3 text-xs sm:text-sm">
                                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                                <div>
                                                    <span class="text-slate-500 text-xs font-bold block">Khách hàng đặt lịch:</span>
                                                    <strong class="text-slate-800" x-text="checkoutShippingForm.name || customerProfile.name"></strong>
                                                </div>
                                                <div>
                                                    <span class="text-slate-500 text-xs font-bold block">Số điện thoại liên hệ:</span>
                                                    <strong class="text-slate-800 font-mono" x-text="checkoutShippingForm.phone || customerProfile.phone"></strong>
                                                </div>
                                            </div>
                                            <div class="pt-2 border-t border-slate-200">
                                                <span class="text-slate-500 text-xs font-bold block">Cơ sở thực hiện:</span>
                                                <div class="font-bold text-slate-900 flex items-center gap-2 mt-0.5">
                                                    <i class="fa-solid fa-location-dot text-rose-500"></i>
                                                    <span>Cơ sở Chính: 88 Nguyễn Thị Minh Khai, Phường Đa Kao, Quận 1, TPHCM</span>
                                                </div>
                                            </div>
                                            <div class="pt-2 border-t border-slate-200">
                                                <span class="text-slate-500 text-xs font-bold block">Đưa đón PetShip:</span>
                                                <template x-if="servicePetShipAddress">
                                                    <div class="font-semibold text-orange-700 flex items-center gap-2 mt-0.5">
                                                        <i class="fa-solid fa-van-shuttle text-orange-600"></i>
                                                        <span x-text="'Đón tại: ' + servicePetShipAddress"></span>
                                                    </div>
                                                </template>
                                                <template x-if="!servicePetShipAddress">
                                                    <div class="text-slate-600 flex items-center gap-2 mt-0.5">
                                                        <i class="fa-solid fa-person-walking text-slate-400"></i>
                                                        <span>Khách hàng tự đưa đón bé cưng tại Cơ sở 88 Nguyễn Thị Minh Khai</span>
                                                    </div>
                                                </template>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </template>

                            <!-- Thanh nút điều hướng dưới chân cột trái -->
                            <div class="pt-2 flex justify-between items-center">
                                <button @click="goToCartStep(1)" class="text-slate-500 hover:text-slate-800 text-xs font-bold flex items-center gap-1.5 transition">
                                    <i class="fa-solid fa-arrow-left"></i>
                                    <span>Quay lại giỏ hàng</span>
                                </button>
                                <button @click="proceedToPaymentStep()" class="py-3.5 px-7 rounded-2xl bg-orange-500 hover:bg-orange-600 text-white font-extrabold text-xs sm:text-sm transition shadow-lg shadow-orange-500/25 flex items-center gap-2">
                                    <span>Tiếp tục đến phương thức thanh toán</span>
                                    <i class="fa-solid fa-arrow-right text-xs"></i>
                                </button>
                            </div>
                        </div>

                        <!-- CỘT BÊN PHẢI: TÓM TẮT ĐƠN HÀNG, KHO VOUCHER & TOÁN THANH TOÁN (CHECKOUT MATH) -->
                        <div class="space-y-4">
                            <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                                <div class="flex items-center justify-between pb-2 border-b border-slate-100">
                                    <h4 class="font-extrabold text-sm text-slate-800">Đơn hàng của bạn</h4>
                                    <span class="text-xs text-slate-400 font-bold" x-text="cart.length + ' mục'"></span>
                                </div>

                                <!-- Danh sách sản phẩm / dịch vụ trong giỏ -->
                                <div class="space-y-3 max-h-56 overflow-y-auto pr-1">
                                    <template x-for="(item, cidx) in cart" :key="cidx">
                                        <div class="flex items-center justify-between text-xs py-1 border-b border-slate-50">
                                            <div class="flex items-center gap-2.5">
                                                <img :src="item.image || item.img || getItemImage(item)" @error="$event.target.src='https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=300&q=80'" class="w-10 h-10 rounded-lg object-cover border border-slate-100 flex-shrink-0">
                                                <div>
                                                    <p class="font-bold text-slate-800 line-clamp-1 max-w-[140px]" x-text="item.name"></p>
                                                    <div class="flex items-center gap-1.5 text-[11px] text-slate-400">
                                                        <span x-text="'SL: x' + (item.qty || item.quantity || 1)"></span>
                                                        <template x-if="item.isService">
                                                            <span class="px-1.5 py-0.2 bg-blue-50 text-blue-700 font-bold rounded text-[10px]">Dịch vụ</span>
                                                        </template>
                                                        <template x-if="!item.isService">
                                                            <span class="px-1.5 py-0.2 bg-orange-50 text-orange-700 font-bold rounded text-[10px]">Sản phẩm</span>
                                                        </template>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="text-right">
                                                <span class="font-extrabold text-slate-900" x-text="formatCurrency((item.price || item.totalCost || 0) * (item.qty || item.quantity || 1))"></span>
                                                <template x-if="isHotelItem(item)">
                                                    <span class="block text-[10px] text-orange-600 font-semibold italic">Cọc 50%</span>
                                                </template>
                                            </div>
                                        </div>
                                    </template>
                                </div>

                                <!-- KHỐI COMPONENT CHỌN MÃ KHUYẾN MÃI (TICKET STYLE COMPONENT - YÊU CẦU 3.1) -->
                                <div class="pt-2">
                                    <div @click="openVoucherWallet()" class="p-3.5 rounded-2xl border-2 border-dashed border-orange-300 bg-orange-50/50 hover:bg-orange-50 cursor-pointer transition flex items-center justify-between group">
                                        <div class="flex items-center gap-3">
                                            <div class="w-9 h-9 rounded-xl bg-orange-500 text-white flex items-center justify-center font-bold text-base shadow-sm group-hover:scale-105 transition">
                                                <i class="fa-solid fa-ticket"></i>
                                            </div>
                                            <div>
                                                <div class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
                                                    <span>PetCare Voucher</span>
                                                    <span class="text-[9px] bg-orange-100 text-orange-800 font-bold px-1.5 py-0.5 rounded">Kho Voucher</span>
                                                </div>
                                                <template x-if="!hasAppliedVouchers">
                                                    <p class="text-[11px] text-slate-500 font-medium mt-0.5">Chọn hoặc nhập mã khuyến mãi</p>
                                                </template>
                                                <template x-if="hasAppliedVouchers">
                                                    <div class="flex flex-wrap gap-1 mt-1">
                                                        <template x-if="appliedVouchers.shipping">
                                                            <span class="inline-flex items-center gap-1 bg-blue-100 text-blue-800 text-[10px] font-bold px-2 py-0.5 rounded-md border border-blue-200">
                                                                <i class="fa-solid fa-truck-fast text-[9px]"></i>
                                                                <span x-text="appliedVouchers.shipping.code"></span>
                                                                <button type="button" @click.stop="removeVoucher('shipping')" class="text-blue-600 hover:text-blue-900 font-black ml-1 text-xs">&times;</button>
                                                            </span>
                                                        </template>
                                                        <template x-if="appliedVouchers.order">
                                                            <span class="inline-flex items-center gap-1 bg-emerald-100 text-emerald-800 text-[10px] font-bold px-2 py-0.5 rounded-md border border-emerald-200">
                                                                <i class="fa-solid fa-tag text-[9px]"></i>
                                                                <span x-text="appliedVouchers.order.code"></span>
                                                                <button type="button" @click.stop="removeVoucher('order')" class="text-emerald-600 hover:text-emerald-900 font-black ml-1 text-xs">&times;</button>
                                                            </span>
                                                        </template>
                                                    </div>
                                                </template>
                                            </div>
                                        </div>
                                        <div class="flex items-center gap-1 text-xs font-bold text-orange-600 group-hover:translate-x-1 transition">
                                            <span x-text="hasAppliedVouchers ? 'Đổi mã' : 'Chọn'"></span>
                                            <i class="fa-solid fa-chevron-right text-[10px]"></i>
                                        </div>
                                    </div>
                                </div>

                                <!-- BẢNG TÍNH TIỀN MINH BẠCH (CHECKOUT MATH - YÊU CẦU 1.4, 1.5, 3.4) -->
                                <div class="pt-3 border-t border-slate-100 space-y-2 text-xs">
                                    <!-- Dòng 1: Tạm tính -->
                                    <div class="flex justify-between text-slate-600">
                                        <span>Tạm tính (Hàng & Dịch vụ):</span>
                                        <span class="font-bold text-slate-800" x-text="formatCurrency(cartSubtotal)"></span>
                                    </div>

                                    <!-- Dòng 2: Phí vận chuyển (Chỉ tính khi hasProduct && deliveryMethod === 'door') -->
                                    <div class="flex justify-between text-slate-600">
                                        <span>Phí vận chuyển:</span>
                                        <template x-if="effectiveShippingFee > 0">
                                            <span class="font-bold text-slate-800" x-text="formatCurrency(effectiveShippingFee)"></span>
                                        </template>
                                        <template x-if="effectiveShippingFee === 0">
                                            <span class="font-bold text-emerald-600">Miễn phí</span>
                                        </template>
                                    </div>

                                    <!-- Dòng 3: Giảm giá (Voucher) -->
                                    <template x-if="totalDiscount > 0">
                                        <div class="flex justify-between text-emerald-600 font-extrabold">
                                            <span class="flex items-center gap-1">
                                                <i class="fa-solid fa-circle-check text-[10px]"></i>
                                                <span>Giảm giá Voucher:</span>
                                            </span>
                                            <span x-text="'-' + formatCurrency(totalDiscount)"></span>
                                        </div>
                                    </template>

                                    <!-- Dòng 4: Tổng giá trị đơn hàng (grandTotal - Màu đen/xám, font thường) -->
                                    <div class="flex justify-between text-slate-700 pt-1 border-t border-slate-100">
                                        <span>Tổng giá trị đơn hàng:</span>
                                        <span class="font-bold text-slate-900" x-text="formatCurrency(grandTotal)"></span>
                                    </div>

                                    <!-- Dòng 5: TỔNG THANH TOÁN HIỆN TẠI (currentPayment - Màu cam, in đậm, to nhất) -->
                                    <div class="pt-2 border-t border-dashed border-orange-200">
                                        <div class="flex justify-between items-baseline">
                                            <span class="text-xs font-bold text-slate-900 uppercase">TỔNG THANH TOÁN HIỆN TẠI:</span>
                                            <span class="text-xl font-black text-orange-600" x-text="formatCurrency(currentPayment)"></span>
                                        </div>
                                        <p class="text-[10px] text-slate-400 italic text-right mt-0.5">Số tiền thực tế thanh toán lúc này</p>
                                    </div>

                                    <!-- Dòng 6: Số tiền thu sau tại cơ sở (remainingBalance - Màu xám, in nghiêng, font nhỏ) -->
                                    <template x-if="hasHotel && remainingBalance > 0">
                                        <div class="flex justify-between text-[11px] text-slate-500 italic pt-1">
                                            <span>Số tiền thu sau tại cơ sở:</span>
                                            <span class="font-semibold" x-text="formatCurrency(remainingBalance)"></span>
                                        </div>
                                    </template>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- BƯỚC 3: PHƯƠNG THỨC THANH TOÁN (PAYMENT UI & ACCORDION) -->
                <div x-show="cartStep === 3" class="space-y-6">
                    <div class="py-3 border-b border-slate-200 flex items-center gap-2 text-xs sm:text-sm font-bold text-slate-500">
                        <span class="text-slate-400 hover:text-orange-600 cursor-pointer flex items-center gap-1" @click="goToCartStep(1)">
                            <i class="fa-solid fa-cart-shopping text-xs"></i>
                            <span>1. Giỏ hàng</span>
                        </span>
                        <i class="fa-solid fa-chevron-right text-[10px] text-slate-300"></i>
                        <span class="text-slate-400 hover:text-orange-600 cursor-pointer flex items-center gap-1" @click="goToCartStep(2)">
                            <i class="fa-solid fa-truck-ramp-box text-xs"></i>
                            <span>2. Thông tin nhận hàng & Lịch hẹn</span>
                        </span>
                        <i class="fa-solid fa-chevron-right text-[10px] text-slate-300"></i>
                        <span class="text-orange-600 font-extrabold flex items-center gap-1 bg-orange-50 px-2.5 py-1 rounded-lg">
                            <i class="fa-solid fa-credit-card text-xs"></i>
                            <span>3. Phương thức thanh toán</span>
                        </span>
                    </div>

                    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                        <!-- Cột trái: Accordion các phương thức thanh toán -->
                        <div class="lg:col-span-2 bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-6">
                            
                            <!-- Thông tin tóm tắt phương thức vận chuyển -->
                            <div class="space-y-2">
                                <h4 class="font-extrabold text-sm text-slate-800 uppercase tracking-wider">Hình thức nhận hàng & Địa điểm</h4>
                                <div class="p-4 rounded-2xl border border-slate-200 bg-slate-50 flex items-center justify-between">
                                    <div class="flex items-center gap-2.5 text-xs sm:text-sm">
                                        <i class="fa-solid fa-truck-fast text-orange-600 text-base"></i>
                                        <div>
                                            <template x-if="hasProduct && deliveryMethod === 'door'">
                                                <span class="font-bold text-slate-800">Giao tận nơi: <span class="font-normal" x-text="checkoutShippingForm.address + ', ' + checkoutShippingForm.ward + ', ' + checkoutShippingForm.district + ', ' + checkoutShippingForm.city"></span></span>
                                            </template>
                                            <template x-if="hasProduct && deliveryMethod === 'store'">
                                                <span class="font-bold text-slate-800">Nhận tại shop: <span class="font-normal">88 Nguyễn Thị Minh Khai, Q1, TP.HCM</span></span>
                                            </template>
                                            <template x-if="!hasProduct && hasService">
                                                <span class="font-bold text-slate-800">Lịch hẹn dịch vụ: <span class="font-normal">88 Nguyễn Thị Minh Khai (PetShip: <span x-text="servicePetShipAddress || 'Khách tự đưa đón'"></span>)</span></span>
                                            </template>
                                        </div>
                                    </div>
                                    <span class="font-bold text-slate-900 text-xs sm:text-sm" x-text="effectiveShippingFee > 0 ? formatCurrency(effectiveShippingFee) : '0 đ'"></span>
                                </div>
                            </div>

                            <!-- ACCORDION PHƯƠNG THỨC THANH TOÁN (YÊU CẦU 2.2) -->
                            <div class="space-y-3">
                                <h4 class="font-extrabold text-sm text-slate-800 uppercase tracking-wider">Chọn phương thức thanh toán</h4>
                                
                                <!-- 1. Chuyển khoản VietQR MB Bank (Khuyên dùng - Dynamic VietQR) -->
                                <div class="rounded-2xl border transition overflow-hidden" :class="paymentMethod === 'vietqr' ? 'border-orange-500 bg-orange-50/20 shadow-sm' : 'border-slate-200'">
                                    <label class="p-4 cursor-pointer flex items-center justify-between">
                                        <div class="flex items-center gap-3">
                                            <input type="radio" value="vietqr" x-model="paymentMethod" class="text-orange-500">
                                            <div>
                                                <div class="flex items-center gap-2">
                                                    <span class="font-extrabold text-xs sm:text-sm text-slate-900">Chuyển khoản VietQR (MB Bank)</span>
                                                    <span class="px-2 py-0.5 bg-emerald-100 text-emerald-800 font-bold text-[10px] rounded-full">Xác thực tự động</span>
                                                </div>
                                                <span class="text-slate-400 text-[11px] block mt-0.5">Tự động điền số tiền & cú pháp chuyển khoản bằng Dynamic QR</span>
                                            </div>
                                        </div>
                                        <i class="fa-solid fa-qrcode text-orange-600 text-lg"></i>
                                    </label>

                                    <!-- Chi tiết VietQR Accordion khi chọn -->
                                    <template x-if="paymentMethod === 'vietqr'">
                                        <div class="p-4 sm:p-5 bg-white border-t border-orange-200 space-y-4">
                                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
                                                <!-- Mã QR động (VietQR API) -->
                                                <div class="text-center p-3 bg-slate-50 rounded-2xl border border-slate-200 space-y-2">
                                                    <img :src="vietQrUrl" alt="VietQR PetCare360" class="w-48 h-48 mx-auto rounded-xl border-2 border-orange-200 shadow p-1 bg-white object-contain">
                                                    <p class="text-[11px] text-slate-500 font-medium">Quét bằng ứng dụng của bất kỳ ngân hàng nào</p>
                                                </div>

                                                <!-- Thông tin tài khoản -->
                                                <div class="space-y-2.5 text-xs text-slate-700">
                                                    <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-100">
                                                        <span class="text-slate-400 text-[11px] block">Ngân hàng thụ hưởng:</span>
                                                        <strong class="text-slate-900 text-sm">MB Bank (Quân Đội)</strong>
                                                    </div>
                                                    <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-100 flex items-center justify-between">
                                                        <div>
                                                            <span class="text-slate-400 text-[11px] block">Số tài khoản:</span>
                                                            <strong class="text-slate-900 text-sm font-mono tracking-wider">8888 9999 6666</strong>
                                                        </div>
                                                        <button type="button" @click="navigator.clipboard.writeText('888899996666'); alert('Đã sao chép STK: 888899996666');" class="px-2.5 py-1 bg-slate-200 hover:bg-slate-300 rounded-lg text-[10px] font-bold text-slate-700 transition">Sao chép</button>
                                                    </div>
                                                    <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-100">
                                                        <span class="text-slate-400 text-[11px] block">Chủ tài khoản:</span>
                                                        <strong class="text-slate-900 font-semibold">CT CP PETCARE360 VIETNAM</strong>
                                                    </div>
                                                    <div class="p-2.5 bg-orange-50 rounded-xl border border-orange-200 flex items-center justify-between">
                                                        <div>
                                                            <span class="text-orange-700 text-[11px] block font-bold">Số tiền chuyển:</span>
                                                            <strong class="text-orange-600 text-base font-black" x-text="formatCurrency(currentPayment)"></strong>
                                                        </div>
                                                        <div class="text-right">
                                                            <span class="text-slate-500 text-[11px] block">Nội dung:</span>
                                                            <strong class="font-mono text-slate-900 bg-white px-2 py-0.5 rounded border border-slate-200" x-text="'PETCARE360 ' + (completedOrderNumber ? completedOrderNumber.replace('#','') : 'DH157817')"></strong>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </template>
                                </div>

                                <!-- 2. Thẻ ATM nội địa & Internet Banking -->
                                <div class="rounded-2xl border transition overflow-hidden" :class="paymentMethod === 'atm' ? 'border-orange-500 bg-orange-50/20' : 'border-slate-200'">
                                    <label class="p-4 cursor-pointer flex items-center justify-between">
                                        <div class="flex items-center gap-3">
                                            <input type="radio" value="atm" x-model="paymentMethod" class="text-orange-500">
                                            <div>
                                                <span class="font-extrabold text-xs sm:text-sm text-slate-900 block">Thẻ ATM nội địa & Internet Banking</span>
                                                <span class="text-slate-400 text-[11px]">Hỗ trợ 40+ ngân hàng trong nước qua cổng Napas</span>
                                            </div>
                                        </div>
                                        <i class="fa-solid fa-building-columns text-slate-400 text-lg"></i>
                                    </label>
                                </div>

                                <!-- 3. Thẻ Quốc tế (Visa / Mastercard / JCB) -->
                                <div class="rounded-2xl border transition overflow-hidden" :class="paymentMethod === 'visa' ? 'border-orange-500 bg-orange-50/20' : 'border-slate-200'">
                                    <label class="p-4 cursor-pointer flex items-center justify-between">
                                        <div class="flex items-center gap-3">
                                            <input type="radio" value="visa" x-model="paymentMethod" class="text-orange-500">
                                            <div>
                                                <span class="font-extrabold text-xs sm:text-sm text-slate-900 block">Thẻ tín dụng / Ghi nợ quốc tế</span>
                                                <span class="text-slate-400 text-[11px]">Visa, MasterCard, JCB, American Express</span>
                                            </div>
                                        </div>
                                        <div class="flex gap-1.5 text-slate-400 text-base">
                                            <i class="fa-brands fa-cc-visa"></i>
                                            <i class="fa-brands fa-cc-mastercard"></i>
                                            <i class="fa-brands fa-cc-jcb"></i>
                                        </div>
                                    </label>
                                </div>

                                <!-- 4. Ví MoMo / ZaloPay -->
                                <div class="rounded-2xl border transition overflow-hidden" :class="paymentMethod === 'ewallet' ? 'border-orange-500 bg-orange-50/20' : 'border-slate-200'">
                                    <label class="p-4 cursor-pointer flex items-center justify-between">
                                        <div class="flex items-center gap-3">
                                            <input type="radio" value="ewallet" x-model="paymentMethod" class="text-orange-500">
                                            <div>
                                                <span class="font-extrabold text-xs sm:text-sm text-slate-900 block">Ví điện tử MoMo / ZaloPay</span>
                                                <span class="text-slate-400 text-[11px]">Thanh toán nhanh qua ví điện tử liên kết</span>
                                            </div>
                                        </div>
                                        <i class="fa-solid fa-wallet text-slate-400 text-lg"></i>
                                    </label>
                                </div>

                                <!-- 5. COD (Chỉ dành cho sản phẩm vật lý) -->
                                <div class="rounded-2xl border transition overflow-hidden" :class="hasService ? 'opacity-50 bg-slate-50 border-slate-200 cursor-not-allowed' : (paymentMethod === 'cod' ? 'border-orange-500 bg-orange-50/20' : 'border-slate-200')">
                                    <label class="p-4 flex items-center justify-between" :class="hasService ? 'cursor-not-allowed' : 'cursor-pointer'">
                                        <div class="flex items-center gap-3">
                                            <input type="radio" value="cod" x-model="paymentMethod" :disabled="hasService" class="text-orange-500">
                                            <div>
                                                <div class="flex items-center gap-2">
                                                    <span class="font-extrabold text-xs sm:text-sm text-slate-900">Thanh toán khi nhận hàng (COD)</span>
                                                    <template x-if="hasService">
                                                        <span class="px-2 py-0.5 bg-slate-200 text-slate-600 font-bold text-[10px] rounded-md">Không khả dụng</span>
                                                    </template>
                                                </div>
                                                <template x-if="hasService">
                                                    <span class="text-rose-500 text-[11px] block mt-0.5 font-medium">Chỉ áp dụng cho đơn 100% sản phẩm vật lý. Dịch vụ cần thanh toán hoặc đặt cọc online.</span>
                                                </template>
                                                <template x-if="!hasService">
                                                    <span class="text-slate-400 text-[11px] block mt-0.5">Kiểm tra hàng trước khi thanh toán tiền mặt</span>
                                                </template>
                                            </div>
                                        </div>
                                        <i class="fa-solid fa-hand-holding-dollar text-slate-400 text-lg"></i>
                                    </label>
                                </div>
                            </div>

                            <div class="pt-4 flex justify-between items-center">
                                <button @click="goToCartStep(2)" class="text-slate-500 hover:text-slate-800 text-xs font-bold flex items-center gap-1.5 transition">
                                    <i class="fa-solid fa-arrow-left"></i>
                                    <span>Quay lại thông tin giao hàng</span>
                                </button>
                                <!-- NÚT HOÀN TẤT ĐƠN HÀNG (SUBMIT CHECKOUT) -->
                                <button @click="finalizeOrder()" class="py-4 px-9 rounded-2xl bg-orange-500 hover:bg-orange-600 text-white font-black text-sm sm:text-base transition shadow-xl shadow-orange-500/30 flex items-center gap-2.5">
                                    <span>Hoàn tất đơn hàng</span>
                                    <i class="fa-solid fa-check"></i>
                                </button>
                            </div>
                        </div>

                        <!-- Cột phải: Tóm tắt thanh toán -->
                        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                            <h4 class="font-extrabold text-sm text-slate-800 pb-2 border-b border-slate-100">Tóm tắt thanh toán</h4>
                            <div class="space-y-2 text-xs text-slate-600">
                                <div class="flex justify-between">
                                    <span>Tạm tính (Hàng & Dịch vụ):</span>
                                    <span class="font-bold text-slate-800" x-text="formatCurrency(cartSubtotal)"></span>
                                </div>
                                <div class="flex justify-between">
                                    <span>Phí vận chuyển:</span>
                                    <span class="font-bold text-slate-800" x-text="effectiveShippingFee > 0 ? formatCurrency(effectiveShippingFee) : '0 đ'"></span>
                                </div>
                                <template x-if="totalDiscount > 0">
                                    <div class="flex justify-between text-emerald-600 font-extrabold">
                                        <span>Giảm giá:</span>
                                        <span x-text="'-' + formatCurrency(totalDiscount)"></span>
                                    </div>
                                </template>
                                <div class="flex justify-between text-slate-700 pt-1 border-t border-slate-100">
                                    <span>Tổng giá trị đơn:</span>
                                    <span class="font-bold text-slate-900" x-text="formatCurrency(grandTotal)"></span>
                                </div>
                                <div class="pt-2 border-t border-dashed border-orange-200">
                                    <div class="flex justify-between items-baseline">
                                        <span class="text-xs font-bold text-slate-900 uppercase">TỔNG THANH TOÁN HIỆN TẠI:</span>
                                        <span class="text-xl font-black text-orange-600" x-text="formatCurrency(currentPayment)"></span>
                                    </div>
                                    <p class="text-[10px] text-slate-400 italic text-right mt-0.5">Số tiền thanh toán ngay lúc này</p>
                                </div>
                                <template x-if="hasHotel && remainingBalance > 0">
                                    <div class="flex justify-between text-[11px] text-slate-500 italic pt-1">
                                        <span>Số tiền thu sau tại cơ sở:</span>
                                        <span class="font-semibold" x-text="formatCurrency(remainingBalance)"></span>
                                    </div>
                                </template>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- BƯỚC 4: XÁC NHẬN ĐƠN HÀNG, GIỮ KHO 15 PHÚT, WEBHOOK & TẢI BIÊN LAI (YÊU CẦU 2.3) -->
                <div x-show="cartStep === 4" class="max-w-3xl mx-auto bg-white rounded-3xl p-6 sm:p-10 border border-slate-200 shadow-sm space-y-6 text-center animate-fadeIn">
                    
                    <!-- Icon trạng thái -->
                    <template x-if="!webhookSuccessReceived">
                        <div class="w-16 h-16 rounded-full bg-amber-100 text-amber-600 flex items-center justify-center text-3xl mx-auto shadow-md">
                            <i class="fa-solid fa-clock"></i>
                        </div>
                    </template>
                    <template x-if="webhookSuccessReceived">
                        <div class="w-16 h-16 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center text-3xl mx-auto shadow-md">
                            <i class="fa-solid fa-check"></i>
                        </div>
                    </template>

                    <div>
                        <h2 class="text-2xl sm:text-3xl font-black text-slate-900" x-text="webhookSuccessReceived ? 'Thanh toán thành công!' : 'Đặt hàng & Giữ chỗ thành công!'"></h2>
                        <p class="text-sm text-slate-500 mt-1">Cảm ơn bạn đã tin tưởng dịch vụ và sản phẩm của PetCare360!</p>
                        <span class="inline-block mt-2 font-mono font-extrabold text-brand-700 bg-brand-50 px-4 py-1.5 rounded-full text-sm border border-brand-200" x-text="'Mã đơn hàng: ' + (currentPendingOrder ? currentPendingOrder.orderCode : completedOrderNumber)"></span>
                    </div>

                    <!-- BANNER COUNTDOWN TIMER GIỮ KHO 15 PHÚT -->
                    <template x-if="!webhookSuccessReceived">
                        <div class="p-4 bg-amber-50 rounded-2xl border border-amber-200 text-center space-y-2">
                            <div class="flex items-center justify-center gap-2 text-amber-800 font-extrabold text-sm">
                                <i class="fa-solid fa-hourglass-half text-amber-600 animate-spin"></i>
                                <span>TỒN KHO ĐƯỢC GIỮ TẠM TRONG:</span>
                                <span class="text-xl font-mono font-black text-orange-600" x-text="formattedCountdown"></span>
                            </div>
                            <p class="text-xs text-amber-700 max-w-lg mx-auto">Vui lòng hoàn tất chuyển khoản trong vòng 15 phút để hệ thống Gateway xác thực Webhook và trừ kho vĩnh viễn.</p>
                        </div>
                    </template>

                    <!-- BANNER WEBHOOK THÀNH CÔNG -->
                    <template x-if="webhookSuccessReceived">
                        <div class="p-4 bg-emerald-50 rounded-2xl border border-emerald-200 text-center space-y-1">
                            <div class="flex items-center justify-center gap-2 text-emerald-800 font-extrabold text-sm">
                                <i class="fa-solid fa-circle-check text-emerald-600 text-base"></i>
                                <span>XÁC THỰC THANH TOÁN WEBHOOK THÀNH CÔNG!</span>
                            </div>
                            <p class="text-xs text-emerald-700">Đơn hàng đã được xác nhận, kho hàng đã trừ vĩnh viễn. Nhân viên PetCare360 sẽ sớm liên hệ phục vụ quý khách.</p>
                        </div>
                    </template>

                    <!-- KHỐI CHUYỂN KHOẢN VIETQR ĐỘNG -->
                    <div class="p-5 bg-slate-50 rounded-2xl border border-slate-200 text-left text-xs space-y-3">
                        <h4 class="font-extrabold text-slate-800 uppercase tracking-wider text-xs flex items-center justify-between">
                            <span>Thông tin đơn hàng & Chuyển khoản</span>
                            <span class="font-bold text-orange-600" x-text="currentPendingOrder ? currentPendingOrder.statusText : 'Chờ thanh toán'"></span>
                        </h4>

                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-1 items-center">
                            <!-- VietQR Code -->
                            <div class="p-3 bg-white rounded-xl border border-slate-200 text-center space-y-1.5 shadow-sm">
                                <img :src="vietQrUrl" class="w-40 h-40 mx-auto rounded-lg border border-orange-100 p-0.5 object-contain">
                                <p class="text-[11px] text-slate-500 font-medium">Mã VietQR động tự động điền STK & Số tiền</p>
                            </div>

                            <!-- Chi tiết đơn -->
                            <div class="space-y-1.5 text-xs text-slate-700">
                                <p>• Người nhận: <strong class="text-slate-900" x-text="checkoutShippingForm.name"></strong> - SĐT: <strong class="text-slate-900 font-mono" x-text="checkoutShippingForm.phone"></strong></p>
                                <p>• Địa chỉ: <strong class="text-slate-800" x-text="checkoutShippingForm.address ? (checkoutShippingForm.address + ', ' + checkoutShippingForm.ward + ', ' + checkoutShippingForm.district + ', ' + checkoutShippingForm.city) : 'Cơ sở Chính 88 NTMK'"></strong></p>
                                <p>• Ngân hàng: <strong>MB Bank (8888 9999 6666 - CT CP PETCARE360 VIETNAM)</strong></p>
                                <p>• Cú pháp CK: <strong class="font-mono bg-white px-2 py-0.5 rounded border text-slate-900" x-text="'PETCARE360 ' + (currentPendingOrder ? currentPendingOrder.orderCode.replace('#','') : 'DH157817')"></strong></p>
                                <p class="pt-1">• Số tiền thanh toán ngay: <strong class="text-orange-600 text-base font-black" x-text="formatCurrency(currentPendingOrder ? currentPendingOrder.amount_paid : currentPayment)"></strong></p>
                                <template x-if="currentPendingOrder && currentPendingOrder.balance_due > 0">
                                    <p class="text-[11px] text-slate-500 italic">• Số tiền thu sau tại cơ sở: <strong class="text-slate-700 font-bold" x-text="formatCurrency(currentPendingOrder.balance_due)"></strong></p>
                                </template>
                            </div>
                        </div>

                        <!-- KHỐI GIẢ LẬP WEBHOOK & TẢI BIÊN LAI THỦ CÔNG (YÊU CẦU 2.3) -->
                        <div class="pt-3 border-t border-slate-200 space-y-2">
                            <div class="flex flex-col sm:flex-row gap-2.5 items-center justify-between">
                                <!-- Nút Giả Lập Webhook -->
                                <button type="button" @click="simulatePaymentWebhook()" class="w-full sm:w-auto px-4 py-2.5 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-700 hover:to-teal-700 text-white font-extrabold text-xs rounded-xl shadow transition flex items-center justify-center gap-1.5">
                                    <i class="fa-solid fa-bolt"></i>
                                    <span>⚡ Giả lập Webhook: Thanh toán thành công (Test Gateway)</span>
                                </button>

                                <!-- Nút Tải Biên Lai / Duyệt Thủ Công -->
                                <div class="flex items-center gap-2 w-full sm:w-auto">
                                    <label class="cursor-pointer px-3.5 py-2.5 bg-slate-200 hover:bg-slate-300 text-slate-700 font-bold text-xs rounded-xl transition flex items-center gap-1.5 flex-1 sm:flex-initial justify-center">
                                        <i class="fa-solid fa-upload"></i>
                                        <span>Tải biên lai</span>
                                        <input type="file" accept="image/*" @change="handleReceiptUpload($event)" class="hidden">
                                    </label>
                                    <button type="button" @click="adminManualApprove()" class="px-3.5 py-2.5 bg-amber-500 hover:bg-amber-600 text-white font-bold text-xs rounded-xl transition flex-1 sm:flex-initial">
                                        Admin duyệt tay
                                    </button>
                                </div>
                            </div>
                            <template x-if="uploadedReceiptUrl">
                                <div class="p-2.5 bg-white rounded-xl border border-slate-200 flex items-center gap-3">
                                    <img :src="uploadedReceiptUrl" class="w-12 h-12 object-cover rounded-lg border">
                                    <div>
                                        <p class="text-xs font-bold text-slate-800">Đã đính kèm ảnh biên lai giao dịch</p>
                                        <span class="text-[10px] text-slate-400">Admin có thể kiểm tra và duyệt trừ kho ngay</span>
                                    </div>
                                </div>
                            </template>
                        </div>
                    </div>

                    <div class="pt-2 text-xs text-slate-500">
                        Cần hỗ trợ đơn hàng? Hotline CSKH 24/7: <strong class="text-orange-600">1900 6888 (Phím 1)</strong>
                    </div>

                    <div class="pt-4 flex justify-center gap-3">
                        <button @click="activeCustomerTab = 'shop'; cartStep = 1;" class="px-6 py-3 rounded-2xl bg-orange-500 hover:bg-orange-600 text-white font-extrabold text-xs sm:text-sm transition shadow-lg shadow-orange-500/20">
                            Tiếp tục mua sắm
                        </button>
                        <button @click="activeCustomerTab = 'orders'; cartStep = 1;" class="px-6 py-3 rounded-2xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs sm:text-sm transition">
                            Xem lịch sử đơn hàng
                        </button>
                    </div>
                </div>

                <!-- BƯỚC 5: QUẢN LÝ ĐƠN HÀNG SAU KHI ĐẶT (LỊCH SỬ ĐƠN HÀNG TRONG TÀI KHOẢN) -->
                <div x-show="cartStep === 5" class="space-y-6">
                    <div class="flex items-center justify-between pb-3 border-b border-slate-200">
                        <h2 class="text-2xl font-black text-slate-900">Tài Khoản Của Bạn</h2>
                        <button @click="goToCartStep(1)" class="text-xs text-brand-600 font-bold hover:underline">Quay lại giỏ hàng</button>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
                        <!-- Menu bên trái (Sidebar) -->
                        <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-2 text-xs font-semibold">
                            <button @click="activeCustomerTab = 'account'" class="w-full py-2.5 px-3 rounded-xl bg-brand-50 text-brand-700 text-left">Thông tin tài khoản</button>
                            <button @click="activeCustomerTab = 'account'" class="w-full py-2.5 px-3 rounded-xl text-slate-600 hover:bg-slate-50 text-left">Danh sách địa chỉ</button>
                            <button @click="logout()" class="w-full py-2.5 px-3 rounded-xl text-rose-600 hover:bg-rose-50 text-left">Đăng xuất</button>
                        </div>

                        <!-- Khung "DANH SÁCH ĐƠN HÀNG MỚI NHẤT" -->
                        <div class="md:col-span-3 bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                            <h3 class="font-extrabold text-base text-slate-900">DANH SÁCH ĐƠN HÀNG MỚI NHẤT</h3>
                            <div class="overflow-x-auto">
                                <table class="w-full text-left text-xs border-collapse">
                                    <thead>
                                        <tr class="bg-slate-50 text-slate-700 font-bold border-b border-slate-200">
                                            <th class="py-3 px-3">Mã đơn hàng</th>
                                            <th class="py-3 px-3">Ngày đặt</th>
                                            <th class="py-3 px-3">Thành tiền</th>
                                            <th class="py-3 px-3">Trạng thái thanh toán</th>
                                            <th class="py-3 px-3">Vận chuyển</th>
                                        </tr>
                                    </thead>
                                    <tbody class="divide-y divide-slate-100">
                                        <template x-for="ord in customerOrdersEnhanced" :key="ord.id">
                                            <tr class="hover:bg-slate-50">
                                                <td class="py-3 px-3 font-bold text-brand-600 cursor-pointer hover:underline" @click="openOrderCheckoutSummary(ord)" x-text="ord.orderCode"></td>
                                                <td class="py-3 px-3 text-slate-500" x-text="ord.date"></td>
                                                <td class="py-3 px-3 font-bold text-orange-600" x-text="formatCurrency(ord.total)"></td>
                                                <td class="py-3 px-3">
                                                    <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-100 text-amber-800" x-text="ord.paymentStatus"></span>
                                                </td>
                                                <td class="py-3 px-3">
                                                    <span :class="ord.badgeColor" class="px-2 py-0.5 rounded-full text-[10px] font-bold border" x-text="ord.statusText"></span>
                                                </td>
                                            </tr>
                                        </template>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </main>

        <!-- Footer Chung -->
        <footer class="bg-slate-900 text-white pt-12 pb-8 border-t border-slate-800 mt-12">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-5 gap-8">
                <div class="space-y-3 md:col-span-2">
                    <div class="flex items-center gap-2">
                        <div class="w-8 h-8 rounded-xl bg-brand-500 flex items-center justify-center text-white">
                            <i class="fa-solid fa-paw"></i>
                        </div>
                        <span class="text-lg font-bold">PetCare360</span>
                    </div>
                    <p class="text-xs text-slate-300 max-w-sm leading-relaxed">PetCare360 - Điểm tựa yêu thương & hệ sinh thái chăm sóc y tế, dinh dưỡng trọn đời cho thú cưng. Cam kết y đức thú y chuẩn mực, tận tâm như người thân trong gia đình.</p>
                    <div class="pt-2 text-xs text-slate-400 space-y-1">
                        <p><i class="fa-solid fa-phone mr-1.5 text-brand-400"></i> Hotline Cấp Cứu 24/7: 1900 6888 (Phím 1)</p>
                        <p><i class="fa-solid fa-envelope mr-1.5 text-brand-400"></i> Email CSKH: cskh@petcare360.vn</p>
                        <p><i class="fa-solid fa-location-dot mr-1.5 text-brand-400"></i> Trụ sở chính: 125 Hoàng Quốc Việt, Cầu Giấy, Hà Nội</p>
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
            <button @click="activeCustomerTab = 'shop'" :class="activeCustomerTab === 'shop' ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1">
                <i class="fa-solid fa-box-open text-base mb-0.5"></i>
                <span>Sản phẩm</span>
            </button>
            <button @click="activeCustomerTab = 'booking'" :class="activeCustomerTab === 'booking' ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1">
                <i class="fa-solid fa-scissors text-base mb-0.5"></i>
                <span>Dịch vụ</span>
            </button>
            <button @click="activeCustomerTab = 'petshare'" :class="activeCustomerTab === 'petshare' ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1">
                <i class="fa-solid fa-newspaper text-base mb-0.5"></i>
                <span>PetShare</span>
            </button>
            <button @click="activeCustomerTab = 'petshow'" :class="activeCustomerTab === 'petshow' ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1">
                <i class="fa-solid fa-video text-base mb-0.5 text-rose-500"></i>
                <span>PetShow</span>
            </button>
            <button @click="activeCustomerTab = 'orders'" :class="activeCustomerTab === 'orders' ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1 relative">
                <i class="fa-solid fa-receipt text-base mb-0.5"></i>
                <span>Đơn hàng</span>
                <span x-show="customerOrdersEnhanced.length > 0" class="absolute top-0 right-1 w-2 h-2 bg-amber-500 rounded-full"></span>
            </button>
            <template x-if="isAuth">
                <button @click="activeCustomerTab = 'account'" :class="(activeCustomerTab === 'account' || activeCustomerTab === 'profile') ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1">
                    <i class="fa-solid fa-user-gear text-base mb-0.5"></i>
                    <span>Tài khoản</span>
                </button>
            </template>
            <template x-if="!isAuth">
                <button @click="openLoginModal()" class="flex flex-col items-center p-1 text-slate-500 hover:text-brand-600">
                    <i class="fa-solid fa-right-to-bracket text-base mb-0.5"></i>
                    <span>Đăng nhập</span>
                </button>
            </template>
        </div>
    </div>
"""
