MODALS_HTML = '''<!-- ==================== CÁC MODAL HỆ THỐNG TOÀN DIỆN ==================== -->
<div id="system-modals-container">

    <!-- 1. MODAL ĐĂNG NHẬP (LOGIN MODAL) -->
    <div x-show="showLoginModal || loginModalOpen" x-cloak class="fixed inset-0 z-50 overflow-y-auto bg-slate-900/70 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-8 shadow-2xl border border-slate-100 relative animate-fadeIn">
            <button @click="showLoginModal = false; loginModalOpen = false;" class="absolute top-5 right-5 text-slate-400 hover:text-slate-600 w-9 h-9 rounded-full bg-slate-100 flex items-center justify-center transition-colors">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>
            
            <div class="text-center mb-6">
                <div class="w-16 h-16 bg-gradient-to-tr from-emerald-500 to-teal-400 rounded-2xl flex items-center justify-center mx-auto text-white text-3xl shadow-lg shadow-emerald-500/30 mb-3">
                    <i class="fa-solid fa-shield-cat"></i>
                </div>
                <h3 class="text-2xl font-black text-slate-800">Đăng Nhập PetCare360</h3>
                <p class="text-xs text-slate-500 mt-1">Đăng nhập tài khoản để quản lý thú cưng hoặc điều hành hệ thống</p>
            </div>

            <!-- Error banner -->
            <div x-show="loginError" x-cloak class="mb-4 p-3 bg-rose-50 border border-rose-200 rounded-xl text-rose-600 text-xs font-semibold flex items-center gap-2">
                <i class="fa-solid fa-triangle-exclamation text-rose-500"></i>
                <span x-text="loginError"></span>
            </div>

            <form @submit.prevent="handleLogin()" class="space-y-4">
                <div>
                    <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">Tên đăng nhập / Số điện thoại</label>
                    <div class="relative">
                        <i class="fa-solid fa-user absolute left-3.5 top-3.5 text-slate-400 text-sm"></i>
                        <input type="text" x-model="loginUsername" placeholder="Nhập tên đăng nhập..." class="w-full pl-10 pr-4 py-2.5 rounded-xl border border-slate-200 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 font-medium">
                    </div>
                </div>

                <div>
                    <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">Mật khẩu</label>
                    <div class="relative">
                        <i class="fa-solid fa-lock absolute left-3.5 top-3.5 text-slate-400 text-sm"></i>
                        <input type="password" x-model="loginPassword" placeholder="Nhập mật khẩu..." class="w-full pl-10 pr-4 py-2.5 rounded-xl border border-slate-200 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 font-medium">
                    </div>
                </div>

                <div class="flex items-center justify-between text-xs text-slate-500">
                    <label class="flex items-center gap-2 cursor-pointer">
                        <input type="checkbox" checked class="rounded text-emerald-600 focus:ring-0">
                        <span>Ghi nhớ đăng nhập</span>
                    </label>
                    <a href="javascript:void(0)" @click="alert('Vui lòng liên hệ CSKH qua hotline 1900 6868 để lấy lại mật khẩu.')" class="text-emerald-600 font-semibold hover:underline">Quên mật khẩu?</a>
                </div>

                <button type="submit" class="w-full py-3 bg-gradient-to-r from-emerald-600 to-teal-500 hover:from-emerald-700 hover:to-teal-600 text-white font-bold rounded-xl shadow-lg shadow-emerald-600/30 transition-all transform active:scale-95 text-sm flex items-center justify-center gap-2">
                    <i class="fa-solid fa-right-to-bracket"></i>
                    <span>Đăng Nhập Ngay</span>
                </button>
            </form>

            <div class="mt-6 pt-5 border-t border-slate-100 text-center">
                <div class="bg-amber-50 rounded-xl p-3 border border-amber-200 text-left text-xs text-amber-800 space-y-1">
                    <p class="font-bold flex items-center gap-1.5"><i class="fa-solid fa-lightbulb text-amber-500"></i> Hướng dẫn tài khoản Demo:</p>
                    <p>• <strong>Khách hàng:</strong> Điền bất kỳ tên và mật khẩu nào để đăng nhập.</p>
                    <p>• <strong>Quản trị viên (Admin):</strong> Tên đăng nhập: <code class="bg-amber-100 px-1 py-0.5 rounded font-mono font-bold text-amber-900">teamnhonho</code> | Mật khẩu: <code class="bg-amber-100 px-1 py-0.5 rounded font-mono font-bold text-amber-900">noletdtu$2006</code></p>
                </div>
            </div>
        </div>
    </div>

    <!-- 2. MODAL CHI TIẾT DỊCH VỤ (SERVICE DETAIL MODAL - ĐẦY ĐỦ 12 DỊCH VỤ) -->
    <div x-show="selectedServiceModal" x-cloak class="fixed inset-0 z-50 overflow-y-auto bg-slate-900/70 backdrop-blur-sm flex items-center justify-center p-4">
        <template x-if="selectedServiceModal">
            <div class="bg-white rounded-3xl max-w-2xl w-full max-h-[90vh] overflow-y-auto shadow-2xl border border-slate-100 relative animate-fadeIn">
                <button @click="selectedServiceModal = null" class="absolute top-4 right-4 z-10 text-slate-500 hover:text-slate-800 w-9 h-9 rounded-full bg-white/80 backdrop-blur-md flex items-center justify-center shadow transition-colors">
                    <i class="fa-solid fa-xmark text-lg"></i>
                </button>

                <div class="relative h-64 overflow-hidden rounded-t-3xl">
                    <img :src="selectedServiceModal.img || selectedServiceModal.image" :alt="selectedServiceModal.name" class="w-full h-full object-cover">
                    <div class="absolute inset-0 bg-gradient-to-t from-slate-900/80 via-transparent to-black/20"></div>
                    <div class="absolute bottom-4 left-6 right-6 text-white">
                        <span class="px-2.5 py-1 bg-emerald-500 text-white text-[11px] font-black rounded-lg uppercase tracking-wider inline-block mb-2 shadow" x-text="selectedServiceModal.category"></span>
                        <h3 class="text-2xl font-black" x-text="selectedServiceModal.name"></h3>
                        <p class="text-xs text-slate-200 mt-1 line-clamp-2" x-text="selectedServiceModal.desc || selectedServiceModal.description"></p>
                    </div>
                </div>

                <div class="p-6 space-y-6">
                    <!-- Key stats -->
                    <div class="grid grid-cols-3 gap-3 bg-slate-50 rounded-2xl p-4 border border-slate-100 text-center">
                        <div>
                            <span class="block text-[11px] text-slate-400 font-bold uppercase">Giá dịch vụ</span>
                            <span class="text-base font-black text-emerald-600" x-text="formatCurrency(selectedServiceModal.price)"></span>
                        </div>
                        <div class="border-x border-slate-200">
                            <span class="block text-[11px] text-slate-400 font-bold uppercase">Thời gian thực hiện</span>
                            <span class="text-sm font-bold text-slate-700" x-text="selectedServiceModal.duration"></span>
                        </div>
                        <div>
                            <span class="block text-[11px] text-slate-400 font-bold uppercase">Chuyên viên phụ trách</span>
                            <span class="text-sm font-bold text-slate-700" x-text="selectedServiceModal.expert || selectedServiceModal.doctor"></span>
                        </div>
                    </div>

                    <!-- 5-Step process -->
                    <div>
                        <h4 class="text-sm font-black text-slate-800 uppercase tracking-wider mb-3 flex items-center gap-2">
                            <i class="fa-solid fa-clipboard-check text-emerald-600"></i>
                            Quy trình chuẩn y khoa & chăm sóc 5 bước
                        </h4>
                        <div class="space-y-3">
                            <template x-for="(step, idx) in selectedServiceModal.steps" :key="idx">
                                <div class="flex items-start gap-3 p-3 rounded-xl bg-emerald-50/50 border border-emerald-100/60">
                                    <span class="w-6 h-6 rounded-full bg-emerald-600 text-white text-xs font-black flex items-center justify-center shrink-0 mt-0.5" x-text="idx + 1"></span>
                                    <div>
                                        <h5 class="text-xs font-bold text-slate-800" x-text="step.title"></h5>
                                        <p class="text-xs text-slate-500 mt-0.5" x-text="step.desc"></p>
                                    </div>
                                </div>
                            </template>
                        </div>
                    </div>

                    <!-- Highlights & Benefits -->
                    <div class="p-4 bg-amber-50/60 rounded-2xl border border-amber-200/60 space-y-2">
                        <h4 class="text-xs font-black text-amber-900 uppercase tracking-wider flex items-center gap-2">
                            <i class="fa-solid fa-award text-amber-600"></i> Cam kết chất lượng tại PetCare360
                        </h4>
                        <ul class="text-xs text-amber-800 space-y-1.5 list-disc list-inside">
                            <li>100% trang thiết bị hiện đại, tiệt trùng vô khuẩn trước mỗi ca chăm sóc</li>
                            <li>Dược mỹ phẩm thảo dược cao cấp dịu nhẹ, không gây kích ứng mắt hay da nhạy cảm</li>
                            <li>Bác sĩ thú y túc trực kiểm tra sức khỏe tổng quát ban đầu miễn phí</li>
                            <li>Hoàn tiền 100% nếu bé cưng không thoải mái hoặc có phản ứng bất thường</li>
                        </ul>
                    </div>

                    <!-- Buttons -->
                    <div class="flex items-center gap-3 pt-2">
                        <button @click="selectedServiceModal = null" class="w-1/3 py-3 border border-slate-200 text-slate-600 font-bold rounded-xl text-xs hover:bg-slate-50 transition-colors">
                            Đóng
                        </button>
                        <button @click="openBookingModalForService(selectedServiceModal); selectedServiceModal = null" class="w-2/3 py-3 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-xl text-xs shadow-lg shadow-emerald-600/30 transition-all flex items-center justify-center gap-2">
                            <i class="fa-solid fa-calendar-check"></i>
                            <span>Đặt Lịch Dịch Vụ Này Ngay</span>
                        </button>
                    </div>
                </div>
            </div>
        </template>
    </div>

    <!-- 3. MODAL ĐẶT LỊCH CHI TIẾT CHO DỊCH VỤ (BOOKING DETAIL MODAL - BẮT BUỘC TRƯỚC THANH TOÁN) -->
    <div x-show="showBookingDetailModal || bookingDetailModalOpen" x-cloak class="fixed inset-0 z-50 overflow-y-auto bg-slate-900/70 backdrop-blur-sm flex items-center justify-center p-4">
        <template x-if="bookingItem">
            <div class="bg-white rounded-3xl max-w-lg w-full p-6 shadow-2xl border border-slate-100 relative animate-fadeIn">
                <button @click="showBookingDetailModal = false; bookingDetailModalOpen = false;" class="absolute top-4 right-4 text-slate-400 hover:text-slate-600 w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center transition-colors">
                    <i class="fa-solid fa-xmark"></i>
                </button>

                <div class="flex items-center gap-3 mb-5 pb-4 border-b border-slate-100">
                    <img :src="bookingItem.img || bookingItem.image" class="w-14 h-14 rounded-2xl object-cover shadow-sm">
                    <div>
                        <span class="text-[10px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full uppercase">Thông tin đặt lịch dịch vụ</span>
                        <h3 class="text-base font-black text-slate-800" x-text="bookingItem.name"></h3>
                        <p class="text-xs font-bold text-slate-500" x-text="formatCurrency(bookingItem.price)"></p>
                    </div>
                </div>

                <form @submit.prevent="saveBookingDetails()" class="space-y-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">
                            Chọn Thú Cưng Đến Sử Dụng Dịch Vụ <span class="text-rose-500">*</span>
                        </label>
                        <select x-model="bookingItem.selectedPet" required class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                            <option value="">-- Vui lòng chọn thú cưng của bạn --</option>
                            <template x-for="pet in pets" :key="pet.id">
                                <option :value="pet.name" x-text="pet.name + ' (' + pet.type + ' - ' + pet.breed + ')'"></option>
                            </template>
                            <option value="Thú cưng mới (chưa có hồ sơ)">+ Thú cưng mới (sẽ bổ sung tại phòng khám)</option>
                        </select>
                    </div>

                    <div class="grid grid-cols-2 gap-3">
                        <div>
                            <label class="block text-xs font-bold text-slate-700 mb-1">
                                Ngày Hẹn Làm Dịch Vụ <span class="text-rose-500">*</span>
                            </label>
                            <input type="date" x-model="bookingItem.bookingDate" required class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-700 mb-1">
                                Khung Giờ Đến <span class="text-rose-500">*</span>
                            </label>
                            <select x-model="bookingItem.bookingTime" required class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                                <option value="08:30">08:30 - Sáng sớm</option>
                                <option value="09:30">09:30 - Buổi sáng</option>
                                <option value="10:30">10:30 - Trưa</option>
                                <option value="14:00">14:00 - Đầu giờ chiều</option>
                                <option value="15:30">15:30 - Giữa chiều</option>
                                <option value="17:00">17:00 - Cuối chiều</option>
                                <option value="18:30">18:30 - Buổi tối</option>
                            </select>
                        </div>
                    </div>

                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">
                            Chi Nhánh Tiếp Nhận <span class="text-rose-500">*</span>
                        </label>
                        <select x-model="bookingItem.bookingBranch" required class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                            <option value="Chi nhánh Cầu Giấy (125 Hoàng Quốc Việt, Cầu Giấy, HN)">Chi nhánh Cầu Giấy (125 Hoàng Quốc Việt, HN)</option>
                            <option value="Chi nhánh Quận 7 (450 Nguyễn Thị Thập, P. Tân Quy, Q7, TP.HCM)">Chi nhánh Quận 7 (450 Nguyễn Thị Thập, Q7, TP.HCM)</option>
                            <option value="Chi nhánh Bình Thạnh (88 Bạch Đằng, P.24, Bình Thạnh, TP.HCM)">Chi nhánh Bình Thạnh (88 Bạch Đằng, Bình Thạnh, TP.HCM)</option>
                        </select>
                    </div>

                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">
                            Ghi Chú Chi Tiết Cho Bác Sĩ / Kỹ Thuật Viên
                        </label>
                        <textarea x-model="bookingItem.bookingNotes" rows="3" placeholder="Ví dụ: Bé sợ tiếng sấy kêu to, lông đang bị bết phần đuôi, cần cắt tỉa móng cẩn thận..." class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500"></textarea>
                    </div>

                    <div class="bg-amber-50 p-3 rounded-xl border border-amber-200 text-amber-800 text-[11px] leading-relaxed">
                        <i class="fa-solid fa-circle-info text-amber-600 mr-1"></i>
                        <strong>Lưu ý quan trọng:</strong> Hệ thống PetCare360 yêu cầu đầy đủ thông tin thú cưng và ngày hẹn để phân bổ bác sĩ và buồng dịch vụ vô khuẩn trước khi quý khách thanh toán đơn hàng.
                    </div>

                    <div class="flex items-center gap-3 pt-2">
                        <button type="button" @click="showBookingDetailModal = false; bookingDetailModalOpen = false;" class="w-1/3 py-2.5 border border-slate-200 text-slate-600 font-bold rounded-xl text-xs hover:bg-slate-50">
                            Hủy
                        </button>
                        <button type="submit" class="w-2/3 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-xl text-xs shadow-md shadow-emerald-600/30 transition-all flex items-center justify-center gap-2">
                            <i class="fa-solid fa-check"></i>
                            <span>Xác Nhận & Lưu Lịch Hẹn</span>
                        </button>
                    </div>
                </form>
            </div>
        </template>
    </div>

    <!-- 4. MODAL CHI TIẾT SẢN PHẨM (PRODUCT DETAIL MODAL - ĐẦY ĐỦ 12 SẢN PHẨM) -->
    <div x-show="selectedProductModal" x-cloak class="fixed inset-0 z-50 overflow-y-auto bg-slate-900/70 backdrop-blur-sm flex items-center justify-center p-4">
        <template x-if="selectedProductModal">
            <div class="bg-white rounded-3xl max-w-2xl w-full max-h-[90vh] overflow-y-auto shadow-2xl border border-slate-100 relative animate-fadeIn">
                <button @click="selectedProductModal = null" class="absolute top-4 right-4 z-10 text-slate-500 hover:text-slate-800 w-9 h-9 rounded-full bg-white/80 backdrop-blur-md flex items-center justify-center shadow transition-colors">
                    <i class="fa-solid fa-xmark text-lg"></i>
                </button>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 p-6">
                    <!-- Image -->
                    <div class="flex flex-col items-center justify-center bg-slate-50 rounded-2xl p-4 border border-slate-100">
                        <img :src="selectedProductModal.img || selectedProductModal.image" :alt="selectedProductModal.name" class="w-full max-h-64 object-contain rounded-xl hover:scale-105 transition-transform duration-300">
                        <div class="mt-4 flex items-center gap-2 text-xs text-emerald-600 font-semibold bg-emerald-50 px-3 py-1 rounded-full">
                            <i class="fa-solid fa-circle-check"></i>
                            <span>Hàng chính hãng 100% - Đổi trả 7 ngày</span>
                        </div>
                    </div>

                    <!-- Details -->
                    <div class="space-y-4">
                        <div>
                            <span class="text-[10px] font-black uppercase text-emerald-600 bg-emerald-50 px-2.5 py-1 rounded-lg" x-text="selectedProductModal.brand"></span>
                            <h3 class="text-xl font-black text-slate-800 mt-2" x-text="selectedProductModal.name"></h3>
                            <div class="flex items-center gap-2 mt-2">
                                <div class="flex text-amber-400 text-xs">
                                    <i class="fa-solid fa-star"></i>
                                    <i class="fa-solid fa-star"></i>
                                    <i class="fa-solid fa-star"></i>
                                    <i class="fa-solid fa-star"></i>
                                    <i class="fa-solid fa-star-half-stroke"></i>
                                </div>
                                <span class="text-xs font-bold text-slate-600" x-text="selectedProductModal.rating + ' (' + (selectedProductModal.reviews || selectedProductModal.reviewsCount || 100) + ' đánh giá)'"></span>
                            </div>
                        </div>

                        <div class="p-3 bg-slate-50 rounded-2xl border border-slate-100">
                            <div class="flex items-baseline gap-2">
                                <span class="text-2xl font-black text-emerald-600" x-text="formatCurrency(selectedProductModal.price)"></span>
                                <span class="text-xs text-slate-400 line-through" x-text="formatCurrency(selectedProductModal.price * 1.2)"></span>
                            </div>
                            <p class="text-[11px] text-slate-500 mt-1">Đã bán: <strong class="text-slate-700" x-text="selectedProductModal.sold"></strong> sản phẩm toàn hệ thống</p>
                        </div>

                        <div>
                            <h4 class="text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">Mô tả sản phẩm:</h4>
                            <p class="text-xs text-slate-600 leading-relaxed" x-text="selectedProductModal.desc || selectedProductModal.description"></p>
                        </div>

                        <div>
                            <h4 class="text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">Thành phần & Công dụng:</h4>
                            <p class="text-xs text-slate-500 leading-relaxed" x-text="selectedProductModal.ingredients || 'Thành phần tự nhiên cao cấp, giàu Omega 3-6, Canxi, Protein dễ tiêu hóa, hỗ trợ hệ xương khớp và lông óng mượt.'"></p>
                        </div>

                        <!-- Quantity and Add -->
                        <div class="pt-2 border-t border-slate-100 space-y-3">
                            <div class="flex items-center justify-between">
                                <span class="text-xs font-bold text-slate-700">Số lượng:</span>
                                <div class="flex items-center border border-slate-200 rounded-xl overflow-hidden">
                                    <button @click="if(prodModalQty > 1) prodModalQty--" class="w-8 h-8 flex items-center justify-center bg-slate-50 hover:bg-slate-100 text-slate-600 font-bold text-sm">-</button>
                                    <span class="w-10 text-center text-xs font-black text-slate-800" x-text="prodModalQty"></span>
                                    <button @click="prodModalQty++" class="w-8 h-8 flex items-center justify-center bg-slate-50 hover:bg-slate-100 text-slate-600 font-bold text-sm">+</button>
                                </div>
                            </div>

                            <div class="flex items-center gap-2">
                                <button @click="addToCart(selectedProductModal, prodModalQty); selectedProductModal = null" class="w-1/2 py-2.5 border-2 border-emerald-600 text-emerald-600 hover:bg-emerald-50 font-bold rounded-xl text-xs transition-colors flex items-center justify-center gap-1.5">
                                    <i class="fa-solid fa-cart-plus"></i>
                                    <span>Thêm Giỏ Hàng</span>
                                </button>
                                <button @click="buyNow(selectedProductModal, prodModalQty); selectedProductModal = null" class="w-1/2 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-xl text-xs shadow-md shadow-emerald-600/30 transition-all flex items-center justify-center gap-1.5">
                                    <i class="fa-solid fa-bolt"></i>
                                    <span>Mua Ngay</span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </template>
    </div>

    <!-- 5. MODAL BÀI VIẾT PETSHARE360 CHI TIẾT -->
    <div x-show="selectedArticleModal" x-cloak class="fixed inset-0 z-50 overflow-y-auto bg-slate-900/70 backdrop-blur-sm flex items-center justify-center p-4">
        <template x-if="selectedArticleModal">
            <div class="bg-white rounded-3xl max-w-2xl w-full max-h-[90vh] overflow-y-auto shadow-2xl border border-slate-100 relative animate-fadeIn">
                <button @click="selectedArticleModal = null" class="absolute top-4 right-4 z-10 text-slate-500 hover:text-slate-800 w-9 h-9 rounded-full bg-white/80 backdrop-blur-md flex items-center justify-center shadow transition-colors">
                    <i class="fa-solid fa-xmark text-lg"></i>
                </button>

                <div class="h-64 overflow-hidden rounded-t-3xl relative">
                    <img :src="selectedArticleModal.image" :alt="selectedArticleModal.title" class="w-full h-full object-cover">
                    <div class="absolute inset-0 bg-gradient-to-t from-slate-900/80 via-transparent to-black/20"></div>
                    <div class="absolute bottom-4 left-6 right-6 text-white">
                        <span class="px-2.5 py-1 bg-emerald-500 text-white text-[10px] font-black rounded-lg uppercase tracking-wider inline-block mb-2 shadow" x-text="selectedArticleModal.category"></span>
                        <h3 class="text-xl md:text-2xl font-black leading-snug" x-text="selectedArticleModal.title"></h3>
                        <div class="flex items-center gap-3 text-xs text-slate-300 mt-2">
                            <span><i class="fa-solid fa-user-pen mr-1"></i> <strong x-text="selectedArticleModal.author"></strong></span>
                            <span>•</span>
                            <span><i class="fa-solid fa-calendar mr-1"></i> <span x-text="selectedArticleModal.date"></span></span>
                            <span>•</span>
                            <span><i class="fa-solid fa-eye mr-1"></i> <span x-text="selectedArticleModal.views"></span> lượt xem</span>
                        </div>
                    </div>
                </div>

                <div class="p-6 space-y-6">
                    <!-- Key takeaway alert -->
                    <div class="p-4 bg-emerald-50/70 rounded-2xl border border-emerald-100 text-xs text-emerald-900 space-y-1">
                        <p class="font-bold flex items-center gap-1.5"><i class="fa-solid fa-bookmark text-emerald-600"></i> Lời khuyên trọng tâm từ Ban Chuyên Môn Thú Y PetCare360:</p>
                        <p class="text-emerald-800 leading-relaxed" x-text="selectedArticleModal.summary"></p>
                    </div>

                    <!-- Article Body Content -->
                    <div class="prose prose-sm max-w-none text-slate-700 space-y-4 text-xs md:text-sm leading-relaxed" x-html="selectedArticleModal.content"></div>

                    <!-- Author box -->
                    <div class="flex items-center gap-4 p-4 bg-slate-50 rounded-2xl border border-slate-100">
                        <div class="w-12 h-12 rounded-full bg-emerald-100 flex items-center justify-center text-emerald-700 text-lg font-black shrink-0">
                            <i class="fa-solid fa-user-doctor"></i>
                        </div>
                        <div>
                            <h4 class="text-xs font-bold text-slate-800" x-text="'Tác giả: ' + selectedArticleModal.author"></h4>
                            <p class="text-[11px] text-slate-500 mt-0.5">Hội đồng Cố vấn Y khoa & Dinh dưỡng Thú cưng - Hệ thống PetCare360 Việt Nam</p>
                        </div>
                    </div>

                    <div class="flex items-center justify-between pt-2 border-t border-slate-100">
                        <button @click="selectedArticleModal = null" class="px-5 py-2.5 border border-slate-200 text-slate-600 font-bold rounded-xl text-xs hover:bg-slate-50">
                            Đóng bài viết
                        </button>
                        <button @click="alert('Đã sao chép liên kết bài viết vào bộ nhớ tạm!')" class="px-5 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-xl text-xs flex items-center gap-2 shadow-md shadow-emerald-600/30">
                            <i class="fa-solid fa-share-nodes"></i>
                            <span>Chia sẻ bài viết</span>
                        </button>
                    </div>
                </div>
            </div>
        </template>
    </div>

    <!-- 6. MODAL BẢNG CHÍNH SÁCH QUYỀN LỢI THÀNH VIÊN CHI TIẾT (6 THÁNG TÍNH LẠI 1 LẦN) -->
    <div x-show="showLoyaltyDetailModal || loyaltyDetailModalOpen" x-cloak class="fixed inset-0 z-50 overflow-y-auto bg-slate-900/70 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-2xl w-full max-h-[90vh] overflow-y-auto p-6 md:p-8 shadow-2xl border border-slate-100 relative animate-fadeIn">
            <button @click="showLoyaltyDetailModal = false; loyaltyDetailModalOpen = false;" class="absolute top-5 right-5 text-slate-400 hover:text-slate-600 w-9 h-9 rounded-full bg-slate-100 flex items-center justify-center transition-colors">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>

            <div class="text-center mb-6">
                <span class="px-3 py-1 bg-amber-100 text-amber-700 text-[11px] font-black rounded-full uppercase">Chương trình Khách hàng Thân Thiết</span>
                <h3 class="text-2xl font-black text-slate-800 mt-2">Quy Chế Xếp Hạng & Tích Điểm PetCare360</h3>
                <p class="text-xs text-slate-500 mt-1">Đặc quyền chăm sóc toàn diện cho bé cưng của gia đình bạn</p>
            </div>

            <!-- Chu kỳ 6 tháng tính điểm lại từ đầu -->
            <div class="p-4 bg-gradient-to-r from-amber-500/10 via-amber-500/5 to-transparent border-l-4 border-amber-500 rounded-2xl mb-6">
                <h4 class="text-xs font-black text-amber-900 uppercase tracking-wider flex items-center gap-2">
                    <i class="fa-solid fa-rotate text-amber-600"></i> QUY ĐỊNH CHU KỲ XÉT HẠNG (6 THÁNG / LẦN)
                </h4>
                <p class="text-xs text-slate-700 mt-1.5 leading-relaxed">
                    Hệ thống PetCare360 thực hiện <strong>tính điểm tích lũy và xét duyệt lại hạng thành viên định kỳ mỗi 6 tháng một lần</strong> (vào ngày <strong>01/01</strong> và ngày <strong>01/07</strong> hàng năm). Điểm tích lũy trong chu kỳ 6 tháng trước sẽ dùng để duy trì hoặc nâng cấp bậc quyền lợi cho chu kỳ 6 tháng tiếp theo. Điểm thưởng còn lại có thể quy đổi voucher giảm giá trước thời điểm chốt kỳ.
                </p>
            </div>

            <!-- Tier Table -->
            <div class="space-y-4">
                <!-- Hạng Đồng -->
                <div class="p-4 rounded-2xl border border-slate-200 bg-slate-50/50">
                    <div class="flex items-center justify-between mb-2">
                        <div class="flex items-center gap-2">
                            <span class="w-8 h-8 rounded-xl bg-amber-700/20 text-amber-800 flex items-center justify-center font-black text-sm">🥉</span>
                            <div>
                                <h5 class="text-sm font-black text-slate-800">Thành viên Đồng (Bronze Member)</h5>
                                <span class="text-[11px] text-slate-500">Dưới 1.000 điểm tích lũy trong 6 tháng</span>
                            </div>
                        </div>
                        <span class="px-2.5 py-1 bg-slate-200 text-slate-700 text-[10px] font-bold rounded-lg">Mặc định ban đầu</span>
                    </div>
                    <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside pl-2">
                        <li>Tích lũy 1% giá trị trên mọi đơn hàng sản phẩm & dịch vụ</li>
                        <li>Tặng voucher 50.000đ nhân dịp sinh nhật của thú cưng</li>
                        <li>Tư vấn sức khỏe trực tuyến miễn phí 24/7 qua cổng CSKH</li>
                    </ul>
                </div>

                <!-- Hạng Bạc -->
                <div class="p-4 rounded-2xl border border-slate-200 bg-slate-50/50">
                    <div class="flex items-center justify-between mb-2">
                        <div class="flex items-center gap-2">
                            <span class="w-8 h-8 rounded-xl bg-slate-300 text-slate-800 flex items-center justify-center font-black text-sm">🥈</span>
                            <div>
                                <h5 class="text-sm font-black text-slate-800">Thành viên Bạc (Silver Member)</h5>
                                <span class="text-[11px] text-slate-500">Từ 1.000 - 2.999 điểm trong 6 tháng</span>
                            </div>
                        </div>
                        <span class="px-2.5 py-1 bg-slate-200 text-slate-700 text-[10px] font-bold rounded-lg">Giảm 5% Spa</span>
                    </div>
                    <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside pl-2">
                        <li>Tích lũy 3% giá trị đơn hàng vào quỹ điểm thưởng</li>
                        <li>Giảm trực tiếp 5% chi phí các gói Spa & Grooming thẩm mỹ</li>
                        <li>Miễn phí 01 lần khám tổng quát và đo huyết áp/nhiệt độ định kỳ</li>
                        <li>Quà sinh nhật thú cưng trị giá 150.000đ</li>
                    </ul>
                </div>

                <!-- Hạng Vàng -->
                <div class="p-4 rounded-2xl border border-amber-300 bg-amber-50/40">
                    <div class="flex items-center justify-between mb-2">
                        <div class="flex items-center gap-2">
                            <span class="w-8 h-8 rounded-xl bg-amber-400 text-amber-900 flex items-center justify-center font-black text-sm">🥇</span>
                            <div>
                                <h5 class="text-sm font-black text-amber-950">Thành viên Vàng (Gold Member)</h5>
                                <span class="text-[11px] text-amber-800">Từ 3.000 - 6.999 điểm trong 6 tháng</span>
                            </div>
                        </div>
                        <span class="px-2.5 py-1 bg-amber-500 text-white text-[10px] font-bold rounded-lg shadow-sm">Ưu Tiên Đặt Khám</span>
                    </div>
                    <ul class="text-xs text-slate-700 space-y-1 list-disc list-inside pl-2">
                        <li>Tích lũy 5% giá trị mọi đơn hàng</li>
                        <li>Giảm 10% trọn đời dịch vụ y tế, khám chữa bệnh & lưu chuồng</li>
                        <li>Ưu tiên xếp lịch khám không cần chờ đợi tại tất cả chi nhánh</li>
                        <li>Miễn phí 01 gói Spa tắm sấy vệ sinh cơ bản mỗi chu kỳ</li>
                        <li>Hộp quà sinh nhật PetCare VIP Box trị giá 350.000đ</li>
                    </ul>
                </div>

                <!-- Hạng Kim Cương -->
                <div class="p-4 rounded-2xl border border-emerald-300 bg-emerald-50/50">
                    <div class="flex items-center justify-between mb-2">
                        <div class="flex items-center gap-2">
                            <span class="w-8 h-8 rounded-xl bg-emerald-500 text-white flex items-center justify-center font-black text-sm">💎</span>
                            <div>
                                <h5 class="text-sm font-black text-emerald-950">Thành viên Kim Cương (Diamond VIP)</h5>
                                <span class="text-[11px] text-emerald-800">Từ 7.000 điểm trở lên trong 6 tháng</span>
                            </div>
                        </div>
                        <span class="px-2.5 py-1 bg-emerald-600 text-white text-[10px] font-bold rounded-lg shadow-sm">Bác Sĩ Riêng 24/7</span>
                    </div>
                    <ul class="text-xs text-slate-700 space-y-1 list-disc list-inside pl-2">
                        <li>Tích lũy 8% giá trị hóa đơn, quy đổi chiết khấu tối đa</li>
                        <li>Giảm 15% tất cả sản phẩm thức ăn, phụ kiện và dịch vụ phẫu thuật</li>
                        <li>Được phân công 01 Bác sĩ thú y gia đình riêng túc trực hỗ trợ 24/7</li>
                        <li>Miễn phí xe cứu thương đưa đón thú cưng cấp cứu trong bán kính 10km</li>
                        <li>Gói khám sức khỏe toàn diện kèm xét nghiệm máu tổng quát miễn phí định kỳ</li>
                    </ul>
                </div>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-100 text-right">
                <button @click="showLoyaltyDetailModal = false; loyaltyDetailModalOpen = false;" class="px-6 py-2.5 bg-slate-800 hover:bg-slate-900 text-white font-bold rounded-xl text-xs transition-colors">
                    Đã hiểu & Đóng
                </button>
            </div>
        </div>
    </div>

    <!-- 7. MODAL SỔ SỨC KHỎE THÚ CƯNG (KÈM HÌNH ẢNH & LỊCH TRÌNH Y TẾ) -->
    <div x-show="selectedPetHealthModal" x-cloak class="fixed inset-0 z-50 overflow-y-auto bg-slate-900/70 backdrop-blur-sm flex items-center justify-center p-4">
        <template x-if="selectedPetHealthModal">
            <div class="bg-white rounded-3xl max-w-2xl w-full max-h-[90vh] overflow-y-auto p-6 md:p-8 shadow-2xl border border-slate-100 relative animate-fadeIn">
                <button @click="selectedPetHealthModal = null" class="absolute top-5 right-5 text-slate-400 hover:text-slate-600 w-9 h-9 rounded-full bg-slate-100 flex items-center justify-center transition-colors">
                    <i class="fa-solid fa-xmark text-lg"></i>
                </button>

                <div class="flex items-center gap-4 pb-5 border-b border-slate-100 mb-6">
                    <img :src="selectedPetHealthModal.avatar || selectedPetHealthModal.image" :alt="selectedPetHealthModal.name" class="w-20 h-20 rounded-2xl object-cover border-2 border-emerald-500 shadow-md">
                    <div>
                        <div class="flex items-center gap-2">
                            <h3 class="text-2xl font-black text-slate-800" x-text="selectedPetHealthModal.name"></h3>
                            <span class="px-2 py-0.5 bg-emerald-100 text-emerald-800 text-[10px] font-black rounded-md" x-text="selectedPetHealthModal.type || selectedPetHealthModal.species"></span>
                        </div>
                        <p class="text-xs text-slate-500 mt-1" x-text="'Giống: ' + selectedPetHealthModal.breed + ' • Giới tính: ' + selectedPetHealthModal.gender + ' • Tuổi: ' + selectedPetHealthModal.age"></p>
                        <p class="text-xs text-slate-500" x-text="'Cân nặng: ' + selectedPetHealthModal.weight + ' • Mã Microchip: ' + (selectedPetHealthModal.chipId || selectedPetHealthModal.chip || '900118000452311')"></p>
                    </div>
                </div>

                <!-- Pet Medical Passport Tabs -->
                <div class="space-y-6">
                    <!-- Vaccine history -->
                    <div>
                        <h4 class="text-xs font-black text-slate-800 uppercase tracking-wider mb-3 flex items-center gap-2">
                            <i class="fa-solid fa-syringe text-emerald-600"></i> Lịch Sử Tiêm Chủng Vắc-xin & Phòng Bệnh
                        </h4>
                        <div class="overflow-x-auto rounded-xl border border-slate-200">
                            <table class="w-full text-left text-xs">
                                <thead class="bg-slate-50 text-slate-500 font-bold border-b border-slate-200">
                                    <tr>
                                        <th class="p-2.5">Vắc-xin</th>
                                        <th class="p-2.5">Ngày tiêm</th>
                                        <th class="p-2.5">Bác sĩ phụ trách</th>
                                        <th class="p-2.5">Hẹn tái chủng</th>
                                        <th class="p-2.5 text-center">Trạng thái</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-100">
                                    <template x-for="(vax, idx) in (selectedPetHealthModal.vaccines || [])" :key="idx">
                                        <tr class="hover:bg-slate-50/50">
                                            <td class="p-2.5 font-bold text-slate-800" x-text="vax.name"></td>
                                            <td class="p-2.5 text-slate-600" x-text="vax.date"></td>
                                            <td class="p-2.5 text-slate-600" x-text="vax.doctor"></td>
                                            <td class="p-2.5 font-semibold text-emerald-600" x-text="vax.nextDate"></td>
                                            <td class="p-2.5 text-center">
                                                <span class="px-2 py-0.5 rounded-full text-[10px] font-bold" :class="vax.status === 'Đã hoàn thành' ? 'bg-emerald-100 text-emerald-700' : 'bg-amber-100 text-amber-700'" x-text="vax.status"></span>
                                            </td>
                                        </tr>
                                    </template>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- Medical treatments -->
                    <div>
                        <h4 class="text-xs font-black text-slate-800 uppercase tracking-wider mb-3 flex items-center gap-2">
                            <i class="fa-solid fa-notes-medical text-rose-600"></i> Bệnh Án & Điều Trị Gần Nhất
                        </h4>
                        <div class="space-y-2">
                            <template x-for="(med, idx) in (selectedPetHealthModal.medicalHistory || [])" :key="idx">
                                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs">
                                    <div class="flex items-center justify-between mb-1">
                                        <strong class="text-slate-800" x-text="med.diagnosis"></strong>
                                        <span class="text-[11px] text-slate-400 font-medium" x-text="med.date"></span>
                                    </div>
                                    <p class="text-slate-600" x-text="'Phác đồ: ' + med.treatment"></p>
                                    <p class="text-slate-500 mt-1 italic" x-text="'Bác sĩ dặn: ' + med.notes"></p>
                                </div>
                            </template>
                        </div>
                    </div>

                    <!-- Health Notes & Allergy Alert -->
                    <div class="p-4 bg-rose-50/70 border border-rose-200 rounded-2xl space-y-1">
                        <h5 class="text-xs font-black text-rose-800 flex items-center gap-1.5">
                            <i class="fa-solid fa-triangle-exclamation text-rose-600"></i> Cảnh báo dị ứng & Chế độ ăn đặc biệt
                        </h5>
                        <p class="text-xs text-rose-700" x-text="selectedPetHealthModal.allergies || 'Không ghi nhận tiền sử dị ứng thuốc hay thực phẩm.'"></p>
                    </div>

                    <div class="flex items-center justify-between pt-2 border-t border-slate-100">
                        <button @click="selectedPetHealthModal = null" class="px-5 py-2.5 border border-slate-200 text-slate-600 font-bold rounded-xl text-xs hover:bg-slate-50">
                            Đóng
                        </button>
                        <button @click="alert('Đã tạo bản in Sổ Sức Khỏe Điện Tử chuẩn quốc tế (PDF) cho bé!')" class="px-5 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-xl text-xs flex items-center gap-2 shadow-md shadow-emerald-600/30">
                            <i class="fa-solid fa-print"></i>
                            <span>Xuất Sổ Sức Khỏe (PDF)</span>
                        </button>
                    </div>
                </div>
            </div>
        </template>
    </div>

    <!-- 8. MODAL THÊM HỒ SƠ THÚ CƯNG (CÓ CHỖ THÊM HÌNH ẢNH THÚ CƯNG) -->
    <div x-show="showAddPetModal || addPetModalOpen" x-cloak class="fixed inset-0 z-50 overflow-y-auto bg-slate-900/70 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-xl w-full p-6 md:p-8 shadow-2xl border border-slate-100 relative animate-fadeIn max-h-[90vh] overflow-y-auto">
            <button @click="showAddPetModal = false; addPetModalOpen = false;" class="absolute top-5 right-5 text-slate-400 hover:text-slate-600 w-9 h-9 rounded-full bg-slate-100 flex items-center justify-center transition-colors">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>

            <div class="text-center mb-5">
                <div class="w-14 h-14 bg-emerald-100 rounded-2xl flex items-center justify-center mx-auto text-emerald-600 text-2xl shadow-sm mb-2">
                    <i class="fa-solid fa-paw"></i>
                </div>
                <h3 class="text-xl font-black text-slate-800">Tạo Hồ Sơ Bé Cưng Toàn Diện</h3>
                <p class="text-xs text-slate-500 mt-0.5">Định danh vi mạch, y tế tiêm chủng, thói quen và liên hệ chủ nuôi</p>
            </div>

            <!-- CẢNH BÁO ĐỎ NẾU CHƯA ĐỦ THÔNG TIN HOẶC CHƯA TẢI ẢNH (YÊU CẦU MỤC 5) -->
            <div x-show="petFormError" x-cloak class="mb-4 p-3.5 bg-rose-50 border-2 border-rose-400 rounded-2xl text-rose-700 text-xs font-bold flex items-center gap-2.5 shadow-sm animate-pulse">
                <i class="fa-solid fa-triangle-exclamation text-rose-600 text-lg shrink-0"></i>
                <span x-text="petFormError"></span>
            </div>

            <form @submit.prevent="saveNewPet()" class="space-y-4">
                <!-- TẢI ẢNH LÊN HOẶC CHỌN ẢNH CỐ ĐỊNH CHO THÚ CƯNG (YÊU CẦU MỤC 5) -->
                <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200">
                    <label class="block text-xs font-bold text-slate-800 mb-2">
                        Ảnh Chân Dung Bé Cưng <span class="text-rose-500">* (Bắt buộc tải ảnh lên để nhận diện bé cưng)</span>
                    </label>
                    <div class="flex flex-col sm:flex-row items-center sm:items-start gap-4">
                        <div class="relative shrink-0">
                            <img :src="newPetData.avatar || 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=300&q=80'" 
                                 class="w-20 h-20 rounded-2xl object-cover border-2 border-brand-500 shadow-sm bg-white">
                            <span x-show="newPetData.avatar" class="absolute -bottom-1 -right-1 bg-emerald-500 text-white rounded-full p-1 text-[9px] shadow">
                                <i class="fa-solid fa-check"></i>
                            </span>
                        </div>
                        <div class="flex-1 w-full space-y-2">
                            <div class="flex flex-wrap items-center gap-2">
                                <label class="px-3.5 py-2 bg-brand-600 hover:bg-brand-700 text-white rounded-xl text-xs font-bold cursor-pointer transition flex items-center gap-1.5 shadow-sm">
                                    <i class="fa-solid fa-cloud-arrow-up"></i> Tải ảnh từ thiết bị
                                    <input type="file" accept="image/*" @change="handlePetPhotoUpload()" class="hidden">
                                </label>
                                <span class="text-[11px] font-medium" :class="newPetData.avatar ? 'text-emerald-600 font-bold' : 'text-slate-400'" 
                                      x-text="newPetData.avatar ? '✓ Đã tải ảnh nhận diện' : 'Chưa tải ảnh lên'"></span>
                            </div>
                            <input type="text" x-model="newPetData.avatar" placeholder="Hoặc dán đường dẫn ảnh trực tuyến..." class="w-full px-3 py-1.5 rounded-xl border border-slate-200 text-xs bg-white focus:outline-none focus:ring-2 focus:ring-brand-500">
                            
                            <!-- Preset Avatars -->
                            <div class="flex items-center gap-1.5 pt-0.5">
                                <span class="text-[10px] text-slate-400 font-bold uppercase">Ảnh mẫu:</span>
                                <button type="button" @click="newPetData.avatar = 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=300&q=80'; petFormError = '';" class="text-[10px] px-2 py-0.5 bg-white hover:bg-brand-100 text-slate-700 rounded-md border border-slate-200 font-semibold">Cún Corgi</button>
                                <button type="button" @click="newPetData.avatar = 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=300&q=80'; petFormError = '';" class="text-[10px] px-2 py-0.5 bg-white hover:bg-brand-100 text-slate-700 rounded-md border border-slate-200 font-semibold">Mèo ALN</button>
                                <button type="button" @click="newPetData.avatar = 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=300&q=80'; petFormError = '';" class="text-[10px] px-2 py-0.5 bg-white hover:bg-brand-100 text-slate-700 rounded-md border border-slate-200 font-semibold">Cún Poodle</button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 1. THÔNG TIN CƠ BẢN -->
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Tên bé cưng <span class="text-rose-500">*</span></label>
                        <input type="text" x-model="newPetData.name" required placeholder="Ví dụ: Bơ, Mochi..." class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-brand-500">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Loài <span class="text-rose-500">*</span></label>
                        <select x-model="newPetData.type" required class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-brand-500">
                            <option value="Chó">Chó</option>
                            <option value="Mèo">Mèo</option>
                            <option value="Thỏ / Hamster">Thỏ / Hamster</option>
                            <option value="Khác">Khác</option>
                        </select>
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Giống loài <span class="text-rose-500">*</span></label>
                        <input type="text" x-model="newPetData.breed" required placeholder="Ví dụ: Poodle, Corgi, ALN..." class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-brand-500">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Giới tính <span class="text-rose-500">*</span></label>
                        <select x-model="newPetData.gender" class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-brand-500">
                            <option value="Đực">Đực</option>
                            <option value="Cái">Cái</option>
                        </select>
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Tuổi / Ngày sinh</label>
                        <input type="text" x-model="newPetData.age" placeholder="Ví dụ: 1.5 tuổi hoặc 15/04/2023" class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-brand-500">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Cân nặng hiện tại (kg) <span class="text-rose-500">*</span></label>
                        <input type="text" x-model="newPetData.weight" required placeholder="Ví dụ: 4.2" class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-brand-500">
                    </div>
                </div>

                <!-- NGOẠI HÌNH & NHẬN DẠNG -->
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Ngoại hình & Đặc điểm nhận diện nổi bật</label>
                    <input type="text" x-model="newPetData.appearance" placeholder="Ví dụ: Lông vàng trắng, tai cụp, đuôi xù, mắt 2 màu..." class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-brand-500">
                </div>

                <!-- 2. HỒ SƠ Y TẾ & BỆNH LÝ -->
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Hồ sơ y tế / Lịch tiêm phòng & Bệnh lý dị ứng</label>
                    <textarea x-model="newPetData.allergies" rows="2" placeholder="Ví dụ: Đã tiêm 3 mũi 7 bệnh, dị ứng thức ăn có ngũ cốc độn..." class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-brand-500"></textarea>
                </div>

                <!-- 3. THÓI QUEN & DINH DƯỠNG -->
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Chế độ dinh dưỡng</label>
                        <input type="text" x-model="newPetData.diet" placeholder="Ví dụ: Hạt Royal Canin + Pate 2 bữa/ngày" class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-brand-500">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Thói quen & Tính cách</label>
                        <input type="text" x-model="newPetData.habits" placeholder="Ví dụ: Thích đi dạo, sợ sấy lông, quấn người..." class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-brand-500">
                    </div>
                </div>

                <!-- 4. THÔNG TIN CHỦ SỞ HỮU -->
                <div class="p-3 bg-slate-50 rounded-2xl border border-slate-200 space-y-2">
                    <span class="text-[11px] font-bold text-slate-800 uppercase tracking-wide block">Thông tin liên hệ chủ sở hữu</span>
                    <div class="grid grid-cols-2 gap-3">
                        <div>
                            <label class="block text-[11px] font-semibold text-slate-600 mb-0.5">Họ tên chủ nuôi</label>
                            <input type="text" x-model="newPetData.ownerName" placeholder="Nguyễn Hoàng Giang" class="w-full px-2.5 py-1.5 rounded-lg border border-slate-200 text-xs bg-white">
                        </div>
                        <div>
                            <label class="block text-[11px] font-semibold text-slate-600 mb-0.5">SĐT liên hệ</label>
                            <input type="text" x-model="newPetData.ownerPhone" placeholder="0909 123 456" class="w-full px-2.5 py-1.5 rounded-lg border border-slate-200 text-xs bg-white">
                        </div>
                    </div>
                    <div class="grid grid-cols-2 gap-3">
                        <div>
                            <label class="block text-[11px] font-semibold text-slate-600 mb-0.5">Địa chỉ nhà</label>
                            <input type="text" x-model="newPetData.ownerAddress" placeholder="125 Hoàng Quốc Việt, Cầu Giấy, HN" class="w-full px-2.5 py-1.5 rounded-lg border border-slate-200 text-xs bg-white">
                        </div>
                        <div>
                            <label class="block text-[11px] font-semibold text-rose-600 mb-0.5">SĐT Khẩn cấp 24/7</label>
                            <input type="text" x-model="newPetData.ownerEmergency" placeholder="0912 345 678" class="w-full px-2.5 py-1.5 rounded-lg border border-rose-200 text-xs bg-white">
                        </div>
                    </div>
                </div>

                <div class="flex items-center gap-3 pt-2">
                    <button type="button" @click="showAddPetModal = false; addPetModalOpen = false; petFormError = '';" class="w-1/3 py-2.5 border border-slate-200 text-slate-600 font-bold rounded-xl text-xs hover:bg-slate-50">
                        Hủy
                    </button>
                    <button type="submit" class="w-2/3 py-2.5 bg-brand-600 hover:bg-brand-700 text-white font-bold rounded-xl text-xs shadow-md shadow-brand-600/30 transition-all flex items-center justify-center gap-2">
                        <i class="fa-solid fa-paw"></i>
                        <span>Lưu Hồ Sơ Bé Cưng</span>
                    </button>
                </div>
            </form>
        </div>
    </div>

    <!-- 9. MODAL CHỈNH SỬA THÔNG TIN CÁ NHÂN (CÓ ĐỔI AVATAR NGƯỜI DÙNG) -->
    <div x-show="showEditProfileModal || editProfileModalOpen" x-cloak class="fixed inset-0 z-50 overflow-y-auto bg-slate-900/70 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 md:p-8 shadow-2xl border border-slate-100 relative animate-fadeIn">
            <button @click="showEditProfileModal = false; editProfileModalOpen = false;" class="absolute top-5 right-5 text-slate-400 hover:text-slate-600 w-9 h-9 rounded-full bg-slate-100 flex items-center justify-center transition-colors">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>

            <div class="text-center mb-6">
                <h3 class="text-xl font-black text-slate-800">Chỉnh Sửa Thông Tin Cá Nhân</h3>
                <p class="text-xs text-slate-500 mt-0.5">Cập nhật hồ sơ thành viên & avatar đại diện</p>
            </div>

            <form @submit.prevent="saveUserProfile()" class="space-y-4">
                <!-- Chọn Avatar -->
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-2">Ảnh Đại Diện (Avatar)</label>
                    <div class="flex items-center gap-4">
                        <img :src="customerProfile.avatar" class="w-16 h-16 rounded-full object-cover border-2 border-emerald-500 shadow-md shrink-0">
                        <div class="flex-1 space-y-2">
                            <input type="text" x-model="customerProfile.avatar" placeholder="Dán URL ảnh đại diện..." class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs font-medium focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                            <!-- Preset User Avatars -->
                            <div class="flex items-center gap-2">
                                <span class="text-[10px] text-slate-400 font-bold uppercase">Mẫu:</span>
                                <button type="button" @click="customerProfile.avatar = 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=200&q=80'" class="w-7 h-7 rounded-full overflow-hidden border border-slate-300 focus:ring-2 focus:ring-emerald-500">
                                    <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=200&q=80" class="w-full h-full object-cover">
                                </button>
                                <button type="button" @click="customerProfile.avatar = 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=200&q=80'" class="w-7 h-7 rounded-full overflow-hidden border border-slate-300 focus:ring-2 focus:ring-emerald-500">
                                    <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=200&q=80" class="w-full h-full object-cover">
                                </button>
                                <button type="button" @click="customerProfile.avatar = 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=200&q=80'" class="w-7 h-7 rounded-full overflow-hidden border border-slate-300 focus:ring-2 focus:ring-emerald-500">
                                    <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=200&q=80" class="w-full h-full object-cover">
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Họ và tên</label>
                    <input type="text" x-model="customerProfile.name" required class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                </div>

                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Số điện thoại</label>
                    <input type="tel" x-model="customerProfile.phone" required class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                </div>

                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Địa chỉ giao hàng mặc định</label>
                    <input type="text" x-model="customerProfile.address" required class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                </div>

                <div class="flex items-center gap-3 pt-2">
                    <button type="button" @click="showEditProfileModal = false; editProfileModalOpen = false;" class="w-1/3 py-2.5 border border-slate-200 text-slate-600 font-bold rounded-xl text-xs hover:bg-slate-50">
                        Hủy
                    </button>
                    <button type="submit" class="w-2/3 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-xl text-xs shadow-md shadow-emerald-600/30 transition-all flex items-center justify-center gap-2">
                        <i class="fa-solid fa-floppy-disk"></i>
                        <span>Lưu Thay Đổi</span>
                    </button>
                </div>
            </form>
        </div>
    </div>

    <!-- 10. MODAL THÊM SẢN PHẨM MỚI (ADMIN) -->
    <div x-show="showAddProductModal || addProductModalOpen" x-cloak class="fixed inset-0 z-50 overflow-y-auto bg-slate-900/70 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-xl w-full p-6 md:p-8 shadow-2xl border border-slate-100 relative animate-fadeIn">
            <button @click="showAddProductModal = false; addProductModalOpen = false;" class="absolute top-5 right-5 text-slate-400 hover:text-slate-600 w-9 h-9 rounded-full bg-slate-100 flex items-center justify-center transition-colors">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>

            <div class="text-center mb-6">
                <div class="w-14 h-14 bg-indigo-100 rounded-2xl flex items-center justify-center mx-auto text-indigo-600 text-2xl shadow-sm mb-2">
                    <i class="fa-solid fa-box-open"></i>
                </div>
                <h3 class="text-xl font-black text-slate-800">Thêm Sản Phẩm Mới Vào Hệ Thống</h3>
                <p class="text-xs text-slate-500 mt-0.5">Tạo SKU và thiết lập giá bán, tồn kho ban đầu theo chi nhánh</p>
            </div>

            <form @submit.prevent="adminSaveNewProduct()" class="space-y-4">
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Mã SKU <span class="text-rose-500">*</span></label>
                        <input type="text" x-model="newProdForm.sku" required placeholder="SKU-8899" class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs font-bold font-mono focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Danh mục <span class="text-rose-500">*</span></label>
                        <select x-model="newProdForm.category" required class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500">
                            <option value="Thức ăn khô">Thức ăn hạt khô</option>
                            <option value="Pate & Treats">Pate & Treats thưởng</option>
                            <option value="Phụ kiện & Đồ chơi">Phụ kiện & Đồ chơi</option>
                            <option value="Thuốc & Y tế">Thuốc & Y tế thú cưng</option>
                            <option value="Vệ sinh & Khử mùi">Vệ sinh & Cát vệ sinh</option>
                        </select>
                    </div>
                </div>

                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Tên sản phẩm <span class="text-rose-500">*</span></label>
                    <input type="text" x-model="newProdForm.name" required placeholder="Nhập tên sản phẩm đầy đủ..." class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500">
                </div>

                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Thương hiệu / Xuất xứ</label>
                        <input type="text" x-model="newProdForm.brand" placeholder="Royal Canin (Pháp)..." class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Giá bán lẻ (VNĐ) <span class="text-rose-500">*</span></label>
                        <input type="number" x-model="newProdForm.price" required placeholder="350000" class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs font-bold text-emerald-600 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500">
                    </div>
                </div>

                <div class="grid grid-cols-3 gap-2 bg-slate-50 p-3 rounded-2xl border border-slate-200">
                    <div>
                        <label class="block text-[11px] font-bold text-slate-600 mb-1">Tồn CN Cầu Giấy</label>
                        <input type="number" x-model="newProdForm.stockHN" placeholder="20" class="w-full px-2.5 py-1.5 rounded-lg border border-slate-200 text-xs font-semibold">
                    </div>
                    <div>
                        <label class="block text-[11px] font-bold text-slate-600 mb-1">Tồn CN Quận 7</label>
                        <input type="number" x-model="newProdForm.stockQ7" placeholder="25" class="w-full px-2.5 py-1.5 rounded-lg border border-slate-200 text-xs font-semibold">
                    </div>
                    <div>
                        <label class="block text-[11px] font-bold text-slate-600 mb-1">Tồn CN Bình Thạnh</label>
                        <input type="number" x-model="newProdForm.stockBT" placeholder="15" class="w-full px-2.5 py-1.5 rounded-lg border border-slate-200 text-xs font-semibold">
                    </div>
                </div>

                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">URL Hình ảnh sản phẩm</label>
                    <input type="text" x-model="newProdForm.img" placeholder="https://images.unsplash.com/..." class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500">
                </div>

                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Mô tả sản phẩm</label>
                    <textarea x-model="newProdForm.desc" rows="2" placeholder="Công dụng, quy cách đóng gói, đối tượng sử dụng..." class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500"></textarea>
                </div>

                <div class="flex items-center gap-3 pt-2">
                    <button type="button" @click="showAddProductModal = false; addProductModalOpen = false;" class="w-1/3 py-2.5 border border-slate-200 text-slate-600 font-bold rounded-xl text-xs hover:bg-slate-50">
                        Hủy
                    </button>
                    <button type="submit" class="w-2/3 py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold rounded-xl text-xs shadow-md shadow-indigo-600/30 transition-all flex items-center justify-center gap-2">
                        <i class="fa-solid fa-plus"></i>
                        <span>Thêm Sản Phẩm Ngay</span>
                    </button>
                </div>
            </form>
        </div>
    </div>

    <!-- 11. MODAL NHẬP THÊM HÀNG / RESTOCK (ADMIN) -->
    <div x-show="showRestockModal || restockModalOpen" x-cloak class="fixed inset-0 z-50 overflow-y-auto bg-slate-900/70 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-lg w-full p-6 md:p-8 shadow-2xl border border-slate-100 relative animate-fadeIn">
            <button @click="showRestockModal = false; restockModalOpen = false;" class="absolute top-5 right-5 text-slate-400 hover:text-slate-600 w-9 h-9 rounded-full bg-slate-100 flex items-center justify-center transition-colors">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>

            <div class="text-center mb-6">
                <div class="w-14 h-14 bg-emerald-100 rounded-2xl flex items-center justify-center mx-auto text-emerald-600 text-2xl shadow-sm mb-2">
                    <i class="fa-solid fa-dolly"></i>
                </div>
                <h3 class="text-xl font-black text-slate-800">Nhập Thêm Kho Hàng Hóa</h3>
                <p class="text-xs text-slate-500 mt-0.5">Tạo phiếu nhập kho và phân bổ số lượng vào chi nhánh</p>
            </div>

            <form @submit.prevent="adminSaveRestock()" class="space-y-4">
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Chọn Sản Phẩm Cần Nhập Thêm <span class="text-rose-500">*</span></label>
                    <select x-model="restockForm.productId" required class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                        <option value="">-- Chọn sản phẩm trong kho --</option>
                        <template x-for="p in products" :key="p.id">
                            <option :value="p.id" x-text="p.name + ' (Hiện có: ' + p.stock + ')'"></option>
                        </template>
                    </select>
                </div>

                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Chi nhánh nhập kho <span class="text-rose-500">*</span></label>
                        <select x-model="restockForm.branch" required class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                            <option value="HN">Chi nhánh Cầu Giấy (Hà Nội)</option>
                            <option value="Q7">Chi nhánh Quận 7 (TP.HCM)</option>
                            <option value="BT">Chi nhánh Bình Thạnh (TP.HCM)</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Số lượng nhập thêm <span class="text-rose-500">*</span></label>
                        <input type="number" x-model="restockForm.quantity" required min="1" placeholder="50" class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs font-bold text-emerald-600 focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Đơn giá nhập (VNĐ)</label>
                        <input type="number" x-model="restockForm.costPrice" placeholder="210000" class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Nhà cung cấp</label>
                        <input type="text" x-model="restockForm.supplier" placeholder="Công ty CP Petcare Distribution..." class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                    </div>
                </div>

                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Ghi chú phiếu nhập kho</label>
                    <input type="text" x-model="restockForm.notes" placeholder="Số hóa đơn VAT, lô sản xuất, hạn sử dụng..." class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                </div>

                <div class="flex items-center gap-3 pt-2">
                    <button type="button" @click="showRestockModal = false; restockModalOpen = false;" class="w-1/3 py-2.5 border border-slate-200 text-slate-600 font-bold rounded-xl text-xs hover:bg-slate-50">
                        Hủy
                    </button>
                    <button type="submit" class="w-2/3 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-xl text-xs shadow-md shadow-emerald-600/30 transition-all flex items-center justify-center gap-2">
                        <i class="fa-solid fa-check"></i>
                        <span>Xác Nhận Nhập Hàng</span>
                    </button>
                </div>
            </form>
        </div>
    </div>

    <!-- 12. MODAL CHAT CHĂM SÓC KHÁCH HÀNG & BÁC SĨ TRỰC TUYẾN 24/7 -->
    <div x-show="showChatModal || chatModalOpen" x-cloak class="fixed inset-0 z-50 overflow-y-auto bg-slate-900/60 backdrop-blur-sm flex items-end sm:items-center justify-center sm:p-4">
        <div class="bg-white rounded-t-3xl sm:rounded-3xl max-w-lg w-full h-[85vh] sm:h-[600px] flex flex-col shadow-2xl border border-slate-100 relative animate-fadeIn overflow-hidden">
            <!-- Header -->
            <div class="p-4 bg-gradient-to-r from-emerald-600 to-teal-500 text-white flex items-center justify-between shadow">
                <div class="flex items-center gap-3">
                    <div class="relative">
                        <div class="w-10 h-10 rounded-full bg-white/20 backdrop-blur-md flex items-center justify-center text-lg">
                            <i class="fa-solid fa-user-doctor"></i>
                        </div>
                        <span class="absolute bottom-0 right-0 w-3 h-3 bg-emerald-400 border-2 border-white rounded-full"></span>
                    </div>
                    <div>
                        <h4 class="text-sm font-black">PetCare360 Live Support</h4>
                        <p class="text-[11px] text-emerald-100 flex items-center gap-1">
                            <span class="w-1.5 h-1.5 bg-emerald-300 rounded-full animate-ping"></span>
                            Bác sĩ thú y & CSKH trực tuyến 24/7
                        </p>
                    </div>
                </div>
                <button @click="showChatModal = false; chatModalOpen = false;" class="w-8 h-8 rounded-full bg-white/20 hover:bg-white/30 flex items-center justify-center text-white transition-colors">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>

            <!-- Messages Area -->
            <div class="flex-1 p-4 overflow-y-auto space-y-3 bg-slate-50/50" id="chat-messages-box">
                <template x-for="(msg, idx) in chatMessages" :key="idx">
                    <div class="flex items-start gap-2.5" :class="msg.sender === 'user' ? 'flex-row-reverse' : ''">
                        <div class="w-7 h-7 rounded-full flex items-center justify-center text-xs shrink-0" :class="msg.sender === 'user' ? 'bg-emerald-600 text-white' : 'bg-teal-100 text-teal-800'">
                            <i :class="msg.sender === 'user' ? 'fa-solid fa-user' : 'fa-solid fa-stethoscope'"></i>
                        </div>
                        <div class="max-w-[78%] rounded-2xl px-3.5 py-2.5 text-xs shadow-sm leading-relaxed" :class="msg.sender === 'user' ? 'bg-emerald-600 text-white rounded-tr-none' : 'bg-white border border-slate-200 text-slate-800 rounded-tl-none'">
                            <p x-text="msg.text"></p>
                            <span class="block text-[9px] mt-1 text-right" :class="msg.sender === 'user' ? 'text-emerald-200' : 'text-slate-400'" x-text="msg.time"></span>
                        </div>
                    </div>
                </template>
            </div>

            <!-- Quick FAQ Prompts -->
            <div class="px-4 py-2 bg-slate-100/70 border-t border-slate-200 flex items-center gap-2 overflow-x-auto text-[11px] whitespace-nowrap">
                <button @click="sendQuickChat('Tư vấn gói tiêm phòng cho mèo con 2 tháng tuổi')" class="px-2.5 py-1 bg-white hover:bg-emerald-50 text-slate-700 hover:text-emerald-700 rounded-full border border-slate-200 font-medium transition-colors">💉 Tư vấn tiêm phòng</button>
                <button @click="sendQuickChat('Kiểm tra lịch hẹn spa của tôi')" class="px-2.5 py-1 bg-white hover:bg-emerald-50 text-slate-700 hover:text-emerald-700 rounded-full border border-slate-200 font-medium transition-colors">📅 Lịch hẹn spa</button>
                <button @click="sendQuickChat('Cần hỗ trợ trường hợp thú cưng cấp cứu khẩn cấp')" class="px-2.5 py-1 bg-rose-50 hover:bg-rose-100 text-rose-700 rounded-full border border-rose-200 font-medium transition-colors">🚨 Cấp cứu 24/7</button>
            </div>

            <!-- Input area -->
            <div class="p-3 bg-white border-t border-slate-200">
                <form @submit.prevent="sendChatMessage()" class="flex items-center gap-2">
                    <input type="text" x-model="newChatMessage" placeholder="Nhập câu hỏi hoặc tình trạng của bé..." class="flex-1 px-3.5 py-2.5 rounded-xl border border-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                    <button type="submit" class="w-10 h-10 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white flex items-center justify-center shadow-md shadow-emerald-600/30 transition-all shrink-0">
                        <i class="fa-solid fa-paper-plane text-xs"></i>
                    </button>
                </form>
            </div>
        </div>
    </div>

    <!-- 13. GIỎ HÀNG DRAWER (CART DRAWER - KIỂM TRA LỊCH HẸN BẮT BUỘC TRƯỚC THANH TOÁN) -->
    <div x-show="showCartDrawer || cartOpen" x-cloak class="fixed inset-0 z-50 overflow-hidden bg-slate-900/60 backdrop-blur-sm flex justify-end">
        <div class="bg-white w-full max-w-md h-full flex flex-col shadow-2xl relative animate-slideLeft">
            <!-- Header -->
            <div class="p-4 border-b border-slate-100 flex items-center justify-between">
                <div class="flex items-center gap-2">
                    <div class="w-8 h-8 rounded-lg bg-emerald-100 text-emerald-600 flex items-center justify-center font-black">
                        <i class="fa-solid fa-cart-shopping"></i>
                    </div>
                    <div>
                        <h4 class="text-sm font-black text-slate-800">Giỏ Hàng & Lịch Hẹn</h4>
                        <p class="text-[11px] text-slate-400" x-text="cart.length + ' mục đã chọn'"></p>
                    </div>
                </div>
                <button @click="showCartDrawer = false; cartOpen = false;" class="w-8 h-8 rounded-full bg-slate-100 text-slate-500 hover:text-slate-800 flex items-center justify-center">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>

            <!-- Cart Items List -->
            <div class="flex-1 overflow-y-auto p-4 space-y-3">
                <template x-if="cart.length === 0">
                    <div class="text-center py-16 space-y-3">
                        <div class="w-16 h-16 bg-slate-100 rounded-full flex items-center justify-center text-slate-300 mx-auto text-2xl">
                            <i class="fa-solid fa-basket-shopping"></i>
                        </div>
                        <p class="text-xs font-bold text-slate-500">Giỏ hàng của bạn đang trống</p>
                        <button @click="showCartDrawer = false; cartOpen = false; activeCustomerTab = 'services'" class="px-4 py-2 bg-emerald-600 text-white rounded-xl text-xs font-bold shadow">
                            Khám phá dịch vụ & sản phẩm
                        </button>
                    </div>
                </template>

                <template x-for="(item, idx) in cart" :key="idx">
                    <div class="p-3 rounded-2xl border transition-all" :class="item.isService && (!item.bookingDate || !item.selectedPet) ? 'border-amber-400 bg-amber-50/40' : 'border-slate-200 bg-white'">
                        <div class="flex items-center gap-3">
                            <img :src="item.img || item.image" class="w-14 h-14 rounded-xl object-cover shrink-0">
                            <div class="flex-1 min-w-0">
                                <div class="flex items-center gap-1.5">
                                    <span class="text-[9px] font-black uppercase px-1.5 py-0.5 rounded" :class="item.isService ? 'bg-teal-100 text-teal-800' : 'bg-blue-100 text-blue-800'" x-text="item.isService ? 'Dịch vụ' : 'Sản phẩm'"></span>
                                    <h5 class="text-xs font-black text-slate-800 truncate" x-text="item.name"></h5>
                                </div>
                                <p class="text-xs font-bold text-emerald-600 mt-0.5" x-text="formatCurrency(item.price)"></p>
                                
                                <!-- Quantity if product -->
                                <template x-if="!item.isService">
                                    <div class="flex items-center gap-2 mt-1">
                                        <div class="flex items-center border border-slate-200 rounded-lg overflow-hidden">
                                            <button @click="if(item.qty > 1) item.qty--" class="w-6 h-6 flex items-center justify-center bg-slate-50 text-slate-600 text-xs font-bold">-</button>
                                            <span class="w-8 text-center text-xs font-bold text-slate-800" x-text="item.qty"></span>
                                            <button @click="item.qty++" class="w-6 h-6 flex items-center justify-center bg-slate-50 text-slate-600 text-xs font-bold">+</button>
                                        </div>
                                    </div>
                                </template>
                            </div>
                            <button @click="removeFromCart(idx)" class="text-slate-300 hover:text-rose-500 p-1">
                                <i class="fa-solid fa-trash-can text-sm"></i>
                            </button>
                        </div>

                        <!-- Nếu là Dịch Vụ: Hiện thông tin Đặt Lịch Hoặc Nhắc Nhở Bắt Buộc Điền -->
                        <template x-if="item.isService">
                            <div class="mt-2.5 pt-2 border-t border-slate-100/80">
                                <template x-if="item.bookingDate && item.selectedPet">
                                    <div class="bg-emerald-50 p-2 rounded-xl text-[11px] text-emerald-800 flex items-center justify-between">
                                        <div>
                                            <p class="font-bold"><i class="fa-solid fa-calendar-check text-emerald-600 mr-1"></i> <span x-text="item.bookingDate + ' (' + (item.bookingTime || '09:00') + ')'"></span></p>
                                            <p class="text-[10px] text-emerald-700"><i class="fa-solid fa-paw mr-1"></i> <span x-text="'Bé: ' + item.selectedPet"></span></p>
                                        </div>
                                        <button @click="openBookingModalForService(item)" class="text-emerald-700 hover:text-emerald-900 font-bold underline text-[10px]">
                                            Sửa lịch
                                        </button>
                                    </div>
                                </template>
                                <template x-if="!item.bookingDate || !item.selectedPet">
                                    <div class="bg-amber-100/80 p-2 rounded-xl text-[11px] text-amber-900 flex items-center justify-between">
                                        <div class="flex items-center gap-1.5">
                                            <i class="fa-solid fa-circle-exclamation text-amber-600 animate-bounce"></i>
                                            <span class="font-bold text-[10px]">Chưa điền lịch hẹn chi tiết!</span>
                                        </div>
                                        <button @click="openBookingModalForService(item)" class="px-2.5 py-1 bg-amber-500 hover:bg-amber-600 text-white rounded-lg font-bold text-[10px] shadow-sm">
                                            Điền ngay
                                        </button>
                                    </div>
                                </template>
                            </div>
                        </template>
                    </div>
                </template>
            </div>

            <!-- Footer Checkout with Validation Check -->
            <div class="p-4 border-t border-slate-100 bg-slate-50 space-y-3">
                <div class="flex items-center justify-between text-xs">
                    <span class="text-slate-500">Tạm tính:</span>
                    <span class="font-bold text-slate-800" x-text="formatCurrency(cartTotal)"></span>
                </div>
                <div class="flex items-center justify-between text-xs">
                    <span class="text-slate-500">Phí dịch vụ / Vận chuyển:</span>
                    <span class="font-bold text-emerald-600">Miễn phí</span>
                </div>
                <div class="flex items-center justify-between text-sm font-black pt-2 border-t border-slate-200">
                    <span class="text-slate-800">Tổng thanh toán:</span>
                    <span class="text-lg text-emerald-600 font-black" x-text="formatCurrency(cartTotal)"></span>
                </div>

                <button @click="checkAndOpenCheckout()" class="w-full py-3 bg-emerald-600 hover:bg-emerald-700 text-white font-black rounded-xl text-xs uppercase tracking-wider shadow-lg shadow-emerald-600/30 transition-all flex items-center justify-center gap-2">
                    <i class="fa-solid fa-credit-card"></i>
                    <span>Tiến Hành Thanh Toán Đơn Hàng</span>
                </button>
            </div>
        </div>
    </div>

    <!-- 14. MODAL THANH TOÁN (CHECKOUT MODAL - REALTIME CẬP NHẬT QUA ADMIN) -->
    <div x-show="showCheckoutModal" x-cloak class="fixed inset-0 z-50 overflow-y-auto bg-slate-900/70 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-xl w-full p-6 md:p-8 shadow-2xl border border-slate-100 relative animate-fadeIn">
            <button @click="showCheckoutModal = false" class="absolute top-5 right-5 text-slate-400 hover:text-slate-600 w-9 h-9 rounded-full bg-slate-100 flex items-center justify-center transition-colors">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>

            <div class="text-center mb-6">
                <span class="px-3 py-1 bg-emerald-100 text-emerald-700 text-[11px] font-black rounded-full uppercase">Thanh toán an toàn</span>
                <h3 class="text-2xl font-black text-slate-800 mt-2">Xác Nhận Đơn Hàng & Dịch Vụ</h3>
                <p class="text-xs text-slate-500 mt-0.5">PetCare360 cam kết bảo mật thông tin & y đức chuẩn mực</p>
            </div>

            <form @submit.prevent="confirmOrderAndPay()" class="space-y-4">
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Họ tên người nhận / đặt lịch</label>
                        <input type="text" x-model="checkoutForm.name" required class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Số điện thoại liên hệ</label>
                        <input type="tel" x-model="checkoutForm.phone" required class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                    </div>
                </div>

                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Địa chỉ giao hàng / Chi nhánh hẹn</label>
                    <input type="text" x-model="checkoutForm.address" required class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs font-semibold focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500">
                </div>

                <!-- Phương thức thanh toán -->
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-2">Phương thức thanh toán</label>
                    <div class="space-y-2">
                        <label class="flex items-center justify-between p-3 rounded-xl border border-slate-200 cursor-pointer hover:bg-slate-50" :class="checkoutForm.paymentMethod === 'cod' ? 'border-emerald-500 bg-emerald-50/30' : ''">
                            <div class="flex items-center gap-3">
                                <input type="radio" value="cod" x-model="checkoutForm.paymentMethod" class="text-emerald-600 focus:ring-0">
                                <div>
                                    <span class="block text-xs font-bold text-slate-800">Thanh toán khi nhận hàng / tại quầy (COD)</span>
                                    <span class="block text-[11px] text-slate-500">Tiền mặt hoặc quẹt thẻ POS khi nhân viên phục vụ</span>
                                </div>
                            </div>
                            <i class="fa-solid fa-money-bill-wave text-emerald-600 text-lg"></i>
                        </label>

                        <label class="flex items-center justify-between p-3 rounded-xl border border-slate-200 cursor-pointer hover:bg-slate-50" :class="checkoutForm.paymentMethod === 'vietqr' ? 'border-emerald-500 bg-emerald-50/30' : ''">
                            <div class="flex items-center gap-3">
                                <input type="radio" value="vietqr" x-model="checkoutForm.paymentMethod" class="text-emerald-600 focus:ring-0">
                                <div>
                                    <span class="block text-xs font-bold text-slate-800">Chuyển khoản VietQR Napas 24/7 (Khuyên dùng)</span>
                                    <span class="block text-[11px] text-slate-500">Quét mã QR tự động xác nhận đơn trong 3 giây</span>
                                </div>
                            </div>
                            <i class="fa-solid fa-qrcode text-indigo-600 text-lg"></i>
                        </label>

                        <label class="flex items-center justify-between p-3 rounded-xl border border-slate-200 cursor-pointer hover:bg-slate-50" :class="checkoutForm.paymentMethod === 'momo' ? 'border-emerald-500 bg-emerald-50/30' : ''">
                            <div class="flex items-center gap-3">
                                <input type="radio" value="momo" x-model="checkoutForm.paymentMethod" class="text-emerald-600 focus:ring-0">
                                <div>
                                    <span class="block text-xs font-bold text-slate-800">Ví điện tử MoMo</span>
                                    <span class="block text-[11px] text-slate-500">Liên kết ví MoMo thanh toán siêu tốc</span>
                                </div>
                            </div>
                            <span class="px-2 py-0.5 bg-pink-100 text-pink-700 text-[10px] font-black rounded">MoMo</span>
                        </label>
                    </div>
                </div>

                <!-- QR Display if VietQR selected -->
                <div x-show="checkoutForm.paymentMethod === 'vietqr'" class="p-4 bg-slate-50 rounded-2xl border border-slate-200 text-center space-y-2">
                    <p class="text-xs font-bold text-slate-700">Mã QR Thanh Toán Tự Động (VietinBank)</p>
                    <img :src="'https://api.vietqr.io/image/970415-113366668888-compact2.png?amount=' + cartTotal + '&addInfo=PETCARE360%20ORDER&accountName=PETCARE360%20VIETNAM'" class="w-48 h-48 mx-auto rounded-xl border shadow-sm object-contain bg-white p-2">
                    <p class="text-[11px] text-slate-500">Số tài khoản: <strong>113366668888</strong> • Chủ TK: <strong>PETCARE360 VIETNAM</strong></p>
                </div>

                <!-- Order summary box -->
                <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200 space-y-2 text-xs">
                    <div class="flex justify-between font-bold text-slate-700">
                        <span>Số lượng sản phẩm & dịch vụ:</span>
                        <span x-text="cart.length + ' mục'"></span>
                    </div>
                    <div class="flex justify-between font-bold text-slate-700">
                        <span>Tích lũy điểm thành viên:</span>
                        <span class="text-emerald-600" x-text="'+' + Math.floor(cartTotal / 10000) + ' điểm'"></span>
                    </div>
                    <div class="flex justify-between font-black text-slate-800 text-sm pt-2 border-t border-slate-200">
                        <span>Tổng tiền cần thanh toán:</span>
                        <span class="text-emerald-600 text-base" x-text="formatCurrency(cartTotal)"></span>
                    </div>
                </div>

                <div class="flex items-center gap-3 pt-2">
                    <button type="button" @click="showCheckoutModal = false" class="w-1/3 py-3 border border-slate-200 text-slate-600 font-bold rounded-xl text-xs hover:bg-slate-50">
                        Quay lại giỏ
                    </button>
                    <button type="submit" class="w-2/3 py-3 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-xl text-xs shadow-lg shadow-emerald-600/30 transition-all flex items-center justify-center gap-2">
                        <i class="fa-solid fa-lock"></i>
                        <span>Xác Nhận & Hoàn Tất Đơn Hàng</span>
                    </button>
                </div>
            </form>
        </div>
    </div>

    <!-- 15. MODAL CHÍNH SÁCH & PHÁP LÝ CHI TIẾT NHẤT CÓ THỂ -->
    <div x-show="showLegalModal || policyModalOpen" x-cloak class="fixed inset-0 z-50 overflow-y-auto bg-slate-900/70 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-3xl w-full max-h-[90vh] overflow-y-auto p-6 md:p-8 shadow-2xl border border-slate-100 relative animate-fadeIn">
            <button @click="showLegalModal = false; policyModalOpen = false;" class="absolute top-5 right-5 text-slate-400 hover:text-slate-600 w-9 h-9 rounded-full bg-slate-100 flex items-center justify-center transition-colors">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>

            <div class="text-center mb-6">
                <div class="w-14 h-14 bg-emerald-100 rounded-2xl flex items-center justify-center mx-auto text-emerald-600 text-2xl shadow-sm mb-2">
                    <i class="fa-solid fa-scale-balanced"></i>
                </div>
                <h3 class="text-2xl font-black text-slate-800">Chính Sách & Quy Định Pháp Lý PetCare360</h3>
                <p class="text-xs text-slate-500 mt-1">Hệ thống văn bản pháp lý & cam kết bảo vệ quyền lợi khách hàng chuẩn y khoa</p>
            </div>

            <div class="space-y-6 text-xs text-slate-700 leading-relaxed">
                <!-- Section 1 -->
                <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200">
                    <h4 class="text-sm font-black text-slate-800 mb-2 flex items-center gap-2">
                        <span class="w-6 h-6 rounded-lg bg-emerald-600 text-white flex items-center justify-center text-xs">1</span>
                        Chính Sách Bảo Mật Dữ Liệu & Thông Tin Khách Hàng (Nghị định 13/2023/NĐ-CP)
                    </h4>
                    <p class="text-slate-600">
                        PetCare360 cam kết bảo vệ tối đa dữ liệu định danh cá nhân (Họ tên, SĐT, Địa chỉ, Hồ sơ bệnh án thú cưng). Toàn bộ dữ liệu giao dịch thanh toán trực tuyến qua Napas 24/7 và cổng thanh toán được mã hóa chuẩn SSL 256-bit cao nhất. Chúng tôi cam kết tuyệt đối không chia sẻ, bán hoặc cung cấp thông tin khách hàng cho bất kỳ bên thứ ba nào vì mục đích quảng cáo thương mại trái phép.
                    </p>
                </div>

                <!-- Section 2 -->
                <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200">
                    <h4 class="text-sm font-black text-slate-800 mb-2 flex items-center gap-2">
                        <span class="w-6 h-6 rounded-lg bg-emerald-600 text-white flex items-center justify-center text-xs">2</span>
                        Quy Chế Hoạt Động Y Tế & Cam Kết Y Đức Thú Y Chuẩn Mực
                    </h4>
                    <p class="text-slate-600">
                        Mọi dịch vụ khám chữa bệnh, phẫu thuật nội soi, tiêm chủng và xét nghiệm cận lâm sàng tại PetCare360 đều được thực hiện bởi đội ngũ Bác sĩ Thú y có chứng chỉ hành nghề chính quy được cấp phép bởi Cục Thú y Việt Nam. Mọi can thiệp y tế đều có biên bản cam kết rõ ràng, minh bạch chi phí trước khi thực hiện và không tự ý phát sinh chi phí ngoài dự toán.
                    </p>
                </div>

                <!-- Section 3 -->
                <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200">
                    <h4 class="text-sm font-black text-slate-800 mb-2 flex items-center gap-2">
                        <span class="w-6 h-6 rounded-lg bg-emerald-600 text-white flex items-center justify-center text-xs">3</span>
                        Chính Sách Hoàn Tiền, Đổi Trả Sản Phẩm & Bồi Thường Rủi Ro
                    </h4>
                    <p class="text-slate-600">
                        • <strong>Sản phẩm hàng hóa:</strong> Đổi trả miễn phí 1-đổi-1 trong vòng 07 ngày đối với các sản phẩm thức ăn hạt, phụ kiện có lỗi sản xuất hoặc phát sinh hỏng vỡ trong quá trình vận chuyển.<br>
                        • <strong>Dịch vụ Spa & Lưu trú:</strong> Hoàn tiền 100% chi phí dịch vụ nếu thú cưng có biểu hiện trầy xước da hoặc không đạt tiêu chuẩn vệ sinh đã cam kết.<br>
                        • <strong>Bảo hiểm rủi ro:</strong> Gói bảo hiểm sức khỏe thú cưng đồng hành chi trả bồi thường đến 100% chi phí điều trị phát sinh trong trường hợp có sơ suất kỹ thuật từ phía nhân sự bệnh viện.
                    </p>
                </div>

                <!-- Section 4 -->
                <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200">
                    <h4 class="text-sm font-black text-slate-800 mb-2 flex items-center gap-2">
                        <span class="w-6 h-6 rounded-lg bg-emerald-600 text-white flex items-center justify-center text-xs">4</span>
                        Giấy Phép Hoạt Động & Cơ Sở Pháp Lý
                    </h4>
                    <p class="text-slate-600">
                        • Giấy chứng nhận đăng ký doanh nghiệp số: <strong>0318999888</strong> do Sở Kế hoạch & Đầu tư TP.HCM cấp.<br>
                        • Giấy chứng nhận đủ điều kiện buôn bán thuốc thú y và dịch vụ phẫu thuật động vật số <strong>54/GCN-TY</strong> cấp bởi Chi cục Chăn nuôi và Thú y.<br>
                        • Địa chỉ trụ sở chính: 450 Nguyễn Thị Thập, Phường Tân Quy, Quận 7, TP. Hồ Chí Minh. Hotline tiếp nhận khiếu nại pháp lý: <strong>1900 6868</strong>.
                    </p>
                </div>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-100 text-right">
                <button @click="showLegalModal = false; policyModalOpen = false;" class="px-6 py-2.5 bg-slate-800 hover:bg-slate-900 text-white font-bold rounded-xl text-xs transition-colors">
                    Đã đọc & Đồng ý
                </button>
            </div>
        </div>
    </div>

</div>
<!-- ==================== HẾT CÁC MODAL HỆ THỐNG ==================== -->
'''
