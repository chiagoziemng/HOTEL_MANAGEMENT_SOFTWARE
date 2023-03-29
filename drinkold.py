
# class Drink(models.Model):
#     CATEGORY_CHOICES = [
#         ('Soft-drink/Non-alcoholic', 'Soft-drink/Non-alcoholic'),
#         ('Beer', 'Beer'),
#         ('Blended-spirit/Whiskey/Wine', 'Blended-spirit/Whiskey/Wine'),
#         ('Others', 'Others')
#     ]
#     name = models.CharField(max_length=100)
#     category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Others')
#     image = models.ImageField(upload_to='drinks', default='drinks/default.png' ,blank=True, null=True)
#     opening_stock = models.IntegerField(default=0)
#     new_stock = models.IntegerField(default=0)
#     total_stock = models.IntegerField(default=0)
#     total_sales = models.DecimalField(max_digits=10, decimal_places=2, default=0) # Added a new field called 'total_sales'

#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     number_sold = models.IntegerField(default=0)
#     damage = models.IntegerField(default=0)
#     amount_sold = models.DecimalField(max_digits=10, decimal_places=2)
#     closing_stock = models.IntegerField(default=0)
#     date_created = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.name
    

#     class Meta:
#         verbose_name_plural = 'Drinks'

#     def save(self, *args, **kwargs):
#         self.total_stock = self.opening_stock + self.new_stock
#         self.closing_stock = self.total_stock - self.number_sold - self.damage
#         self.amount_sold = self.number_sold * self.price
#         super().save(*args, **kwargs)
#  Defined Drink Form
# class DrinkForm(forms.ModelForm):
#     class Meta:
#         model = Drink
#         fields = ['name','category','opening_stock', 'new_stock', 'price', 'damage', 'image']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'category': forms.Select(attrs={'class': 'form-control'}),
#             'opening_stock': forms.NumberInput(attrs={'class': 'form-control'}),
#             'new_stock': forms.NumberInput(attrs={'class': 'form-control'}),
#             'price': forms.NumberInput(attrs={'class': 'form-control'}),
#             'damage': forms.NumberInput(attrs={'class': 'form-control'}),
#             'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            
#         }
  <!-- Bootstrap Toasts Styles -->
              <div class="card mb-4">
                <h5 class="card-header">Bootstrap Toasts Styles</h5>
                <div class="row g-0">
                  <div class="col-md-6 p-4">
                    <div class="text-light small fw-semibold mb-3">Default</div>
                    <div class="toast-container">
                      <div class="bs-toast toast fade show" role="alert" aria-live="assertive" aria-atomic="true">
                        <div class="toast-header">
                          <i class="bx bx-bell me-2"></i>
                          <div class="me-auto fw-semibold">Bootstrap</div>
                          <small>11 mins ago</small>
                          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                        <div class="toast-body">
                          Fruitcake chocolate bar tootsie roll gummies gummies jelly beans cake.
                        </div>
                      </div>

                      <div
                        class="bs-toast toast fade show bg-primary"
                        role="alert"
                        aria-live="assertive"
                        aria-atomic="true"
                      >
                        <div class="toast-header">
                          <i class="bx bx-bell me-2"></i>
                          <div class="me-auto fw-semibold">Bootstrap</div>
                          <small>11 mins ago</small>
                          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                        <div class="toast-body">
                          Fruitcake chocolate bar tootsie roll gummies gummies jelly beans cake.
                        </div>
                      </div>

                      <div
                        class="bs-toast toast fade show bg-secondary"
                        role="alert"
                        aria-live="assertive"
                        aria-atomic="true"
                      >
                        <div class="toast-header">
                          <i class="bx bx-bell me-2"></i>
                          <div class="me-auto fw-semibold">Bootstrap</div>
                          <small>11 mins ago</small>
                          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                        <div class="toast-body">
                          Fruitcake chocolate bar tootsie roll gummies gummies jelly beans cake.
                        </div>
                      </div>

                      <div
                        class="bs-toast toast fade show bg-success"
                        role="alert"
                        aria-live="assertive"
                        aria-atomic="true"
                      >
                        <div class="toast-header">
                          <i class="bx bx-bell me-2"></i>
                          <div class="me-auto fw-semibold">Bootstrap</div>
                          <small>11 mins ago</small>
                          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                        <div class="toast-body">
                          Fruitcake chocolate bar tootsie roll gummies gummies jelly beans cake.
                        </div>
                      </div>

                      <div
                        class="bs-toast toast fade show bg-danger"
                        role="alert"
                        aria-live="assertive"
                        aria-atomic="true"
                      >
                        <div class="toast-header">
                          <i class="bx bx-bell me-2"></i>
                          <div class="me-auto fw-semibold">Bootstrap</div>
                          <small>11 mins ago</small>
                          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                        <div class="toast-body">
                          Fruitcake chocolate bar tootsie roll gummies gummies jelly beans cake.
                        </div>
                      </div>

                      <div
                        class="bs-toast toast fade show bg-warning"
                        role="alert"
                        aria-live="assertive"
                        aria-atomic="true"
                      >
                        <div class="toast-header">
                          <i class="bx bx-bell me-2"></i>
                          <div class="me-auto fw-semibold">Bootstrap</div>
                          <small>11 mins ago</small>
                          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                        <div class="toast-body">
                          Fruitcake chocolate bar tootsie roll gummies gummies jelly beans cake.
                        </div>
                      </div>

                      <div
                        class="bs-toast toast fade show bg-info"
                        role="alert"
                        aria-live="assertive"
                        aria-atomic="true"
                      >
                        <div class="toast-header">
                          <i class="bx bx-bell me-2"></i>
                          <div class="me-auto fw-semibold">Bootstrap</div>
                          <small>11 mins ago</small>
                          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                        <div class="toast-body">
                          Fruitcake chocolate bar tootsie roll gummies gummies jelly beans cake.
                        </div>
                      </div>

                      <div
                        class="bs-toast toast fade show bg-dark"
                        role="alert"
                        aria-live="assertive"
                        aria-atomic="true"
                      >
                        <div class="toast-header">
                          <i class="bx bx-bell me-2"></i>
                          <div class="me-auto fw-semibold">Bootstrap</div>
                          <small>11 mins ago</small>
                          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                        <div class="toast-body">
                          Fruitcake chocolate bar tootsie roll gummies gummies jelly beans cake.
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6 ui-bg-overlay-container p-4">
                    <div class="ui-bg-overlay bg-dark opacity-75 rounded-end-bottom"></div>
                    <div class="text-white small fw-semibold mb-3">Translucent</div>

                    <div class="toast-container">
                      <div class="bs-toast toast fade show" role="alert" aria-live="assertive" aria-atomic="true">
                        <div class="toast-header">
                          <i class="bx bx-bell me-2"></i>
                          <div class="me-auto fw-semibold">Bootstrap</div>
                          <small>11 mins ago</small>
                          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                        <div class="toast-body">
                          Fruitcake chocolate bar tootsie roll gummies gummies jelly beans cake.
                        </div>
                      </div>

                      <div
                        class="bs-toast toast fade show bg-primary"
                        role="alert"
                        aria-live="assertive"
                        aria-atomic="true"
                      >
                        <div class="toast-header">
                          <i class="bx bx-bell me-2"></i>
                          <div class="me-auto fw-semibold">Bootstrap</div>
                          <small>11 mins ago</small>
                          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                        <div class="toast-body">
                          Fruitcake chocolate bar tootsie roll gummies gummies jelly beans cake.
                        </div>
                      </div>

                      <div
                        class="bs-toast toast fade show bg-secondary"
                        role="alert"
                        aria-live="assertive"
                        aria-atomic="true"
                      >
                        <div class="toast-header">
                          <i class="bx bx-bell me-2"></i>
                          <div class="me-auto fw-semibold">Bootstrap</div>
                          <small>11 mins ago</small>
                          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                        <div class="toast-body">
                          Fruitcake chocolate bar tootsie roll gummies gummies jelly beans cake.
                        </div>
                      </div>

                      <div
                        class="bs-toast toast fade show bg-success"
                        role="alert"
                        aria-live="assertive"
                        aria-atomic="true"
                      >
                        <div class="toast-header">
                          <i class="bx bx-bell me-2"></i>
                          <div class="me-auto fw-semibold">Bootstrap</div>
                          <small>11 mins ago</small>
                          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                        <div class="toast-body">
                          Fruitcake chocolate bar tootsie roll gummies gummies jelly beans cake.
                        </div>
                      </div>

                      <div
                        class="bs-toast toast fade show bg-danger"
                        role="alert"
                        aria-live="assertive"
                        aria-atomic="true"
                      >
                        <div class="toast-header">
                          <i class="bx bx-bell me-2"></i>
                          <div class="me-auto fw-semibold">Bootstrap</div>
                          <small>11 mins ago</small>
                          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                        <div class="toast-body">
                          Fruitcake chocolate bar tootsie roll gummies gummies jelly beans cake.
                        </div>
                      </div>

                      <div
                        class="bs-toast toast fade show bg-warning"
                        role="alert"
                        aria-live="assertive"
                        aria-atomic="true"
                      >
                        <div class="toast-header">
                          <i class="bx bx-bell me-2"></i>
                          <div class="me-auto fw-semibold">Bootstrap</div>
                          <small>11 mins ago</small>
                          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                        <div class="toast-body">
                          Fruitcake chocolate bar tootsie roll gummies gummies jelly beans cake.
                        </div>
                      </div>

                      <div
                        class="bs-toast toast fade show bg-info"
                        role="alert"
                        aria-live="assertive"
                        aria-atomic="true"
                      >
                        <div class="toast-header">
                          <i class="bx bx-bell me-2"></i>
                          <div class="me-auto fw-semibold">Bootstrap</div>
                          <small>11 mins ago</small>
                          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                        <div class="toast-body">
                          Fruitcake chocolate bar tootsie roll gummies gummies jelly beans cake.
                        </div>
                      </div>

                      <div
                        class="bs-toast toast fade show bg-dark"
                        role="alert"
                        aria-live="assertive"
                        aria-atomic="true"
                      >
                        <div class="toast-header">
                          <i class="bx bx-bell me-2"></i>
                          <div class="me-auto fw-semibold">Bootstrap</div>
                          <small>11 mins ago</small>
                          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                        <div class="toast-body">
                          Fruitcake chocolate bar tootsie roll gummies gummies jelly beans cake.
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <!--/ Bootstrap Toasts Styles -->
