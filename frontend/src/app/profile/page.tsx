export default function Profile() {
  return (
    <div className="min-h-screen bg-gray-50 py-12">
      <div className="max-w-md mx-auto bg-white rounded-lg shadow-md p-6">
        <h1 className="text-2xl font-bold text-center mb-6">User Profile</h1>
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700">Name</label>
            <p className="mt-1 text-sm text-gray-900">John Doe</p>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">Email</label>
            <p className="mt-1 text-sm text-gray-900">john@example.com</p>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">Subscription</label>
            <p className="mt-1 text-sm text-gray-900">Premium</p>
          </div>
        </div>
      </div>
    </div>
  )
}